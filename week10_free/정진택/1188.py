# 10/1

from sys import stdin 
n,m = map(int, stdin.readline().split())

def gcd(a,b):
    if b == 0:
        return a 
    return gcd(b, a%b)

print(m - gcd(m,n)) 
