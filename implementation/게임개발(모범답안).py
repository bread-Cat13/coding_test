n, m = map(int, input().split())

x, y, direction = map(int, input().split())

d = [[0]*m for _ in range(n)]
d[x][y] = 1

map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction = (direction+3)%4

count = 1
turn_time = 0 #4가 되면 뒤로 후진진

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if(nx<0 or ny<0 or nx>=n or ny>=m):
        continue

    #정상적으로 왼쪽으로 가기
    if(d[nx][ny]==0 and map[nx][ny]==0):
        x = nx
        y = ny
        d[nx][ny] = 1
        count+=1
        turn_time = 0
        continue
    #왼쪽으로 갈 수 없는 경우
    else:
        turn_time+=1


    #4면 다 봤음
    if(turn_time==4):
        nx = x - dx[direction]
        ny = y - dy[direction]

        if(nx<0 or ny<0 or nx>=n or ny>=m):
            break
        if(map[nx][ny]==0):
            x = nx
            y = ny
            turn_time = 0
        else:
            break
    
print(count)

       


    



    

    

