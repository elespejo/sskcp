# Generate configuration

### Download the configuration generator
You can download the generator package from web page or command line.

* From web:  
    Go to the [release page](https://github.com/elespejo/sskcp/releases) of this project and download `sskcp-conf-generator-[VERSION].zip`.

* From command line:  
    ```bash
    wget https://github.com/elespejo/sskcp/releases/download/[VERSION]/sskcp-conf-generator-[VERSION].zip
    ```

### Unzip
```bash
unzip sskcp-conf-generator-[VERSION].zip
```

### Generate configuration

```bash
cd confgenerator
python cli.py server --kcpport [KCP_PORT] --key [KEY]
```
in which,
* [KCP_PORT]: kcp listened port on vps 
* [KEY]: seed key for generate ss pass and kcp pass  

e.g, generate sskcp configuration
```bash
python cli.py server --kcpport 7010 --key music
``` 

You can validate the result by `tree ../conf`, with successful output similar with the following,
```
../conf
└── 7010
    ├── kcp.json
    └── ss.json
```
