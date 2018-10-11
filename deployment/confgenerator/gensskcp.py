import json
import os

class SSKCP:
    def init_client(self):
        self.clientss = {
            "server":"127.0.0.1",
            "server_port": self.args["kcpport"],
            "local_address": "0.0.0.0",
            "local_port": self.args["ssport"],
            "password": self.sspass,
            "timeout":600,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        self.clientkcp = {
            "localaddr": "127.0.0.1:" + str(self.args["kcpport"]),
            "remoteaddr": "".join([self.args["vpsip"], ":", str(self.args["kcpport"])]),
            "key": self.kcppass,
            "mode": "fast2",
            "snmplog":"/clientlog/kcp-20060102.log"
        }
        self.clientdir = self.args["dest"]+"/client"

    def init_server(self):
        self.serverss = {
            "server":"0.0.0.0",
            "server_port": self.args["ssport"],
            "password": self.sspass,
            "timeout":300,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        self.serverkcp = {
            "listen": "0.0.0.0:" + str(self.args["kcpport"]),
            "target": "127.0.0.1:" + str(self.args["ssport"]),
            "key": self.kcppass,
            "mode": "fast2",
            "snmplog": "/serverlog/kcp-20060102.log"
        }
        self.serverdir = self.args["dest"]+"/server"

    def __init__(self, args):
        self.args = args
        self.sspass = "testss"
        self.kcppass = "testkcp"
        self.init_client()
        self.init_server()

    def write_client(self, where):
        clientpath = where + "/" + self.clientdir
        if not os.path.exists(clientpath):
            os.makedirs(clientpath)
        with open(clientpath+"/ss.json", 'w') as outfile:
            json.dump(self.clientss, outfile, indent=4)
        with open(clientpath+"/kcp.json", 'w') as outfile:
            json.dump(self.clientkcp, outfile, indent=4)

    def write_server(self, where):
        serverpath = where + "/" + self.serverdir
        if not os.path.exists(serverpath):
            os.makedirs(serverpath)
        with open(serverpath+"/ss.json", 'w') as outfile:
            json.dump(self.serverss, outfile, indent=4)
        with open(serverpath+"/kcp.json", 'w') as outfile:
            json.dump(self.serverkcp, outfile, indent=4)

    def start(self, where):
        self.write_client(where)
        self.write_server(where)

