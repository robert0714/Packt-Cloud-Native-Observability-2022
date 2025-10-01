# Chapter 3 examples

This folder contains examples for Chapter 3.

## Pre-requisites

- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Setup

```
git clone https://github.com/PacktPublishing/Cloud-Native-Observability
cd Cloud-Native-Observability/chapter3
dos2unix .\python\*
docker compose build
docker compose up
```

## Instrumentation libraries

Some of the available instrumentation libraries in OpenTelemetry:

| Language   | Libraries                                                         |
| ---------- | ----------------------------------------------------------------- |
| Go         | gin, gomemcache, gorilla/mux, net/http                            |
| Erlang     | Cowboy, Ecto, Phoenix                                             |
| Java       | Akka, gRPC, Hibernate, JDBC, Kafka, Spring, Tomcat                |
| Javascript | fetch, grpc-js, http, xml-http-request                            |
| .Net       | AspNetCore, GrpcNetClient, SqlClient, StackExchangeRedis          |
| Python     | Boto, Celery, Django, Flask, Redis, Requests, SQLAlchemy, urllib3 |
| Ruby       | ActiveJob, Faraday, Mongo, Rack, Rails                            |

---

_Cloud Native Observability_
* We will test the various tools to ensure each one is working as expected and is accessible from your browser. Let's start with Jaeger by accessing the following URL: http://localhost:16686. 