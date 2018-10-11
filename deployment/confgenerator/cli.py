import gen, gensskcp, genss
import argparse

def cli():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--ssport', dest="ssport", type=int, help='ss port')
    parser.add_argument('--kcpport', dest='kcpport', type=int, help='kcp port')
    parser.add_argument('--dest', dest="dest", type=int, help='dest')
    parser.add_argument('--vpsip', dest='vpsip', type=int, help='vps ip')

if __name__ == "__main__":
    args = vars(parser.parse_args())
    if args["vpsip"] == None:
        print("Wrong")
    elif args["kcpport"] == None:
        ss = genss.SS(args) 
        runner = gen.Generation().add(ss)
        runner.start("../conf")
    else:
        sskcp = gensskcp.SSKCP(args)
        runner = gen.Generation().add(sskcp)
        runner.start("../conf")
