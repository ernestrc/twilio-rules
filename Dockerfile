FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get -y install python python-pip build-essential libpq-dev python-dev

ADD requirements.txt /src/requirements.txt
ADD ./src /src

EXPOSE 8888

RUN cd /src; pip install -r requirements.txt

CMD ["python", "/src/api.py"]
