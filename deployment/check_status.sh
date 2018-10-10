CUR_DIR=`cd $(dirname $0);pwd`

docker-compose -f $CUR_DIR/docker-compose-client.yml ps
docker-compose -f $CUR_DIR/docker-compose-client.yml logs

sudo netstat -tunpl | grep docker