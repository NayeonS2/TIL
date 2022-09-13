import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])



V = int(input())
E = V - 1
edges = list(map(int,input().split()))
root = 1

ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = edges[i*2], edges[i*2+1]

    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

preorder(root)