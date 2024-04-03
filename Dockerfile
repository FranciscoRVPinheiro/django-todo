FROM python:3.10.0-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONWARNINGS ignore
RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

# RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
