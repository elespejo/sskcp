#! /bin/bash
config() {
  for i in {3..6}
  do
    make config CONF=~/elespejo/sskcp/deployment/conf/40${i}0/client LOG=~/elespejo/sskcp/deployment/log/40${i}0 NAME=40${i}0
  done
}

start() {
  for i in {3..6}
  do
    make start NAME=40${i}0
  done
}


stop() {
  for i in {3..6}
  do
    make stop NAME=40${i}0
  done
}

status() {
  for i in {3..6}
  do
    make status NAME=40${i}0
  done
}

case "$1" in 
  config)
    config
    ;;

  start)
    start
    ;;
  
  stop)
    stop
    ;;

  status)
    status
    ;;

  *)
    echo error
esac
