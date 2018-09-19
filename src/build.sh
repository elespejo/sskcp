#!/bin/bash
arch="$1"
docker build -t elespejo/sskcp-$arch:test ./src
