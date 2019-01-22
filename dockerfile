FROM python:3

MAINTAINER Tomas Cernak "cernak.tomi@gmail.com"

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

RUN apt update && apt -y install locales

COPY . /app

WORKDIR ./app

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "web_currency_converter.py"]
