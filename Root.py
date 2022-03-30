from sys import stdin
from collections import deque
import sys
import math
sys.setrecursionlimit(10**8)

"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

def dfs(u):
    global G, lb, vis
    vis[u] = 1
    ans = 0
    for v in G[u]:
        if vis[v]==0:
            dfs(v)
            ans = max(ans, 1+lb[v])
    lb[u] = ans
    return


def diam(u):
    global G, lb, vis
    vis[u] = 1
    R = r = 0 # Length of longest and second longest path u-->leaf
    for v in G[u]:
        if vis[v]==0:
            x = 1 + lb[v]
            if x >= R: r=R; R=x
            elif x>r: r=x
    ans1 = r + R # length of longest path that uses u
    #ans1 = sum(sorted(1+lb[v] for v in G[u])[-2:]) # alternative
    ans2 = 0 # length of longest path that does not use u
    for v in G[u]:
        if vis[v]==0:
            ans2 = max(ans2, diam(v))
    ans = max(ans1, ans2)
    return ans

def bfs(s):
  global G, n
  dist,visited = [ None ]*len(G),[ 0 ]*len(G)
  queue = deque()
  queue.append(s) ; dist[s] = 0
  while len(queue)!=0:
    u = queue.popleft()
    for v in G[u]:
      if visited[v]==0:
        queue.append(v)
        visited[v] = 1
        dist[v] = dist[u]+1
    visited[u] = 2
  return (dist)

def main():
    global G,lb,vis
    nodes = stdin.readline().split()
    while len(nodes) != 0:
        n = int(nodes[0])
        G = [[] for i in range(n)]
        for i in range(n):
            inp = stdin.readline().split()
            for j in range(1,len(inp)):
                G[i].append(int(inp[j]) - 1)
        root = 0 
        lb = [None]*n # lb[u] = length of longest path u-->leaf
        vis = [0]*n
        dfs(root)
        vis = [0]*n
        ans = diam(root)
        best,worst = [],[]
        b = bfs(0)
        mx = max(b)
        for i in range(len(b)):
            if b[i] == mx:
                worst.append(i + 1)
        b = bfs(worst[0] - 1)
        mx = max(b)
        for i in range(len(b)):
            if b[i] >= mx and not(i + 1 in worst):
                worst.append(i + 1)
        for i in range(len(lb)):
            if(lb[i] == int(math.ceil(float(ans)/2)) or lb[i] == int(math.floor(float(ans)/2))):
                best.append(i+1)
        best.sort()
        worst.sort()
        print("Best Roots  :",*best)
        print("Worst Roots :",*worst)
        nodes = stdin.readline().split()
main()
