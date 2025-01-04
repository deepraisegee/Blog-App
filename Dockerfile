# pull from base image
FROM python:3.10-slim

#set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set woking directory
WORKDIR /app

# copy dependencies
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy the rest app contents
COPY . .

EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]