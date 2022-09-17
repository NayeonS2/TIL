
import sys
sys.stdin = open('input.txt')


def inorder(n):
    if not tree[n]:
        return elem[n]
    left = inorder(ch1[n])
    right = inorder(ch2[n])

    if elem[n] == "+":
        return left + right
    elif elem[n] == "-":
        return left - right
    elif elem[n] == "*":
        return left * right
    elif elem[n] == "/":
        return left//right




for tc in range(1,11):
    N = int(input())

    elem = [0] * (N+1)

    edges = []

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    tree = [[] for _ in range(N+1)]



    for _ in range(N):
        info = list(input().split())


        if len(info) == 2:
            node, num = info[0], info[1]
            elem[int(node)] = int(num)



        elif len(info) == 4:
            node, opr, ch1_node, ch2_node = info[0], info[1], info[2], info[3]
            elem[int(node)] = opr
            edges.append((int(node),int(ch1_node)))
            edges.append((int(node), int(ch2_node)))
            tree[int(node)].append(ch1_node)
            tree[int(node)].append(ch2_node)



    for edge in edges:
        p,c = edge[0], edge[1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    #print(f'#{tc} {elem}') #1 [0, '-', '-', 10, 88, 65]
    #print(f'#{tc} {tree}') #1 [[], ['2', '3'], ['4', '5'], [], [], []]
    print(f'#{tc} {inorder(1)}')