import sys
n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data.sort()
print("%d %d"%(data[0], data[-1]))
