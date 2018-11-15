"""
"""

import os
import argparse
import sskcp_confgenerator.generator as GEN
import sskcp_confgenerator.validator as VAL

# traceback setting
#sys.tracebacklimit = 0
CONFGEN_DIR=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class Confgen_Cli():
    """The cli of sskcp confgenerator."""

    def __init__(self, generator, validator, gen_dir):
        """
        Arguments:
            generator: the generator for generating sskcp configuration.
            validator: the validator for validating sskcp conf-info.
        """
        self.gen = generator
        self.val = validator
        self.dir = gen_dir
        self._parse_arg()

    def _parse_arg(self):
        """Design the cli of sskcp configuration generator.
        Arguments:
            client:
                -f [conf-info]: The path of client conf-info file. The default value is pwd/../sskcp-client-info.yml
            server:
                -f [conf-info]: The path of server conf-info file. The default value is pwd/../sskcp-server-info.yml
        
        Return:
            parser: The argument parser of cli.
        """
        parser = argparse.ArgumentParser(description="Generate sskcp configuration.")
        subcmd = parser.add_subparsers(title="subcommand", dest="site")
        
        client = subcmd.add_parser('client', help="Generate client configuration.")
        client.add_argument('-f', '--info-file', dest="info-file", default=self.dir+"/sskcp-client-info.yml")
        client.add_argument('-m', '--mode', dest="mode")
        client.add_argument('--log-dir', dest="log-dir")
        client.add_argument('--listenport', dest="listenport")
        client.add_argument('--vpsip', dest="vpsip")
        client.add_argument('--vpsport', dest="vpsport")
        client.add_argument('--key', dest="key")
        client.add_argument('-d', '--dest', dest="dest")

        server = subcmd.add_parser('server', help="Generate server configuration.")
        server.add_argument('-f', '--info-file', dest="info-file", default=self.dir+"/sskcp-server-info.yml")
        server.add_argument('-m', '--mode', dest="mode")
        server.add_argument('--log-dir', dest="log-dir")
        server.add_argument('--listenport', dest="listenport")
        server.add_argument('--key', dest="key")
        server.add_argument('-d', '--dest', dest="dest")

        self.parser = parser

    def gen_conf(self):
        """Generate sskcp configuration."""
        args = vars(self.parser.parse_args())
        site = args.pop('site').title()
        generator = getattr(self.gen, site+"_Conf_Generator")
        validator = getattr(self.val, site+"_Validator")
        print(args)
        return generator(args, validator).generate()

if __name__ == "__main__":
    CLI = Confgen_Cli(GEN, VAL, CONFGEN_DIR)
    CLI.gen_conf()
