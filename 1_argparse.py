import argparse
#创建一个解析器
parser = argparse.ArgumentParser(description='Process some integers.')
#添加参数
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
#解析参数
args = parser.parse_args()

print(args.accumulate(args.integers))
