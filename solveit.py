import math
from sys import stdin

esp = 10**-7
p,q,r,s,t,u = 0,0,0,0,0,0

def solve(x):
        global p,q,r,s,t,u
        return p*math.exp(-x) + q*math.sin(x) + r*math.cos(x) + s*math.tan(x) + t*x*x + u

def bis():
        global p,q,r,s,t,u
        low,hi = 0,1
        while (low + esp < hi):
                x = (low+hi)/2
                if (solve(low) * solve(x) <= 0):
                	hi = x
                else:
                	low = x
        return round(((low + hi)/2),4)

def main():
    global p,q,r,s,t,u
    lista = list(map(int, stdin.readline().split()))
    while len(lista) != 0:
        p = lista[0]
        q = lista[1]
        r = lista[2]
        s = lista[3]
        t = lista[4]
        u = lista[5]
        if((solve(0) * solve(1)) > 0):
            print("No solution")
        else:
            print(bis())
        lista = list(map(int, stdin.readline().split()))

main()