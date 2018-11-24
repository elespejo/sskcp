# Deployment

### Step 1: Download the deployment package
    
You can download the deployment package from web page or command line.

* From web:  
Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project. Select the package according to the architecture of your machine and the mode you want to use.

* From command line:  
```bash
wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/[MODE]-server-imageAPI-x86-[VERSION].zip
```
  * VERSION : the release tag.
  * MODE : ss or sskcp.
  * ARCH : the architecture of your machine. It can be x86 and armv6.

  e.g : Deploy a sskcp server on a x86 machine with the release 0.4.8 by executing
  ```bash
  wget https://github.com/elespejo/sskcp/releases/download/0.4.8/sskcp-server-imageAPI-x86-0.4.8.zip
  ```

### Step 2: Unzip

```bash
unzip [MODE]-server-imageAPI-x86-[VERSION].zip
cd [MODE]-server-imageAPI-x86/
```

### Step 3: Prepare the configuration

The configuration for server imageAPI looks like following:
```
configuration
├── conf
│   ├── kcp.json # if mode is ss, this file is not exists.
│   └── ss.json 
└── config.env
```
The explanation of each file:
* [ss.json]: the configuration of ss.
* [kcp.json]: the configuration of kcp.
* [config.env]: the environment file which content is the variables for the instance.

The template of environment file looks like following:
```env
LOG_DIR=[path]
MODE=[ss or sskcp]
```
> The configuration can use the [confgenerator](GENCONF_SERVER.md) to generate. 

### Step 4: Config a instance
```bash
cd [mode]-server-imageAPI-x86/
make config CONFIG=[configuration path] NAME=[NAME]
```
The explanation of those arguments:
* [CONFIG] : The absolute path to configuration directory.  
* [NAME] : The instance name. This name is used to control the instance. Must be **uniqueness**.

e.g : Generate a compose file named `7010.yml` with the configuration in `~/conf/2010-123.45.67.8-7010/`.
```bash
cd ~/sskcp-server-imageAPI-x86/
make config CONF=~/conf/2010-123.45.67.8-7010 NAME=7010
```
Therefore a compose file named `7010.yml` is generated in `~/sskcp-server-imageAPI-x86/compose/`.
```yaml
# 7010.yml
services:
  sskcp-server:
    command: supervisord -c /service.conf.d/sskcp-redir-x86.conf
    image: elespejo/sskcp-x86:0.4.8
    network_mode: host
    restart: always
    volumes:
    - source: ~/conf/2010-123.45.67.8-7010
      target: /serverconf
      type: bind
    - source: ~/log/2010-123.45.67.8-7010
      target: /serverlog
      type: bind
version: '3.2'
```
For testing configed instance , use another makefile target 'test_config':
```bash
make test_config NAME=[NAME]
``` 


### Step 5: Start the instance
Start the instance with the name you specified in the config step above.
```bash 
make start NAME=[NAME]
```
e.g: start instance `7010`
```bash
cd sskcp-server-imageAPI-x86/
make start NAME=7010
```
After starting the instance successfully, you may see the output similar with the following: 
```
docker-compose -p 7010 -f ~/sskcp-server-imageAPI-x86/compose/7010.yml up -d
Creating 7010_sskcp-server_1 ... done
```

### Step 6: Restart the instance
```bash
make restart NAME=[NAME]
```
e.g
```bash
make restart NAME=7010
```
After restarting the instance successfully, you may see the output similar with the following:
```
docker-compose -p 7010 -f ~/sskcp-server-imageAPI-x86/compose/7010.yml up -d --force-recreate
Recreating 7010_sskcp-server_1 ... done
```

### Step 7: Check status of the instance
```bash
make status NAME=[NAME]
```
e.g,
```bash
make stop NAME=7010
```
You may see the output similar with the following:
```
docker-compose -p 7010 -f ~/sskcp-server-imageAPI-x86/compose/7010.yml ps
       Name                      Command               State   Ports
--------------------------------------------------------------------
7010_sskcp-server_1   supervisord -c /service.co ...   Up
docker-compose -p 7010 -f ~/sskcp-server-imageAPI-x86/compose/7010.yml logs
Attaching to 7010_sskcp-server_1
sskcp-server_1  | 2018-10-12 04:02:09,572 CRIT Supervisor is running as root...
sskcp-server_1  | 2018-10-12 04:02:09,572 CRIT Supervisor is running as root...
sskcp-server_1  | 2018-10-12 04:02:09,574 INFO supervisord started with pid 1
sskcp-server_1  | 2018-10-12 04:02:09,574 INFO supervisord started with pid 1
...
```

### Step 8: Stop the instance
```bash
make stop NAME=[NAME]
```
e.g,
```bash
make stop NAME=7010
```
After stoping the instance successfully, you may see the output similar with the following:
```
docker-compose -p 7010 -f ~/sskcp-server-imageAPI-x86/compose/7010.yml down
Stopping 7010_sskcp-server_1 ... done
Removing 7010_sskcp-server_1 ... done
```

### Step 9: List the instances
```bash
make list
```
You may see the output similar with the following:
```
for compose in `ls ~/sskcp-server-imageAPI-x86/compose`;do name=`echo $compose|awk -F "." '{print $1}'`;echo $name;docker-compose -p $name -f ~/sskcp-server-imageAPI-x86/compose/$compose ps;done
7010
       Name                      Command               State   Ports
--------------------------------------------------------------------
7010_sskcp-server_1   supervisord -c /service.co ...   Up
...
```

### Step 10: Remove the compose file
```bash
make remove NAME=[NAME]
```
e.g,
```bash
make remove NAME=7010
```
You may see the output similar with the following:
```
rm ~/sskcp-server-imageAPI-x86/compose/7010.yml
```
Check whether the remove step successfully:
```bash
ls compose | grep 7010
```

