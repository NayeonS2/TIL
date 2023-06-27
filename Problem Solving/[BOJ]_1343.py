# 폴리오미노

# AAAA , BB
# replace() 는 왼쪽부터 해당 문자열 치환

import sys

sys.stdin = open('input.txt')


board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)





# lst = []
# comp = ''
# dot = ''
# for i in range(len(board)):
#     if board[i] == 'X':
#         comp += board[i]
#         if len(dot)>0:
#             lst.append(dot)
#         dot = ''
#     elif board[i] == '.':
#         dot += board[i]
#         if len(comp)>0:
#             lst.append(comp)
#         comp = ''
#
# if len(lst) > 1:
#     sep = lst[-1]
#     last = board.split(sep)[1]
#     lst.append(last)
# else:
#     lst.append(board)
#
# ans = lst[:]
#
# n_lst = []
# for a in ans:
#     if '.' not in a:
#         tmp = ''
#         tmp_l = len(a)
#         if len(a)%2 != 0:
#             break
#         while len(tmp) != tmp_l:
#
#             tmp += 'AAAA'*(len(a)//4)
#             a = a[(4*(len(a)//4)):]
#
#             tmp += 'BB'*(len(a)//2)
#             a = a[(2*(len(a)//2)):]
#         n_lst.append(tmp)
#     else:
#         n_lst.append(a)
#
# if len(lst) == len(n_lst):
#     print(''.join(n_lst))
# else:
#     print(-1)





