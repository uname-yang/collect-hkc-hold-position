FROM python:3

ADD ./requirements.txt /
RUN pip install -r /requirements.txt

ADD . /code
WORKDIR /code

CMD python3 app.py

EXPOSE 5000
