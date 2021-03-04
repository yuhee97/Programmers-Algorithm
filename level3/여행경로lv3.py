from collections import defaultdict


def dfs(route, n, stack, answer):
    if len(answer) == n + 1:
        return answer[::-1]

    while stack:
        top = stack[-1]
        if len(route[top]) == 0:
            answer.append(stack.pop())
            return dfs(route, n, stack, answer)
        else:
            stack.append(route[top].pop())
            return dfs(route, n, stack, answer)


def solution(tickets):
    route = defaultdict(list)
    for a, b in tickets:
        route[a].append(b)

    for key in route.keys():
        route[key].sort(reverse=True)

    return dfs(route, len(tickets), ["ICN"], [])
    
tt = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tt))