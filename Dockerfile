FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0

# set project environment variables
# grab these via the Python os.environ
# these are 100% optional here
# $PORT is set by Heroku
ENV PORT=8888

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-dependencies \
      gcc libc-dev linux-headers python3-dev postgresql-dev
    
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-dependencies

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
