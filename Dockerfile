FROM python:3.10-alpine

WORKDIR /backend

RUN pip install --upgrade pip

COPY . /backend

RUN pip install -r requirements.txt

ENV PYTHONPATH=/backend

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

# Build command: docker build --tag 'image_name' .
# Docker compose: docker-compose up -d ИЛИ docker compose up -d
