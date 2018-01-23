FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install --trusted-host pypi.python.org -r requirements.txt