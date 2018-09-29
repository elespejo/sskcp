#!/bin/bash

USER=$1
PASS=$2
TAG=$3
ARCH=$4

ORG=elespejo

REPO=sskcp

docker tag $REPO-$ARCH $ORG/$REPO-$ARCH:$TAG 
docker login -u $USER -p $PASS
docker push $ORG/$REPO-$ARCH:$TAG
