# 이모티콘

# 이미 화면에 이모티콘 1개를 입력
# 3가지 연산만 사용해서 이모티콘을 S개 만들기
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다.
# 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다.
# 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.
# 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다.
# 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

from collections import deque
import sys
input = sys.stdin.readline
S = int(input())
visited = dict()

def bfs(window,clip):

    q = deque()
    q.append((window, clip))
    visited[(window, clip)] = 1

    while q:
        window, clip = q.popleft()
        if window == S:
            print(visited[(window,clip)] -1)
            break
        else:
            if (window, window) not in visited.keys():
                q.append((window,window))
                visited[(window,window)] = visited[(window,clip)] + 1
            if (window+clip, clip) not in visited.keys():
                q.append((window+clip, clip))
                visited[(window+clip, clip)] = visited[(window,clip)] + 1
            if (window-1, clip) not in visited.keys():
                q.append((window-1, clip))
                visited[(window-1, clip)] = visited[(window,clip)] + 1

bfs(1,0)


