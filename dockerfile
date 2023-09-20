FROM python:3.9

ENV DJANGO_SETTINGS_MODULE=country_comp.settings
ENV DJANGO_SECRET_KEY=django-insecure-4+d^2iqna=*bfsgax1kbbb)8o-(qb3c512fko#)qj*&g1=a#6t
ENV DJANGO_DEBUG=False

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000