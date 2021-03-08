def solution(skill, skill_trees):
    new_lis = []; c = 0
    
    for i in range(len(skill_trees)):
        strr = ''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                strr += skill_trees[i][j]
        new_lis.append(strr)
    
    skill_lis = []
    for i in range(1, len(skill)+1):
        skill_lis.append(skill[0:i])

    for k in new_lis:
        if k in skill_lis:
            c += 1
        if k == '':
            c += 1
            
    return c

sk = 'CBA'
sk_tree = ['CB', 'C', 'BA', 'BAC']
print(solution(sk, sk_tree))