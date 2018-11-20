# 0.4.7: update

### Update gitbook:
1. update dependency:
    1) add python and pyyaml
2. update deployment:
    1) add step on title
    2) replace 'service' to 'instance'
    3) replace 'structure' to 'mode'
    4) add imageAPI to directory and package
    5) add configuration explanation
3. update confgen:
    1) replace 'conf-generator' to 'confgenerator'
    2) add new confgenerator usage
    3) add validation
    4) add 'step' on title
4. update summary:
    1) add changelog document
5. add changelog

### Update imageAPI:
1. only show the last 100 line of log when checking status
2. new config structure
3. stay true when checking status

### Update makefile:
1. rename sskcp-server-x86 to sskcp-server-imageAPI-x86
2. rename sskcp-client-x86 to sskcp-client-imageAPI-x86
3. rename sskcp-client-armv6 to sskcp-client-imageAPI-armv6
4. rename confgenerator zip package name to sskcp-confgenerator-[version].zip

### update confgenerator
1. cover the situation : if configuration exist
2. add some hint when script run
3. remove key 'dest' in conf-info
4. fix typo of template log path
5. update all mode to 'sskcp'
6. rename directory confgenerator to sskcp-confgenerator

### update .gitignore:
1. ignore vscode setting

