import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

list_str = list(map(int, list(str(a * b * c))))
# print(list_str)
for i in range(10):
    print(list_str.count(i))