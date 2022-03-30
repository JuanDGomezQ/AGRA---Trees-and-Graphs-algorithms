"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**8)
G = None

def dfs_topo(G, vis, s, i):
    vis[i] = 1
    for j in G[i]:
        if vis[j]==0:
            dfs_topo(G, vis, s, j)
    s.append(i)
    return

def main_topo(G):
    s = []
    n = len(G)
    vis = [0]*n
    for i in range(n):
        if vis[i]==0:
            dfs_topo(G,vis,s,i)
    return s

def dfs_scc(G, vis, cnt, i):
    vis[i] = cnt
    for j in G[i]:
        if vis[j]==-1:
            dfs_scc(G, vis, cnt, j)
    return

def kosaraju(G):
    n = len(G)
    
    R = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            R[j].append(i)
    topo = main_topo(R)
    
    cnt = 0
    scc = [-1]*n
    while len(topo):
        i = topo.pop()
        if scc[i]==-1:
            dfs_scc(G,scc,cnt,i)
            cnt += 1
    return cnt

def main():
    global G
    p,t = map(int,stdin.readline().split())
    while p != 0 or t != 0:
        names = {}
        G = [[] for _ in range(p)]
        for i in range(p):
            name = stdin.readline()
            names[name] = i
        for _ in range(t):
            a = stdin.readline()
            b = stdin.readline()
            G[names[a]].append(names[b])
        print(kosaraju(G))
        p,t = map(int,stdin.readline().split())
main()