FROM python:3.9-slim
LABEL maintainer="Charlie Lewis <clewis@iqt.org>"
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y git
COPY . /app
WORKDIR /app
RUN python3 -m pip install -U pip && \
    pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install .
ENTRYPOINT ["/usr/local/bin/zzztest"]
