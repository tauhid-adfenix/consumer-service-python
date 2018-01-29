# consumer-service-python
A Django Rest API project that consume messages from RabbitMQ Queue and store it into Postgres DB. 

## Docker-compose
First need to clone the docker compose project from [Github](https://github.com/tauhid-adfenix/docker-compose.git). After that run the `setup.sh` or `setup.bat` for first time. For further instruction read the README.

## REST API
Hit the API to get all consumer-service data
```shell
curl localhost:8000/data
```