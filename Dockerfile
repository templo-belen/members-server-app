FROM python:3.12-alpine

WORKDIR /code

RUN pip install --upgrade pip

COPY ./setup.cfg /code/setup.cfg
COPY ./setup.py /code/setup.py
COPY ./pyproject.toml /code/pyproject.toml
COPY ./app /code/app

RUN pip install .

CMD ["fastapi", "run", "app", "--port", "80"]
