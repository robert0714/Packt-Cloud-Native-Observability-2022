# Chapter 2 examples

This folder contains examples for Chapter 2.

## Prerequisites

- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Setup

```
docker compose up
```

---

_Cloud Native Observability_


* We will test the various tools to ensure each one is working as expected and is accessible from your browser. Let's start with Jaeger by accessing the following URL: http://localhost:16686. 
* The next backend this chapter will use for metrics is Prometheus; let's test the application by visiting http://localhost:9090.
* The last tool we need to ensure is working in our backend for logs is Loki. We will use Grafana as a dashboard to visualize the logs being emitted. Begin by visiting http://localhost:3000/explore to ensure Grafana is up.
* The next application we will check is the OpenTelemetry Collector, which acts as the routing layer for all the telemetry produced by the example application. The Collector exposes a health check endpoint discussed in [Chapter 8](../chapter08/README.md), OpenTelemetry Collector. For now, it's enough to know that accessing the endpoint will give us information about the health of the Collector, using the following curl command:
    ````bash
    $ curl localhost:13133

    {"status":"Server available","upSince":"2021-10-03T15:42:02.7345149Z","uptime":"9.3414709s"}
    ````
* The same command can be used to check the status of the inventory application by specifying port 5001:
    ```bash
    $ curl localhost:5001/healthcheck

    {

    "service": "inventory",

    "status": "ok"

    }
    ```
* The shopper application represents a client application and does not provide any endpoint to expose its health status. Instead, we can look at the logs emitted by the application to get a sense of whether it's doing the right thing or not. The following uses the docker logs command to look at the output from the application. Although it may vary slightly, the output should contain information about the shopper connecting to the grocery store:
    ```bash
    $ docker logs -f shopper

    DEBUG:urllib3.connectionpool:http://grocery-store:5000 "GET /products HTTP/1.1" 200 107

    INFO:shopper:message="add orange to cart
    ```
* The same docker logs command can be used on any of the other containers if you're interested in seeing more information about them. Once you're done with the chapter, you can clean up all the containers by running stop to terminate the running containers, and rm to delete the containers themselves:
    ```bash
    $ docker compose stop

    $ docker compose rm
    ```

All the examples in this chapter will expect that the Docker Compose environment is already up and running. When in doubt, come back to this technical requirement section to ensure your environment is still running as expected. Now, let's see what these OpenTelemetry signals are all about, starting with traces.    