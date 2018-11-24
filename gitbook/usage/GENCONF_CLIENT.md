# Generate client configuration

### Step 1: Download the configuration generator
You can download the generator package from web page or command line.

* From web:  
    Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project and download `sskcp-confgenerator-[VERSION].zip`.

* From command line:  
```bash
wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/sskcp-confgenerator-[VERSION].zip
```
e.g, download configuration generator of version 0.4.8
```bash
wget https://github.com/elespejo/sskcp/releases/download/0.4.8/sskcp-confgenerator-0.4.8.zip
```

### Step 2: Unzip
```bash
unzip sskcp-confgenerator-[VERSION].zip
cd sskcp-confgenerator/
```
e.g:
```bash
unzip sskcp-confgenerator-0.4.8.zip
cd sskcp-confgenerator/
```

### Step 3: Modify the conf-info

Here is the template conf-info for sskcp client:
```yaml
client:
  - mode: [ss or sskcp]
    listenport: [port]
    vpsip: [ip]
    vpsport: [port]
    key: [key]
    log-dir: [path]
```
The explanation of needed keywords:
* [mode]: The mode of the instance. It can be `ss` or `sskcp`.
* [listenport]: The port that the instance listens.
* [vpsip]: The vps ip where the instance sent data. 
* [vpsport]: The vps port where the instance sent data.
* [key]: The password for client and server authorize each other.
* [log-dir]: The absolute path where the log directory created. The confgenerator will create a directory named `[listenport]-[vpsip]-[vpsport]` to store snmp log under this path.

### Step 4: Use confgenerator

```bash
python -m confgenerator.cli client -f [conf-info] -d [dest]
```
The explanation of arguments:
* [conf-info]: the absolute path of conf-info file.
* [dest]: the absolute path for configuration generation.

### Step 4: validation

After generation, A configuration directory named `[listenport]-[vpsip]-[vpsport]` is generated in [dest].
```bash
tree [dest]/
[dest]
└── [listenport]-[vpsip]-[vpsport]
    ├── conf
    │   ├── kcp.json # if mode is ss, this file is not exists.
    │   └── ss.json 
    └── config.env
```
Also, A log directory named `[listenport]-[vpsip]-[vpsport]` is created in [log-dir].
```bash
tree [log-dir]
[log-dir]
└── [listenport]-[vpsip]-[vpsport]
``` 
Log files will consistently generated after instance started.