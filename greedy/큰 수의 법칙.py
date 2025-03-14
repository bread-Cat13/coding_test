N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

first = arr[0]
second = arr[1]



result = 0
count = 0
n_cnt = 0

# while(count < M):
#     if n_cnt == K:
#         n_cnt = 0
#         result+=second
#     else:
#         n_cnt+=1
#         result+=first
#     count+=1


while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1

    if M == 0: 
        break
    
    result += second
    M-=1

print(result)