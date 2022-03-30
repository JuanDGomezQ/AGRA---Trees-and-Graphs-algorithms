
"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin
pre = []
ans = []

def pos(low,hi):
    global pre,ans
    if low < hi:
        izq = low + 1
        while izq < hi and pre[low] > pre[izq]:
            izq += 1
        pos(low + 1, izq)
        pos(izq,hi)
        ans.append(pre[low])
    return(ans)

def main():
    global pre  
    elem = stdin.readline().strip()
    while len(elem) != 0:
        v = int(elem.strip())
        pre.append(v)
        elem = stdin.readline().strip()
    low = 0
    hi = len(pre)
    ans = pos(low,hi)
    for i in ans:
        print(i)
main()