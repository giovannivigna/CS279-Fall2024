#!/bin/bash
IMAGE="sympthy"
PORT=40404
docker run -p ${PORT}:${PORT} ${IMAGE}
