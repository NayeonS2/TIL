rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
# 1,1 / 1,3 / ... 1,7 -> (x_l,y_l~y_r)
# 1,1 / 2,1, ... 4,1 -> (x_l~x_r, y_l)
# 1,7 / 2,7 / 3,7 / 4,7 -> (x_l~x_r, y_r)
# 4,1 / 4,2 / 4,3 /... 4,7 -> (x_r, y_l~y_r)
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):

    visited = [[1] * 102 for _ in range(102)]
    poss = [[-1] * 102 for _ in range(102)]


    for rect in rectangle:
        x_l,y_l,x_r,y_r = rect[0]*2,rect[1]*2,rect[2]*2,rect[3]*2

        for x in range(x_l,x_r+1):
            for y in range(y_l,y_r+1):
                if x_l < x < x_r and y_l < y < y_r:
                    poss[x][y] = 0
                else:
                    if poss[x][y] != 0:
                        poss[x][y] = 1


    def bfs(i,j):
        q = deque()
        q.append((i*2,j*2))

        while q:

            i,j = q.popleft()

            if i == itemX*2 and j == itemY*2:
                return visited[i][j]//2
            else:
                for di,dj in [[1,0],[-1,0],[0,-1],[0,1]]:
                    ni,nj = i + di, j + dj

                    if visited[ni][nj] == 1 and poss[ni][nj] == 1:
                        q.append((ni,nj))
                        visited[ni][nj] = visited[i][j] + 1

    answer = bfs(characterX,characterY)

    return answer

print(solution(rectangle,characterX,characterY,itemX,itemY))



