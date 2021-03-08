import math

def solution(w,h):
    entire = w * h
    gcd = math.gcd(w, h)
    return entire - gcd * (w//gcd + h//gcd - 1)


ww = 12
hh = 8
print(solution(ww, hh))