tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

def solution(tickets):

    route = []

    adjList = dict()

    for ticket in tickets:
        adjList[ticket[0]] = []
    for ticket in tickets:
        adjList[ticket[0]].append(ticket[1])
    for ticket in tickets:
        adjList[ticket[0]].sort(reverse=True)

    def dfs():
        stack = ["ICN"]

        while stack:
            now = stack[-1]

            if now not in adjList or len(adjList[now]) == 0:
                route.append(stack.pop())
            else:
                stack.append(adjList[now].pop())

    dfs()

    return route[::-1]

print(solution(tickets))