FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
WORKDIR /app
ADD ./urlshortener /app
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    pip install gunicorn
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn urlshortener.wsgi -b 0.0.0.0:8000
