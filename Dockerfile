FROM ubuntu:16.04
Maintainer Eric Tam

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["client.py"]
