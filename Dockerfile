FROM python:3.9-alpine

WORKDIR /code

COPY user_greeting_service/ /code/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "waitress_server.py" ]