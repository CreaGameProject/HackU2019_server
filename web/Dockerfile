FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
RUN mkdir /code
WORKDIR /code
RUN pip install -U pip
RUN pip install pipenv
RUN apt update && apt upgrade -y
RUN apt install -y at && service atd start
