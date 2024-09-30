#!/bin/bash
IMAGE="babyshot"
PORT=7631
docker run -p ${PORT}:${PORT} ${IMAGE}
