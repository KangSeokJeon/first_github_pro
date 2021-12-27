import sys
arr = []
for i in range(0, 9):
    arr.append(int(sys.stdin.readline()))

print(max(arr))
print(arr.index(max(arr)) + 1)

# 주석 github에 추가되는지 확인