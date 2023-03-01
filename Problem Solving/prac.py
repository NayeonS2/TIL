import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    parent = [0]*(N+1)

    for i in range(1,N+1):
        parent[i] = i

    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])

        return parent[x]

    def union_parent(parent,a,b):

        a = find_parent(parent,a)
        b = find_parent(parent,b)

        if a<b:
            parent[b] = a
        elif b<a:
            parent[a] = b


    info = list(map(int,input().split()))

    for i in range(0,len(info),2):
        a,b = info[i:i+2][0], info[i:i+2][1]
        union_parent(parent,a,b)

    ans = set()

    for i in parent:
        ans.add(find_parent(parent,i))
    print(f'#{tc} {len(ans)-1}')