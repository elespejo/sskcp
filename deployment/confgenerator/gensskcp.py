import json
import os

class SSKCP:
    def init_client(self):
        localss = self.args["ssport"]
        localkcp = localss+2000
        sspass = "ss_" + self.args["key"]
        kcppass = "kcp_" + self.args["key"]
        vpsip = self.args["vpsip"]
        remotekcp = self.args["kcpport"]
        self.clientss = {
            "server":"127.0.0.1",
            "server_port": localkcp,
            "local_address": "0.0.0.0",
            "local_port": localss,
            "password": sspass,
            "timeout":600,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        self.clientkcp = {
            "localaddr": "127.0.0.1:" + str(localkcp),
            "remoteaddr": "".join([vpsip, ":", str(remotekcp)]),
            "key": kcppass,
            "mode": "fast2",
            "snmplog":"/clientlog/kcp-20060102.log"
        }
        self.clientdir = self.args["dest"]+"/"+str(localss)+"-"+vpsip+"-"+str(remotekcp)

    def init_server(self):
        kcpport = self.args["kcpport"] 
        ssport = kcpport + 2000
        sspass = "ss_" + self.args["key"]
        kcppass = "kcp_" + self.args["key"]
        self.serverss = {
            "server":"0.0.0.0",
            "server_port": ssport,
            "password": sspass,
            "timeout":300,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        self.serverkcp = {
            "listen": "0.0.0.0:" + str(kcpport),
            "target": "127.0.0.1:" + str(ssport),
            "key": kcppass,
            "mode": "fast2",
            "snmplog": "/serverlog/kcp-20060102.log"
        }
        self.serverdir = self.args["dest"]+"/"+str(kcpport)

    def __init__(self, args):
        self.args = args

    def write_client(self, where):
        self.init_client()
        clientpath = where + "/" + self.clientdir
        if not os.path.exists(clientpath):
            os.makedirs(clientpath)
        with open(clientpath+"/ss.json", 'w') as outfile:
            json.dump(self.clientss, outfile, indent=4)
        with open(clientpath+"/kcp.json", 'w') as outfile:
            json.dump(self.clientkcp, outfile, indent=4)

    def write_server(self, where):
        self.init_server()
        serverpath = where + "/" + self.serverdir
        if not os.path.exists(serverpath):
            os.makedirs(serverpath)
        with open(serverpath+"/ss.json", 'w') as outfile:
            json.dump(self.serverss, outfile, indent=4)
        with open(serverpath+"/kcp.json", 'w') as outfile:
            json.dump(self.serverkcp, outfile, indent=4)

