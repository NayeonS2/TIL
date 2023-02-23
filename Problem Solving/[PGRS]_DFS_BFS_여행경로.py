tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):

    adjList = dict()

    for ticket in tickets:
        adjList[ticket[0]] = []

    for ticket in tickets:
        adjList[ticket[0]].append(ticket[1])

    for k,v in adjList.items():
        v.sort(reverse=True)

    route = []
    def dfs():

        stack = ["ICN"]

        while stack:

            now = stack[-1]

            if now not in adjList or len(adjList[now])==0:
                route.append(stack.pop())
            else:
                next = adjList[now].pop()
                stack.append(next)

    dfs()

    return route[::-1]

print(solution(tickets))