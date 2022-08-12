FROM python:3.9-alpine

WORKDIR /code

COPY user_greeting_service/ /code/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w 2", "-b 0.0.0.0:9090", "wsgi:app"]