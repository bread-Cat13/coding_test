n = int(input())
lst = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

curX, curY = 1, 1

for l in lst:
    for i in range(len(move_types)):
        if(move_types[i]==l):
            tempX = curX+dx[i]
            tempY = curY+dy[i]
    
    if(tempX < 1 or tempX > n or tempY < 1 or tempY > n):
        continue

    curX, curY = tempX, tempY










# for i in range(len(lst)):
#     cmd = lst[i]

#     if(cmd=='L'):
#         if( 1<= curX+dx[0] <= n):
#             curX+=dx[0]
#     elif(cmd=='R'):
#         if( 1<= curX+dx[1] <= n):
#             curX+=dx[1]
#     elif(cmd=='U'):
#         if( 1<= curY+dy[2] <= n):
#             curY+=dy[2]
#     else:
#         if( 1<= curY+dy[3] <= n):
#             curY+=dy[3]

print(curY, curX)