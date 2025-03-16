inputStr=input()

gap = ord('a') - 1


curX = int(inputStr[1])
curY = ord(inputStr[0]) - gap



dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

cnt = 0

for i in range(len(dx)):
    nx = curX + dx[i]
    ny = curY + dy[i]

    if(nx<1 or ny<1 or nx>8 or ny>8):
        continue

    cnt+=1


print(cnt)
    
