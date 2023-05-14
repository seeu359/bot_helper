from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from datetime import datetime

from src.bot.events import algo_courses as algo_events
from src.domain import models
from src.domain.business_layer import algo_courses
from src.bot.keybords.algo_courses import (
    get_action,
    get_course,
    get_premium,
    python_course_cb_data,
    python_premium_cb_data,
)



async def algo_courses(message: types.Message):
    await message.answer('Choose your action:', reply_markup=get_action())


async def select_course(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Select course:', reply_markup=get_course())
    await algo_events.AddTask.course.set()


async def select_date(callback_query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    course = callback_data.get('course')
    await state.update_data(course=course)
    await callback_query.message.answer('Enter data in format mm-dd')
    await algo_events.AddTask.next()


async def select_time(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer('Choose time in format hh:mm')
    await algo_events.AddTask.next()


async def select_premium(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer('Select premium:', reply_markup=get_premium())


async def add_algo_course(callback_query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    premium = callback_data.get('premium')
    await state.update_data(premium=premium)
    data = await state.get_data()
    date_time = f'2023-{data.get("date")} {data.get("time")}:00'
    date_time = datetime.strptime(date_time, format='%m-%d-%Y %H:%M:%S')
    course_id = models.Course(name=data.get('course'))
    course = models.AlgoCourse(premium=premium, datetime=date_time, user_id=1, course_id=course_id())
    course_data = algo_courses.AlgoCourseData(algo_course=course)
    await callback_query.message.answer(course_data.salary())
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(algo_courses, commands='courses')
    dp.register_callback_query_handler(select_course, lambda call: call.data == 'add course')
    dp.register_callback_query_handler(
        select_date, python_course_cb_data.filter(), state=algo_events.AddTask.course
    )
    dp.register_message_handler(
        select_time, state=algo_events.AddTask.date,
    )
    dp.register_message_handler(
        select_premium, state=algo_events.AddTask.time,
    )
    dp.register_callback_query_handler(
        add_algo_course, python_premium_cb_data.filter(), state=algo_events.AddTask.premium
    )
