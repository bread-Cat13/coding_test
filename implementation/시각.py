n = int(input())

cnt = 0
A = 15*60 + 45 * 15

if(n<3):
    cnt = (n+1)*A

elif(n<13):
    cnt = n*A + 3600

elif(n<23):
    cnt = (n-1)*A + 2*3600

else:
    cnt = (n-2)*A + 3*3600

print(cnt)

