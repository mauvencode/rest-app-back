FROM python:3.10-slim

RUN pip install --upgrade pip
RUN pip install poetry
RUN apt-get update
RUN apt-get install libxmlsec1-dev pkg-config -y

COPY poetry.lock pyproject.toml /code/
WORKDIR /code
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
