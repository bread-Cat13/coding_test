n,m = map(int, input().split())

curR, curC, dType = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

def isValid(curR, curC, dType, normal):
    if(normal):
        nR = curR + dR[dType]
        nC = curC + dC[dType]
        print("왼쪽 방향 좌표: ("+str(nR)+", "+str(nC)+")")
        if(nR<0 or nC<0 or nR>=n or nC>=m):
            print("map 바깥입니다.")
            return False
        elif(map[nR][nC]==1):
            print("바다입니다.")
            return False

        return True
    else:
        nR = curR - dR[dType]
        nC = curC - dC[dType]
        print("뒤로가기 방향 좌표: ("+str(nR)+", "+str(nC)+")")
        if(nR<0 or nC<0 or nR>=n or nC>=m):
            return False
        elif(map[nR][nC]==1):
            return False

def move(curR, curC, dType, normal):
    if(normal):
        curR += dR[dType]
        curC += dC[dType]
    else:
        curR -= dR[dType]
        curC -= dC[dType]
    
    return (curR, curC)


map[curR][curC] = 1
visitCnt = 1

while True:
    checkCnt = 0
    while checkCnt<4:
        checkDtype = (dType+3)%4
        print("현재 방향: ", dType, "// 왼쪽 방향: ",checkDtype)
        ok = isValid(curR, curC, checkDtype, True)
        print("ok: ", ok)
        #전진 가능
        if(ok):
            dType = checkDtype
            curR, curC = move(curR, curC, dType, True)
            print("이동합니다. 가는 좌표: ("+str(curR)+","+str(curC)+")")
            map[curR][curC] = 1 #방문함(바다로 바꾸기기)
            visitCnt+=1
            break
        #방향만 왼쪽
        else:
            dType = checkDtype
            checkCnt+=1
    
    if(checkCnt==4):
        print("뒤로 무르기 part")
        ok = isValid(curR, curC, dType, 0)
        if(ok):
            print("뒤로 한 칸 갑니다. 방향 - ", dType)
            curR, curC = move(curR, curC, dType, 0)
        else:
            print("뒤로 갈 수 없습니다!!!")
            break

print(visitCnt)       
    


##잘못된 이유
#1. 잘못된 문제 이해
# - 방문한 곳은 육지로 나둬야 함. 따로 배열로 관리해줘야함. 
# - 뒤로 후진한다는 것은 잘 생각해보면 이미 방문했던 곳 or 바다임 count+1하면 안됨. 
#2. 문제 그대로 코드를 짜자. 
#3. global 변수를 사용할 수 있음을 명심하자. 
#4. 공통 행위는 함수로 묶자. 최소단위로 묶자!!


