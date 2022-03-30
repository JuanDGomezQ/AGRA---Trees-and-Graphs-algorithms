"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin,setrecursionlimit

setrecursionlimit(10**8)
inp = None

def parse():
    global inp

def main():
    global find,inp
    inp = stdin.read()
    inp = inp.replace("\n","")
    inp = inp.replace(" ","")
    print(inp)
    op = 0
    cl = 0
    i = 0
    case = []
    while inp[i] != '(':
        case.append(inp[i])
        inp.popleft()
        i +=1
    print(case,inp)
main()