FROM python:3.9-slim-buster

RUN pip install --upgrade pip

ENV TZ=America/Sao_Paulo

RUN apt-get update \
    && apt-get -y install libpq-dev gcc cron vim tzdata \
    && pip install psycopg2

# sync timezone
RUN echo $TZ > /etc/timezone \
    && ln -fsn /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app/web
WORKDIR /home/app/web

COPY . .

COPY ./docker/django_nginx/entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]