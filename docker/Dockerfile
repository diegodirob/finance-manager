FROM python:3.11.3-slim-bullseye

# Enable real time logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

# Add packages needed by crontab
RUN apt-get update \
  && apt-get install -y libpq-dev gcc \
  && apt-get -y install cron \
  && apt-get clean \
  && pip install --upgrade pip

WORKDIR /code

# By copying over requirements first, we make sure that Docker will cache our installed requirements rather than reinstall them on every build
COPY ./django/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /code

WORKDIR /code/finance-manager