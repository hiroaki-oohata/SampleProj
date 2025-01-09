import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--hoge")
parser.add_argument('--piyo')
parser.add_argument('fuwa')
parser.add_argument('saku')
args = parser.parse_args()
print('引数 hoge : ', args.hoge)
print('引数 piyo : ', args.piyo)
print('引数 fuwa : ', args.fuwa)
print('引数 saku : ', args.saku)