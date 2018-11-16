"""
"""

import os
import yaml
import json
import shutil

class Conf_Generator():
    """Basic generator."""
    
    def __init__(self, infos_args, val_obj):
        """Initial arguments for generator.
        Arguments:
            infos_args: A dict for generating infos_list.
            val_obj: A object for validating the info.
        """
        self.infos_args = infos_args
        self.val = val_obj

    def _gen_info(self, infos_args):
        """Generate infos_list.
        Argument:
            infos_args: the dict of information that from cli parser.

        Return:
            infos_list: The list of infos.
        """
        pass

    def _validate(self, info):
        """Validate the info.
        Argument:
            self.val: the validator object.
            info: A dict of sskcp client or server information.
                {
	            	'mode': [ss/sskcp],
	            	'log-dir': [/path/to/log],
	            	'listenport': [port],
                    'key': [key],
	            	'dest': [/path/to/config],
                    ...
	            }

        Return:
            result: (bool, msg)
        """
        validator = self.val(info)
        return validator.validate()

    def _gen_config(self, mode, log, dest):
        """Generate configuration structure and config.env.
        Arguments:
            mode: the mode of sskcp. It is ss or sskcp.
            log: the absolute path of log.
            dest: the absolute path of configuration.

        Return:
            1. A configuration directory for sskcp is created in [dest].
            2. A log directory for sskcp is created in [log] 
            3. A config.env is generated in [dest]/.
            
        configuration structure:
            info['dest']/
            |_config.env
            |_conf/
        
        Content of config.env:
            LOG_DIR=info['log-dir']
            MODE=info['mode'] 
        """
        if os.path.exists(dest):
            print("The configuration exists.")
            yn = input("Do you want to overwrite it?[y/n]")
            if yn == 'y':
                print("Remove origin configuration: "+dest)
                shutil.rmtree(dest)
            elif yn == 'n':
                raise SystemExit("Exit.")
            else:
                raise SystemExit("Worry keyword: "+yn+"\nExit.")

        print("\nGenerate configuration structure.")
        print(" - create directory: "+dest)
        os.makedirs(dest+"/conf")
        print(" - create log directory: "+log)
        os.makedirs(log, exist_ok=True)
        print(" - create config.env.")
        with open(dest+"/config.env", "w") as f:
            f.write("LOG_DIR="+log+'\nMODE='+mode)
        
    def _gen_ss_setting(self, info):
        """Generate setting for mode ss.
        Arguments:
            info: the dict of ss info.

        Return:
            ss_setting: the dict of ss setting for ss.json generation.
        """
        pass

    def _gen_sskcp_setting(self, info):
        """Generate setting for mode sskcp.
        Arguments:
            info: the dict of sskcp info.

        Return:
            ss_setting: the dict of ss setting for ss.json generation.
            kcp_setting: the dict of ss setting for kcp.json generation.
        """
        pass

    def _gen_ss_conf(self, ss_setting):
        """Generate ss configuration according to [ss_setting].
        Arguments:
            ss_setting: A dict of information that ss configuration needed.

        Return:
            ss_conf: A dict that can be dumped to json file that used by ss.
        """
        pass

    def _gen_kcp_conf(self, kcp_setting):
        """Generate kcp according to [kcp_setting].
        Arguments:
            kcp_setting: A dict of information that kcp configuration needed. 

        Return:
            kcp_conf: A dict that can be dumped to json file that used by kcp.
        """
        pass

    def write_json(self, conf, dest, name):
        """Write [conf] to a json file in [dest].
        Arguments:
            conf: A dict.
            dest: An absolute path where json file generated.
            name: The name of the json file.

        Return:
            A json file named [name] with content [conf] in [dest].
        """
        print("\nGenerate json file: "+dest+'/'+name+".json")
        with open(dest+'/'+name+".json", 'w') as outfile:
            try:
                json.dump(conf, outfile, indent=4)
            except json.JSONDecodeError as exc:
                print(exc)
            except KeyboardInterrupt:
                print('You cancelled the operation.')

    def load_yaml(self, yaml_file):
        """Load yaml to a dict.
        Arguments:
            yaml_file: the absolute path of a yaml file.

        Return:
            yaml_dict: the dict of the yaml file. 
        """
        print("\nLoad yaml file: "+yaml_file)
        with open(yaml_file, 'r') as file:
            try:
                return yaml.load(file)
            except yaml.YAMLError as exc:
                print(exc)
    
    def generate(self):
        """Steps for generating sskcp configuration.
        Steps:
            1. generate list of infos
            2. for info in infos_list:
                2.1 validate info
                2.2 generate structure and config.env
                2.3 generate setting
                2.4 generate conf
                2.5 write file
        """
        # generate list of infos
        infos_list = self._gen_info(self.infos_args)
        for info in infos_list:
            # validate info(TODO) 
            # validation = self._validate(info)
            
            # generate structure and config.env
            log = info.pop('log-dir')
            mode = info.pop('mode')
            dest = info.pop('dest')
            self._gen_config(mode, log, dest)

            # generate setting and conf
            if mode == 'sskcp':
                ss_setting, kcp_setting = self._gen_sskcp_setting(info)
                kcp_conf = self._gen_kcp_conf(kcp_setting)
                self.write_json(kcp_conf, dest+"/conf", "kcp")

            elif mode == 'ss':
                ss_setting = self._gen_ss_setting(info)

            ss_conf = self._gen_ss_conf(ss_setting)
            self.write_json(ss_conf, dest+"/conf", "ss")


class Client_Conf_Generator(Conf_Generator):
    """sskcp client configuration generator."""
    
    def _gen_info(self, infos_args):
        """Generate info list.
        Arguments:
            infos_args = 
                {
                    'info-file': [/path/to/conf-info],
                    'mode': [ss/sskcp],
                    'log-dir': [/path/to/log],
                    'listenport': [port],
                    'vpsip': [ip],
                    'vpsport': [port]
                    'key': [key],
                    'dest': [/path/to/config]
                }

        Return:
            infos_list: The list of infos.
                [
	                {
		                'mode': [ss/sskcp],
		                'log-dir': [/path/to/log],
		                'listenport': [port],
                        'vpsip': [ip],
                        'vpsport': [port]
                        'key': [key],
		                'dest': [/path/to/config],
	                },
	                ...
                ]
        """
        # load info file to list
        info_file = infos_args.pop('info-file')
        infos_list = self.load_yaml(info_file)['client']
        
        # modify the value of [key] in info if value of [key] specified in infos_args[]
        for info in infos_list:
            for k, v in infos_args.items():
                if not v == None:
                    info[k] = v
            # modify the value of dest to info['dest']/info['listenport']-info['vpsip']-info['vpsport']
            info['dest'] = info['dest']+'/'+str(info['listenport'])+'-'+info['vpsip']+'-'+str(info['vpsport'])
            # modify the value of log-dir to info['log-dir']/info['listenport']-info['vpsip']-info['vpsport']
            info['log-dir'] = info['log-dir']+'/'+str(info['listenport'])+'-'+info['vpsip']+'-'+str(info['vpsport'])

        return infos_list

    def _gen_ss_setting(self, info):
        """Generate ss client setting for mode ss.
        Arguments:
            info: A dict of sskcp client information.
                {
	            	'listenport': [port],
                    'vpsip': [ip],
                    'vpsport': [port]
                    'key': [key],
	            }

        Return:
            ss_setting: A setting dict for ss.json generation.
                {
                	"listenport": info['listenport']
                	"server": info['vpsip']
                	"serverport": info['vpsport']
                	"sskey": "ss_"+info['key']
                }
        """
        ss_setting = {
            "listenport": info['listenport'],
            "server": info['vpsip'],
            "serverport": info['vpsport'],
            "sskey": "ss_"+info['key']
        }
        return ss_setting

    def _gen_sskcp_setting(self, info):
        """Generate ss and kcp client setting for mode sskcp.
        Arguments:
            info: A dict of sskcp client information.
                {
	            	'mode': [ss/sskcp],
	            	'log-dir': [/path/to/log],
	            	'listenport': [port],
                    'vpsip': [ip],
                    'vpsport': [port]
                    'key': [key],
	            	'dest': [/path/to/config],
	            }

        Return:
            ss_setting: A setting dict for ss.json generation.
                {
                	"ssport": info['listenport']
                	"server": 127.0.0.1
                	"serverport": info['vpsport']+2000
                	"sskey": "ss_"+info['key']
                }

            kcp_setting: A setting dict for kcp.json generation.
                {
                	"listenport": info['listenport']+2000 
                	"server": info['vpsip']
                	"serverport": info['vpsport']
                	"kcpkey": "kcp_"+info['key']
                }
        """
        ss_setting = {
        	"listenport": info['listenport'],
        	"server": "127.0.0.1",
        	"serverport": info['listenport']+2000,
        	"sskey": "ss_"+info['key']
        }
        
        kcp_setting = {
        	"listenport": info['listenport']+2000,
        	"server": info['vpsip'],
        	"serverport": info['vpsport'],
        	"kcpkey": "kcp_"+info['key']
        }
        return ss_setting, kcp_setting

    def _gen_ss_conf(self, ss_setting):
        """Generate ss configuration according to [ss_setting].
        Arguments:
            ss_setting: A dict of information that ss configuration needed.

        Return:
            ss_conf: A dict that can be dumped to json file that used by ss.
        """
        ss_conf = {
            "server": ss_setting['server'],
            "server_port": ss_setting['serverport'],
            "local_address": "0.0.0.0",
            "local_port": ss_setting['listenport'],
            "password": ss_setting['sskey'],
            "timeout":600,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        return ss_conf

    def _gen_kcp_conf(self, kcp_setting):
        """Generate kcp according to [kcp_setting].
        Arguments:
            kcp_setting: A dict of information that kcp configuration needed. 

        Return:
            kcp_conf: A dict that can be dumped to json file that used by kcp.
        """
        kcp_conf = {
            "localaddr": "127.0.0.1:"+str(kcp_setting['listenport']),
            "remoteaddr": kcp_setting['server']+":"+str(kcp_setting['serverport']),
            "key": kcp_setting['kcpkey'],
            "mode": "fast2",
            "snmplog":"/clientlog/kcp-20060102.log"
        }
        return kcp_conf


class Server_Conf_Generator(Conf_Generator):
    """sskcp server configuration generator."""

    def _gen_info(self, infos_args):
        """Generate info list.
        Argument:
            infos_args = 
                {
                    'info-file': [/path/to/conf-info],
                    'mode': [ss/sskcp],
                    'log-dir': [/path/to/log],
                    'listenport': [port],
                    'key': [key],
                    'dest': [/path/to/config],
                }

        Return:
            infos_list: The list of infos.
                [
	                {
		                'mode': [ss/sskcp],
		                'log-dir': [/path/to/log]/[listenport],
		                'listenport': [port],
                        'key': [key],
		                'dest': [/path/to/config],
	                },
	                ...
                ]
        """
         # load info file to list
        info_file = infos_args.pop('info-file')
        infos_list = self.load_yaml(info_file)['server']
        
        # modify the value of [key] in info if value of [key] specified in infos_args[]
        for info in infos_list:
            for k, v in infos_args.items():
                if not v == None:
                    info[k] = v
            # modify the value of dest to info['dest']/info['listenport']
            info['dest'] = info['dest']+'/'+str(info['listenport'])
            # modify the value of log-dir to info['log-dir']/info['listenport']
            info['log-dir'] = info['log-dir']+'/'+str(info['listenport'])

        return infos_list

    def _gen_ss_setting(self, info):
        """Generate ss server setting for mode ss.
        Arguments:
            info: A dict of sskcp server information.
                {
	            	'listenport': [port],
                    'key': [key],
	            }

        Return:
            ss_setting: A setting dict for ss.json generation.
                {
                	"listenport": info['listenport'],
                	"sskey": "ss_"+info['key']
                }
        """
        ss_setting = {
            "listenport": info['listenport'],
            "sskey": "ss_"+str(info['key'])
        }
        return ss_setting

    def _gen_sskcp_setting(self, info):
        """Generate ss and kcp server setting for mode sskcp.
        Arguments:
            info: A dict of sskcp server information.
                {
	            	'listenport': [port],
                    'key': [key],
	            }

        Return:
            ss_setting: A setting dict for ss.json generation.
                {
                	"listenport": info['listenport']+2000,
                	"sskey": "ss_"+info['key']
                }

            kcp_setting: A setting dict for kcp.json generation.
                {
                	"listenport": info['vpsport'] ,
                	"server": 127.0.0.1,
                	"serverport": info['listenport']+2000,
                	"kcpkey": "kcp_"+info['key']
                }
        """
        ss_setting = {
            "listenport": info['listenport']+2000,
            "sskey": "ss_"+str(info['key'])
        }
        kcp_setting = {
            "listenport": info['listenport'],
            "serverport": info['listenport']+2000,
            "kcpkey": "kcp_"+str(info['key'])
        }
        return ss_setting, kcp_setting

    def _gen_ss_conf(self, ss_setting):
        """Generate ss configuration according to [ss_setting].
        Arguments:
            ss_setting: A dict of information that ss configuration needed.

        Return:
            ss_conf: A dict that can be dumped to json file that used by ss.
        """
        ss_conf = {
            "server":"0.0.0.0",
            "server_port": ss_setting['listenport'],
            "password": ss_setting['sskey'],
            "timeout":300,
            "method":"aes-256-cfb",
            "fast_open": True
        }
        return ss_conf

    def _gen_kcp_conf(self, kcp_setting):
        """Generate kcp according to [kcp_setting].
        Arguments:
            kcp_setting: A dict of information that kcp configuration needed. 

        Return:
            kcp_conf: A dict that can be dumped to json file that used by kcp.
        """
        kcp_conf = {
            "listen": "0.0.0.0:"+str(kcp_setting['listenport']),
            "target": "127.0.0.1:" + str(kcp_setting['serverport']),
            "key": kcp_setting['kcpkey'],
            "mode": "fast2",
            "snmplog": "/serverlog/kcp-20060102.log"
        }
        return kcp_conf
