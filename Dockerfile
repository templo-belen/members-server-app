FROM python:3.12-alpine

WORKDIR /code

RUN pip install --upgrade pip

COPY ./setup.cfg /code/setup.cfg
COPY ./setup.py /code/setup.py
COPY ./pyproject.toml /code/pyproject.toml
RUN pip install .

COPY ./app /code/app


CMD ["fastapi", "run", "app", "--port", "80"]
