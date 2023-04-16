FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH="/.venv/bin:$PATH"
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY . /bot_helper

COPY pyproject.toml /bot_helper

WORKDIR /bot_helper

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD poetry run bot
