import sys
arr = []
for i in range(0, 9):
    arr.append(int(sys.stdin.readline()))

print(max(arr))
print(arr.index(max(arr)))