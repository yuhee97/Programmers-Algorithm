def solution(genres, plays):

    g_rank = {}; rank = {}

    for i in range(len(plays)):
        if genres[i] in g_rank:
            g_rank[genres[i]] += plays[i]
        else:
            g_rank[genres[i]] = plays[i] 

    for i in range(len(plays)):
        rank[str(i)] = [g_rank[genres[i]], plays[i]]
    rank = sorted(rank.items(), key = lambda x:x[1], reverse = True)

    result = []; value = ''

    print(rank)

    for i in rank:
        if value != i[1][0]:
            c = 0
        if c != 2:
            value = i[1][0]
            c += 1
            result.append(int(i[0]))
            continue

    return result

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution(g, p))