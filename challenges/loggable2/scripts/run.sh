#!/bin/bash
IMAGE="loggable2"
PORT=4243
docker run -p ${PORT}:${PORT} ${IMAGE}
