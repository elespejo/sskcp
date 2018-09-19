<p align="center">
  <img width="250" src="https://www.lucidchart.com/publicSegments/view/acf1287b-07f1-4ac9-8efe-a82eec2a9e73/image.png">
</p>

<h1 align="center"> sskcp </h1>
<p align="center">
  <b >x86 and armv6 image of ss and kcp</b>
</p>
<br>

[![GitHub release](https://img.shields.io/github/release/elespejo/sskcp.svg)](https://github.com/elespejo/sskcp/releases)
![GitHub](https://img.shields.io/github/license/elespejo/sskcp.svg)  
Travis :  
![Travis (.org) branch](https://img.shields.io/travis/elespejo/sskcp/master.svg)  
Docker :  
[![Docker Build Status](https://img.shields.io/docker/build/elespejo/sskcp-x86.svg)](https://hub.docker.com/r/elespejo/sskcp-x86/builds/)
[![Docker Pulls](https://img.shields.io/docker/pulls/elespejo/sskcp-x86.svg)](https://hub.docker.com/r/elespejo/sskcp-x86/tags/)

# Dependence

1. Install docker 18.06 : [reference](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

2. Install `docker-compose` command :  
For x86 : docker-compose 1.22.0 [reference](https://docs.docker.com/compose/install/)  
For armv6 : `pip install docker-compose`

# Deployment

  - Pull the code from github.
    ```bash
    $ git clone https://github.com/elespejo/sskcp.git
    $ cd sskcp/test
    ```

  - Start sskcp client or server.  
    Client:
    ```bash
    $ ./client-ctl start
    ```
    Server:
    ```bash
    $ ./server-ctl start
    ```

  - Check status of sskcp client or server.  
    Client:
    ```bash
    $ ./client-ctl status
    ```
    Server:
    ```bash
    $ ./server-ctl status
    ```

  - Stop the sskcp client or server.  
    Client:
    ```bash
    $ ./client-ctl stop
    ```
    Server:
    ```bash
    $ ./server-ctl stop
    ```

### Build

  ```bash
  $ cd src/
  $ ./build.sh
  ```

### Built With
  - travis


# Logistics

### Contributing

Please read [CONTRIBUTING.md](https://github.com/elespejo/sskcp/blob/master/docs/CONTRIBUTING.md) for contributing.
For details on our [code of conduct](https://github.com/elespejo/sskcp/blob/master/docs/CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository

### Authors
* **AUTHOR** - *Initial work* - [mateomartin1998](https://github.com/mateomartin1998)
* **AUTHOR** - *improvement* - [Valerio-Perez](https://github.com/valerio-Perez)

See also the list of [contributors](https://github.com/elespejo/sskcp/graphs/contributors) who participated in this project.

### Acknowledgments

See [Acknowledgments](https://github.com/elespejo/sskcp/blob/master/docs/ACKNOWLEDGMENTS.md)


### License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/elespejo/sskcp/blob/master/LICENSE.md) file for details

