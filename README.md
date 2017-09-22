# Simple Flask Web Server

A simple flask web server that only has `/` as an endpoint. If Accept header exists, return `<p>Hello, World</p>`. If Accept header is `application/json`, return `{"message": "Good morning"}`

## Requirements
* Docker

## Installation
```shell
docker build -t server .
docker run -d -p 5000:5000 server
```

## Testing Requests
```shell
# No Accept Header
curl -XGET http://0.0.0.0:5000
curl -XPOST http://0.0.0.0:5000

# Accept Header is application/json
curl -XGET -H 'Accept:application/json' http://0.0.0.0:5000
curl -XPOST-H 'Accept:application/json' http://0.0.0.0:5000
```