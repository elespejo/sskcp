#!/bin/bash

USER="$1"
PASS="$2"
TAG="$3"
ARCH="$4"

ORG="elespejo"
REPO="sskcp-${ARCH}"


docker tag $REPO $ORG/$REPO:$TAG 
docker login -u "$USER" -p "$PASS"
docker push $ORG/$REPO:$TAG
