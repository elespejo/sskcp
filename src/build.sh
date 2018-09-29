#!/bin/bash
cur_dir=`cd $(dirname $0);pwd`
docker build -f $cur_dir/Dockerfile-$1 -t sskcp-$1 ./src
