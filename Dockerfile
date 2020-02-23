# Docker image based on Alpine Linux with python3.6
FROM python:3.6-alpine3.10

WORKDIR /usr/src/app

# Bundle app source
COPY . .

# Installing GCC for C-based dependencies
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev autoconf automake libtool make

RUN pip install -r requirements.txt

# Removing build dependencies in order trim down the image size 
RUN apk del .build-deps

EXPOSE 8080

CMD ["python" ,"manage.py", "runserver"]
