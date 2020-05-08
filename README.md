![Docker](https://github.com/iminders/grpc-cpp-docker/workflows/Docker/badge.svg)
# Using Docker to build and deploy a C++ gRPC service

This sample demonstrates how to create a basic gRPC service in C++ and build it
it using GCC and CMake in a Docker container. It also shows how to create a
Docker image that contains only the service implementation, without the tools
needed to build it. It is based on the Dockerfile used to build the [official
gRPC CXX image](https://hub.docker.com/r/grpc/cxx/~/dockerfile/).

## run server
```
make serv
```

## run (python3)client
```
make client
```

## generate proto for python client
```
make proto
```

## Build image:
```
make build
```
