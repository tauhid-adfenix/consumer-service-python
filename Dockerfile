FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1

RUN mkdir /consume
WORKDIR /consume
COPY . /consume/

RUN pip install --trusted-host pypi.python.org -r requirements.txt
# ENTRYPOINT /bin/bash
# CMD ["bash","start_server.sh" ]