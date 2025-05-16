FROM python:3.12-alpine

WORKDIR /code

COPY ./setup.cfg /code/setup.cfg
COPY ./setup.py /code/setup.py
COPY ./pyproject.toml /code/pyproject.toml
COPY ./app /code/app

RUN pip install --upgrade pip

RUN ["ls"]

RUN pip install .

CMD ["fastapi", "run", "app/main.py", "--port", "80"]