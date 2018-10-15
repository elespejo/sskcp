# Generate configuration

### Download the configuration generator
You can download the generator package from web page or command line.

* From web:  
    Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project and download `sskcp-conf-generator-[VERSION].zip`.

* From command line:  
    ```bash
    wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/sskcp-conf-generator-[VERSION].zip
    ```
    e.g, download configuration generator of version 0.3.7
    ```bash
    wget https://github.com/elespejo/sskcp/releases/download/0.3.7/sskcp-conf-generator-0.3.7.zip
    ```

### Unzip
```bash
unzip sskcp-conf-generator-[VERSION].zip
```
e.g,
```bash
unzip sskcp-conf-generator-0.3.7.zip
```

### Generate configuration

```bash
cd confgenerator
python cli.py client --ssport [SS_PORT] --vpsip [VPS_IP] --kcpport [KCP_PORT] --key [KEY]
```
in which,
* [SS_PORT]: shadowsocks listened port 
* [VPS_IP]: vps ip address  
* [KCP_PORT]: remote kcp port on vps 
* [KEY]: seed key for generate ss pass and kcp pass  

e.g, generate sskcp configuration
```bash
python cli.py client --ssport 2010 --vpsip 123.45.67.8 --kcpport 7010 --key music
``` 

You can validate the result by `tree ../conf`, with successful output similar with the following,
```
../conf
└── 2010-123.45.67.8-7010
    ├── kcp.json
    └── ss.json

```
