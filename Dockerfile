FROM python:3.10.5-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

LABEL org.opencontainers.image.authors="me@azureagst.dev"
LABEL org.opencontainers.image.source="https://github.com/Azure-Agst/rpilocator-rss-feed"

CMD [ "python3", "rpilocator-rss.py" ]