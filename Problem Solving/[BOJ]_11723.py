import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

ans = set()

M = int(input())
for _ in range(M):
  info = sys.stdin.readline().strip().split()
  if len(info) == 1:
      if info[0] == "all":
          ans = set([x for x in range(1, 21)])
      else:
          ans = set()
      continue

  ord,n = info[0],info[1]
  now = int(n)

  if ord == "check":
      if now in ans:
          print(1)
      else:
          print(0)
  elif ord == "add":
        ans.add(now)
  elif ord == "remove":
        ans.discard(now)

  elif ord == "toggle":
      if now in ans:
          ans.discard(now)
      else:
          ans.add(now)





