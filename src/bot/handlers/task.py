from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from dataclasses import asdict
from loguru import logger

from src.bot.events import task as task_events
from src.bot import bot
from src.service import formatters
from src.domain import bussines_rules, models
from src.service import uow as _uow
from src.bot.keybords.task import (
    get_action,
    get_month,
    get_task_period,
    get_inline_for_tasks,
    task_cb_data,
    task_done_cb_data,
    inline_done_for_task,
)


async def tasks(message: types.Message):
    await message.reply('Choose your action:', reply_markup=get_action())


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('All action is canceled', reply_markup=types.ReplyKeyboardRemove())


async def select_title(query: types.CallbackQuery):
    await query.message.delete()
    await bot.send_message(query.from_user.id, text='Select task title')
    await task_events.AddTask.title.set()


async def select_description(message: types.Message, state: FSMContext):
    await message.delete()
    await state.update_data(title=message.text)
    await message.answer('Type task description')
    await task_events.AddTask.next()


async def select_months_day(message: types.Message, state: FSMContext):
    await message.delete()
    await state.update_data(description=message.text)
    await message.answer('Enter the day of the month as a regular number')
    await task_events.AddTask.next()


async def select_month(message: types.Message, state: FSMContext):
    await message.delete()
    await state.update_data(month_day=message.text)
    await message.answer('Select month', reply_markup=get_month())
    await task_events.AddTask.next()


async def add_task(message: types.Message, state: FSMContext):
    await message.delete()
    await state.update_data(month=message.text)
    data = await state.get_data()
    data['user_id'] = message.from_user.id
    date = bussines_rules.format_day(
        int(data.get('month_day')), data.get('month')
    )
    data['start_date'] = date
    data.pop('month')
    data.pop('month_day')

    uow = _uow.DatabaseService()
    with uow:
        task = models.Task(**data)
        user = uow.item.get(models.User, message.from_user.id)
        if user is None:
            user = models.User(
                id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
            )
            uow.item.add(user)
            uow.commit()
        uow.item.add(task)
        uow.commit()
    await state.finish()
    await message.reply(
        'Task successfully added', reply_markup=ReplyKeyboardRemove()
    )


async def get_sample_type(query: types.CallbackQuery):
    await query.message.delete()
    await bot.send_message(
        query.from_user.id,
        text='What task to display?',
        reply_markup=get_task_period()
    )
    await task_events.GetTasks.period.set()


async def get_tasks(message: types.Message, state: FSMContext):
    await state.update_data(period=message.text)
    data = await state.get_data()
    uow = _uow.DatabaseService()

    period = models.Task.get_period(data.get('period'))

    with uow:
        if period is None:
            _tasks = uow.item.get_list(
                models.Task, user_id=message.from_user.id
            )
        else:
            logger.info(f'Get task for date {period.day}')
            _tasks = uow.item.get_list(
                models.Task, user_id=message.from_user.id, period=period
            )

    output = 'You\'re have no tasks' if len(_tasks) == 0 else 'Your Task'
    await state.finish()
    await message.answer(
        text=output, reply_markup=get_inline_for_tasks(_tasks)
    )


async def get_task_info(query: types.CallbackQuery, callback_data: dict):
    await query.message.delete()
    task_id = callback_data.get('task_id')
    user_id = query.from_user.id
    uow = _uow.DatabaseService()
    with uow:
        task = uow.item.get(models.Task, user_id, task_id)
    formatter = formatters.TaskFormatter()
    await bot.send_message(
        query.from_user.id, formatter.format(task),
        reply_markup=inline_done_for_task(task_id)
    )


async def done_task(query: types.CallbackQuery, callback_data: dict):
    await query.message.delete()
    task_id = callback_data.get('task_id')
    user_id = query.from_user.id
    uow = _uow.DatabaseService()
    with uow:
        task = uow.item.get(models.Task, user_id, task_id)
        d_task = models.DoneTask(**asdict(task))
        uow.item.done(d_task)
        uow.item.delete(task)
        uow.commit()
    await bot.send_message(query.from_user.id, 'Task has been done')


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        get_sample_type, lambda call: call.data == 'get tasks'
    )
    dp.register_callback_query_handler(
        select_title, lambda call: call.data == 'add task', state=None
    )
    dp.register_message_handler(cancel, state="*", commands="cancel")
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(tasks, commands='tasks', state=None)

    dp.register_callback_query_handler(
        get_task_info, task_cb_data.filter()
    )
    dp.register_callback_query_handler(
        done_task, task_done_cb_data.filter()
    )

    dp.register_message_handler(
        get_tasks, state=task_events.GetTasks.period
    )
    dp.register_message_handler(
        select_description, state=task_events.AddTask.title
    )
    dp.register_message_handler(
        select_months_day, state=task_events.AddTask.description
    )
    dp.register_message_handler(
        select_month, state=task_events.AddTask.month_day
    )
    dp.register_message_handler(add_task, state=task_events.AddTask.month)
