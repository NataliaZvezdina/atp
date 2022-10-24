FROM python:3.10-alpine
WORKDIR /opt/app
ADD ./requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "app.py"]