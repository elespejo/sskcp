# Deployment

### Download the deployment package
    
You can download the deployment package from web page or command line.

* From web:  
Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project. Select the package according to the architecture of your machine and the structure you want to use.

* From command line:  
  ```bash
  $ wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/[STRUCTURE]-[ARCH]-[VERSION].zip
  ```
  > VERSION : the release tag  
  > STRUCTURE : the structure of ss and kcp  
  > ARCH : the architecture of your machine

  e.g : Deploy a sskcp client on a x86 machine with the release 0.3.7 by executing
  ```bash
  $ wget https://github.com/elespejo/sskcp/releases/download/0.3.7/sskcp-client-x86-0.3.7.zip
  ```

### Unzip

```bash
$ unzip [STRUCTURE]-[ARCH]-[VERSION].zip
$ cd [STRUCTURE]-[ARCH]
```

### Generate the docker compose file

Docker compose file is used for sskcp deployment. Its generation requires three parameters:
> [CONF_PATH] : The absolute path to configuration directory.  
> [LOG_PATH] : The absolute path for storage generated log. This path will be created if it is not existed.  
> [COMP_NAME] : The name of this compose file. This name is used to control the service. Must be **uniqueness**.

```bash
$ make config CONF=[CONF_PATH] LOG=[LOG_PATH] NAME=[COMP_NAME]
```

e.g : Generate a compose file named `4010.yml` with the configuration in `~/4010/conf` and log generated into `~/4010/log`.
```bash
$ cd ~/sskcp-client-x86/
$ make config CONF=~/4010/conf LOG=~/4010/log NAME=4010
```
Therefore a compose file named `4010.yml` is generated in `~/sskcp-client-x86/compose/`.
```yaml
# 4010.yml
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


```

### Start the service
Start the service with the name you specified in the config step above.
```bash 
$ make start NAME=[COMP_NAME]
```
e.g: start service `4010`
```bash
$ cd sskcp-client-x86/
$ make start NAME=4010
```
After starting the service successfully, you may see the output similar with the following: 
```
docker-compose -p 4010 -f ~/sskcp-client-x86/compose/4010.yml up -d
Creating 4010_sskcp-client_1 ... done
```

### Restart the service
```bash
$ make restart NAME=[COMP_NAME]
```

### Check status of the service
```bash
$ make status NAME=[COMP_NAME]
```

### Stop the service
```bash
$ make stop NAME=[COMP_NAME]
```

### List the services
```bash
$ make list
```

### Remove the compose file
```bash
$ make remove NAME=[COMP_NAME]
```
