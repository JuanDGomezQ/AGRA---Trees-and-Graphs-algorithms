""" Spreding the new, BY: Camilo Rocha"""
from sys import stdin
from collections import deque

lenv,graph = None,None

def solve(s):
  ansc,ansd = 0,0
  dist,cnt,visited = [ None ]*lenv,[ 0 ]*(lenv+1),[ 0 ]*lenv
  print("Distancia:",dist)
  print("cnt:", cnt)
  print("visited",visited)
  queue = deque()
  queue.append(s) ; dist[s] = 0
  print("queue",queue)
  while len(queue)!=0:
    u = queue.popleft()
    cnt[dist[u]] += 1
    if cnt[dist[u]]>ansc: ansc,ansd = cnt[dist[u]],dist[u]
    for v in graph[u]:
      if visited[v]==0:
        queue.append(v)
        visited[v] = 1
        dist[v] = dist[u]+1
    visited[u] = 2
    print("cnt",cnt)
    print("visited",visited)
    print("Distancia:",dist)
  print("visited",visited)
  print("Distancia:",dist)
  if ansd==0: ansc = 0
  return (ansc, ansd)


def main():
  global lenv,graph
  lenv = int(stdin.readline())
  graph = list()
  for _ in range(lenv):
    tok = [ int(x) for x in stdin.readline().split() ]
    graph.append(tok[1:])
  print( "graph:",graph)
  tcnt = int(stdin.readline())
  for _ in range(tcnt):
    cnt,day = solve(int(stdin.readline()))
    if cnt!=0: print('{0} {1}'.format(cnt, day))
    else: print(0)

main()
