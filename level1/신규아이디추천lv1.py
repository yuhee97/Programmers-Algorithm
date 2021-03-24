import re

def first_step(id):
    return id.lower()

def second_step(id):
    id = re.sub("[^a-z0-9._-]", "", id)
    return id
                    
def third_step(id):
    id = re.sub("\.\.*", ".", id)
    return id
                                
def four_step(id):
    if id[0] == '.':
        if len(id) > 1:
            id = id[1:] 
    if id[-1] == '.':
        if len(id) > 1:
            id = id[0:len(id)-1] 
    if len(id) == 1:
        if id[0] == '.':
            return ''
    return id
                    
def five_step(id):
    if len(id) == 0:
        id = 'a'
    return id
                    
def six_step(id):
    if len(id) > 15:
        if id[14] == '.':
            return id[0:14]
        return id[0:15]
    return id

def seven_step(id):
    if len(id) < 3:
        id += id[-1] * (3-len(id))
    return id
                    
def solution(new_id):
    n_id = first_step(new_id)
    n_id = second_step(n_id) 
    n_id = third_step(n_id)
    n_id = four_step(n_id)
    n_id = five_step(n_id)
    n_id = six_step(n_id)
    n_id = seven_step(n_id)
    return n_id

new = "...!@BaT#*..y.abcdefghijklm"
print(solution(new))