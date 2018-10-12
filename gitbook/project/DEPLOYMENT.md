# Deployment

### Download the deployment package
    
You can download the deployment package from web page or command line.

From web:  
Go to the release page of this project ([here](https://github.com/elespejo/sskcp/releases)). Find the latest release and select the package according to the architecture of your machine and the structure you want to use.

From command line:  
```bash
$ wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/[STRUCTURE]-[ARCH]-[VERSION].zip
```
> VERSION : the release tag  
> STRUCTURE : the structure of ss and kcp  
> ARCH : the architecture of your machine

For example:  
You want to deploy a sskcp client on your x86 machine and use the release 0.3.7. So run the command below:
```bash
$ wget https://github.com/elespejo/sskcp/releases/download/0.3.7/sskcp-client-x86-0.3.7.zip
```

### Unzip

```bash
$ unzip [STRUCTURE]-[ARCH]-[VERSION].zip
$ cd [STRUCTURE]-[ARCH]
```

### Generate the docker compose file

The deployment use docker compose file to control the image. The generation of docker compose file need specify the configuration path, log path and the name of this compose file. After this step, a compose file is generated in `unziped_package_path/compose/`.
```bash
$ cd [STRUCTURE]-[ARCH]
$ make config CONF=[CONF_PATH] LOG=[LOG_PATH] NAME=[COMP_NAME]
```
> [CONF_PATH] : The absolute path to configuration directory.  
> [LOG_PATH] : The absolute path for storage generated log. This path will be created if it is not existed.  
> [COMP_NAME] : The name of this compose file. This name is used to control the service. Must be **uniqueness**.

For example:  
After downloading and unziping the package `sskcp-client-x86-0.3.7.zip`, you want to generate a compose file named `4010` with the configuration in `~/4010/conf` and log generated to `~/4010/log`.
```bash
$ cd ~/sskcp-client-x86/
$ make config CONF=~/4010/conf LOG=~/4010/log NAME=4010

cp ~/sskcp-client-x86/temp.env ~/sskcp-client-x86/.env
echo "CONF_DIR=~/4010/conf" >> ~/sskcp-client-x86/.env
echo "LOG_DIR=~/4010/log" >> ~/sskcp-client-x86/.env
cat ~/sskcp-client-x86/.env
ORG=elespejo
REPO=sskcp
ARCH=x86
VERSION=0.3.7
CONF_DIR=~/4010/conf
LOG_DIR=~/4010/log
mkdir -p ~/sskcp-client-x86/compose
docker-compose -p 4010 -f ~/sskcp-client-x86/docker-compose.yml config | tee ~/sskcp-client-x86/compose/4010.yml
services:
  sskcp-client:
    command: supervisord -c /service.conf.d/sskcp-redir-x86.conf
    image: elespejo/sskcp-x86:develop
    network_mode: host
    restart: always
    volumes:
    - source: ~/4010/conf
      target: /clientconf
      type: bind
    - source: ~/4010/log
      target: /clientlog
      type: bind
version: '3.2'

rm ~/sskcp-client-x86/.env
mkdir -p ~/4010/log
```
Then, you can see a compose file named `4010.yml` in `~/sskcp-client-x86/compose`.

### Start the service
Start the service with the name you specified in config step.
```bash 
$ cd path/to/package/
$ make start NAME=[COMP_NAME]
```
For example:  
After config a compose file `4010`, you want to start the service with this compose file.
```bash
$ cd sskcp-client-x86/
$ make start NAME=4010

docker-compose -p 4010 -f ~/sskcp-client-x86/compose/4010.yml up -d
Creating 4010_sskcp-client_1 ... done
```

### Restart the service
Restart the service with the name you specified in config step.
```bash
$ cd path/to/package/
$ make restart NAME=[COMP_NAME]
```

### Check status of the service
```bash
$ cd path/to/package/
$ make status NAME=[COMP_NAME]
```

### Stop the service
```bash
$ cd path/to/package/
$ make stop NAME=[COMP_NAME]
```

### List the services
List all the services start or not.
```bash
$ cd path/to/package/
$ make list
```

### Remove the compose file
Remove the configured compose file.
```bash
$ cd path/to/package/
$ make remove NAME=[COMP_NAME]
```
