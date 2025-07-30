FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]