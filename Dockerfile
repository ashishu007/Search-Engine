FROM python:slim

# FROM ubuntu:18.04
# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev && \
#     apt-get -y install locales

# ENV LC_ALL=C.UTF-8
# ENV LANG=C.UTF-8

WORKDIR /code
# ENV FLASK_APP main.py
# ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD ["flask", "run"]
CMD gunicorn --bind 0.0.0.0:$PORT main
