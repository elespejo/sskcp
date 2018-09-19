#!/bin/bash
cur_dir=`cd $(dirname $0);pwd`
docker build -f $cur_dir/Dockerfile -t sskcp-x86 ./src
