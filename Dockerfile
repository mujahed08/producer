FROM python:3.9

COPY . /dist

WORKDIR /dist

RUN pip install -r requirements.txt
