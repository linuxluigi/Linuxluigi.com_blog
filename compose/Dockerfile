FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # git
  && apt-get install -y git \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# download all plugins
RUN git clone https://github.com/getpelican/pelican-plugins /plugins  && \
  cd /plugins && \
  git fetch --all && \
  git reset --hard ce698144d831e5b27cba6283b4db3238dfbd2c10

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

EXPOSE 8000