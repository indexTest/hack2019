FROM python:3

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . . 

RUN pip install --no-cache-dir -r /usr/src/app/requirement.txt &\
    chmod 777 ./start.sh

RUN pip install Flask

ENTRYPOINT ./start.sh
