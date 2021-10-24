import sys

n, m = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

high = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        high = mid
        start = mid + 1

print(high)