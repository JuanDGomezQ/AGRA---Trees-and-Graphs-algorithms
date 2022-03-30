"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin
from heapq import heappop,heappush

INF = float('inf')
G = None

def solve(police,banks):
  global INF,G
  ans = [ INF for _ in G ]
  visited = [ False for _ in G ]
  heap = []
  for i in range(len(police)):
      heap.append([0,police[i]])
      ans[police[i]] = 0
  while len(heap)!=0:
    d,u = heappop(heap)
    if visited[u]==False:
      for v,dv in G[u]:
        if d+dv<ans[v]:
          ans[v] = d+dv
          heappush(heap, [ans[v], v])
      visited[u] = True
  dist = []
  for i in range(len(banks)):
    dist.append([ans[banks[i]],banks[i]])
  dist.sort()
  e = len(dist) -1
  if len(dist) != 0:
    r = []
    temp = dist[e]
    r.append(temp)
    e -= 1
    while (e  >= 0 and temp[0] == dist[e][0]):
        r.append(dist[e])
        e -= 1
    if(r[0][0] != INF):
        print(len(r),r[0][0])
    else:
        print(len(r),"*")
    f = len(r) -1
    r.sort(reverse = True)
    while f >= 0:
        print(r[f][1],end = "")
        if(f != 0):
            print(" ",end="")
        f -= 1
    print()
  return (ans,dist)

def main():
    global G
    G = []
    l = stdin.readline().strip()
    while len(l) != 0:
        l = l.split()
        n = int(l[0])
        m = int(l[1])
        p = int(l[3])
        G = [list() for _ in range(n)]
        banks = []
        police = []
        for _ in range(m):
            u,v,t = map(int,stdin.readline().split()) 
            G[u].append([v,t])
            G[v].append([u,t])
        ban = stdin.readline().split()
        for i in range(len(ban)):
            banks.append(int(ban[i])) 
        if (p != 0):
            woop = stdin.readline().split()
            for i in range (len(woop)):
                police.append(int(woop[i]))
            solve(police,banks)
        else:
            banks.sort(reverse = True)
            e = len(banks) - 1
            print(len(banks), "*")
            while e >= 0:
                print(banks[e], end = "")
                if e != 0:
                    print(" ", end = "")
                e -= 1
            print()
        l = stdin.readline().strip()
main()