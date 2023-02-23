tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

def solution(tickets):
    answer = []

    route = []

    adjList = dict()

    for ticket in tickets:
        adjList[ticket[0]] = []
    for ticket in tickets:
        adjList[ticket[0]].append(ticket[1])


    return answer