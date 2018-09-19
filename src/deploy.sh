#!/bin/bash

USER="$1"
PASS="$2"
TAG="$3"

ORG="elespejo"
REPO="sskcp-x86"


docker tag $REPO $ORG/$REPO:$TAG 
docker login -u "$USER" -p "$PASS"
docker push $ORG/$REPO:$TAG