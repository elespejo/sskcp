#! /bin/bash
config() {
  for i in {3..6}
  do
    make config CONF=/home/develop/elespejo/sskcp/deployment/conf/40${i}0/client LOG=/home/develop/elespejo/sskcp/deployment/log/40${i}0 NAME=40${i}0
  done
}

start() {
  for i in {3..6}
  do
    make start NAME=40${i}0
  done
}

#config
#start

stop() {
  for i in {3..6}
  do
    make stop NAME=40${i}0
  done
}


stop
