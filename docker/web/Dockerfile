FROM python:3.10-alpine
WORKDIR /opt/app
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "app.py"]