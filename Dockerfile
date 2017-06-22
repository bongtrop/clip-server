FROM ubuntu

MAINTAINER Pongsakorn Sommalai "bongtrop@gmail.com"

RUN apt-get update && apt-get install -y python-pip python-dev build-essential

COPY requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /clip-server
WORKDIR /clip-server

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]