import gensskcp
import argparse

def cli():
    parser = argparse.ArgumentParser(description='Process some integers.')
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='additional help -h', dest='subcmd')
    client_parser = subparsers.add_parser('client')
    client_parser.add_argument('--ssport', dest="ssport", type=int, help='ss port')
    client_parser.add_argument('--vpsip', dest='vpsip', help='vps ip')
    client_parser.add_argument('--kcpport', dest='kcpport', type=int, help='kcp port')
    client_parser.add_argument('--key', dest='key', help='key for password')
    client_parser.add_argument('--dest', dest="dest", help='dest', default="")
    server_parser = subparsers.add_parser('server')
    server_parser.add_argument('--kcpport', dest='kcpport', type=int, help='kcp port')
    server_parser.add_argument('--key', dest='key', help='key for password')
    server_parser.add_argument('--dest', dest="dest", help='dest', default="")

    return parser

if __name__ == "__main__":
    args = vars(cli().parse_args())
    if args["subcmd"] == "client":
        sskcp = gensskcp.SSKCP(args)
        sskcp.write_client("../conf")
    elif args["subcmd"] == "server":
        sskcp = gensskcp.SSKCP(args)
        sskcp.write_server("../conf")
    else:
        print("Wrong")
