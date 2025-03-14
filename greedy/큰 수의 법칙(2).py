n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

q = m // (k+1)
r = m % (k+1)

result = (r+q*k)*first + q*second

print(result)