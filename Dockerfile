ARG VERSION=3.12

FROM python:${VERSION}-slim-bullseye

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code/app

CMD ["fastapi", "run", "app/main.py", "--proxy-headers",  "--port", "80"]

