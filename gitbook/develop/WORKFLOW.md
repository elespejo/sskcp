# Work flow
### Download the project
```bash
git clone https://github.com/elespejo/sskcp.git
cd sskcp/
```

### Build docker image 
After modifying the Dockerfile, use the command below to build the docker  image:
```bash
make mk-image ARCH=[arch]
```
The `arch` can be `x86` or `armv6`.
This action build a docker image named `elespejo/sskcp-[arch]:latest` by using the resource in directory `image`.

### Clean docker image 
```bash
make clean-image ARCH=[arch]
```

### Build sskcp client x86 image API
```bash
make mk-deployment-SKC_x86 VERSION=[version]
```

### Build sskcp server x86 image API
```bash
make mk-deployment-SKS_x86 VERSION=[version]
```

### Build sskcp client armv6 image API
```bash
make mk-deployment-SKC_armv6 VERSION=[version]
```

### Build configuration generator
```bash
make mk-deployment-CONFGEN VERSION=[version]
```

### Build all package
```bash
make mk-deployment VERSION=[version]
```

### Build gitbook
```bash
make mk-book
```