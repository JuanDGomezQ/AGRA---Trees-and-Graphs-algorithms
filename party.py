""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin
from collections import deque

graph = None
lenv = None

def solve(s):
  dist,visited = [ None ]*lenv,[ 0 ]*lenv
  queue = deque()
  queue.append(s) ; dist[s] = 0
  while len(queue)!=0:
    u = queue.popleft()
    for v in graph[u]:
      if visited[v]==0:
        queue.append(v)
        visited[v] = 1
        dist[v] = dist[u]+1
    visited[u] = 2
  return (dist)

def main():
    global lenv,graph
    casos = int(stdin.readline())
    while casos != 0:
        graph = list()
        stdin.readline()
        lenv,coup = map(int,stdin.readline().split())
        for v in range(0,lenv):   
            graph.append([]) 
        while int(coup) != 0:
            tok = [ int(x) for x in stdin.readline().split() ]
            graph[tok[0]].append(tok[1])
            graph[tok[1]].append(tok[0])
            coup -= 1
        giovNum = solve(0)
        for v in range(1,len(giovNum)):
            print(giovNum[v])
        if(casos != 1):
          print("")
        casos -= 1
main()    