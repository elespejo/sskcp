# Generate configuration

### Step 1: Download the configuration generator
You can download the generator package from web page or command line.

* From web:  
    Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project and download `sskcp-confgenerator-[VERSION].zip`.

* From command line:  
    ```bash
    wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/sskcp-confgenerator-[VERSION].zip
    ```
    e.g, download configuration generator of version 0.4.7
    ```bash
    wget https://github.com/elespejo/sskcp/releases/download/0.4.7/sskcp-confgenerator-0.4.7.zip
    ```

---

### Step 2: Unzip
```bash
unzip sskcp-confgenerator-[VERSION].zip
```
e.g,
```bash
unzip sskcp-confgenerator-0.4.7.zip
cd sskcp-confgenerator/
```

---

### Step 3: Check the help of confgenerator
```bash
python -m confgenerator.cli client -h
```
The explanation of needed keywords:
* [mode]: The mode of the instance. It can be `ss` or `sskcp`.
* [listenport]: The port that the instance listen.
* [vpsip]: The vps ip where the instance sent data. 
* [vpsport]: The vps port where the instance sent data.
* [key]: The password for client and server authorize each other.
* [log-dir]: The absolute path where the log directory created. The confgenerator will create a directory named `[listenport]-[vpsip]-[vpsport]` to store snmp log under this path.

---

### Step 4: Generate configuration 
There are several ways to use the confgenerator:
1. use conf-info file
2. use arguments
3. use both conf-info file and arguments

**Approach 1**: use conf-info file
* Modify the conf info.

    Here is the template of conf-info:
    ```yaml
    mode: [sskcp or ss]
    listenport: [port]
    vpsip: [ip]
    vpsport: [port]
    key: [key]
    log-dir: [path]
    ```
* Generate configuration.
    ```bash
    python -m confgenerator.cli client -f [conf-info] -d [dest]
    ```
    e.g: generate a configuration to `~/sskcp_conf` with conf-info in `~/info/sskcp-info.yml`.

    The conf-info file looks like below:
    ```yaml
    # ~/info/sskcp-info.yml
    mode: sskcp
    listenport: 2010
    vpsip: 1.1.1.1
    vpsport: 7010
    key: test
    log-dir: /home/user/log
    ```
    Generate configuration.
    ```bash
    python -m confgenerator.cli client -f ~/info/sskcp-info.yml -d ~/sskcp_conf
    ```

**Approach 2**: use arguments
* the arguments of the confgenerator.
    ```bash
    python -m confgenerator.cli client  --mode [mode] \
                                        --listenport [port] \
                                        --vpsip [ip] \
                                        --vpsport [port] \
                                        --key [key] \
                                        --log-dir [path] \
                                        -d [dest]
    ```
    e.g, generate sskcp configuration with mode `sskcp`, listenport `2010`, vpsip `1.1.1.1`,vpsport     `7010`, key `test`, log-dir `~/log` at `~/sskcp_conf`.
    ```bash
    python -m confgenerator.cli client  --mode sskcp \
                                        --listenport 2010 \
                                        --vpsip 1.1.1.1 \
                                        --vpsport 7010 \
                                        --key test \
                                        --log-dir ~/log \
                                        -d ~/sskcp_conf
    ```

**Approach 3**: use both conf-info file and arguments
* prepare the info.
    ```yaml
    # conf-info
    mode: [sskcp or ss]
    listenport: [port]
    vpsip: [ip]
    ```
    Others use arguments way.
* generate the configuration.
    ```bash
    python -m confgenerator.cli client  -f [conf-info] \
                                        --vpsport [port] \
                                        --key [key] \
                                        --log-dir [path] \
                                        -d [dest]
    ```
> Attention: if the keywords conflict between conf-info and arguments, use argument. 

### Step 5: Validation
After generation, a configuration named `[listenport]-[vpsip]-[vpsport]` is generated in `[dest]`.
```bash
tree [dest]
[dest]
└── [listenport]-[vpsip]-[vpsport]
    ├── conf
    │   ├── kcp.json # if mode is ss, this file is not exists.
    │   └── ss.json 
    └── config.env
```
Also, the log directory is created.
```bash
tree [log-dir]
[log-dir]
└── [listenport]-[vpsip]-[vpsport]
``` 
Log files will consistently generated after instance started.