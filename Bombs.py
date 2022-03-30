""" 
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(999999999)
G,parent,rails = [],[],[]
it = None
def dfs(u):
    global depth, low, stack, in_stack,G,parent,rails
    assert low[u]==depth[u]
    stack.append(u)
    in_stack[u] = 1
    son = 0
    for v in G[u]:
        if depth[v]==-1: # tree-edge
            son += 1
            parent[v] = u
            depth[v] = low[v] = depth[u]+1
            dfs(v)
            low[u] = min(low[u], low[v])
            if((depth[u] <= low[v] and parent[u] != -1) or (parent[u] == -1 and  1 < son)):
                rails[u][0] = rails[u][0] + 1
        elif in_stack[v]: # back-edge
            low[u] = min(low[u], depth[v])
        else: # cross-edge
            pass
    # low[u] ya esta calculado
    if low[u]==depth[u]:
        # pop from stack until u
        aux = []
        while stack[-1]!=u:
            aux.append(stack.pop())
        aux.append(stack.pop())
        for x in aux:
            in_stack[x] = 0
    return

def orde(v):
    global it,rails
    while(it  >= 0 and v == rails[it][0]):
        it-= 1
    return it + 1


def tarjan(m):
    global depth, low, stack, in_stack,G,parent,rails,it
    n = len(G)
    depth = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    parent = [- 1 for i in range(n)]
    stack = []
    in_stack = [0 for i in range(n)]
    rails = [[1,i] for i in range(n)]
    for i in range(n):
        if depth[i]==-1:
            depth[i] = low[i] = 0
            dfs(i)
    rails.sort()
    it = n -1
    dep = n -1
    k = n
    cnt = 0
    while(cnt < m and dep -1  > 0):
        v = rails[dep][0]
        dep = orde(v)
        aux = dep
        while(cnt < m and dep < k):
            cnt +=1
            print(rails[dep][1],rails[dep][0])
            dep += 1
        k = aux
        v = rails[aux -1]
        dep = aux - 1
    print("")

def main():
    global G
    n,m = map(int,stdin.readline().split())
    while n != 0 and m != 0:
        G = [[] for _ in range(n)]
        x,y = map(int,stdin.readline().split())
        while x != -1 and y != -1:
            if not(y in G[x]):
                G[x].append(y)
            if not (x in G[y]):
                G[y].append(x)
            x,y = map(int,stdin.readline().split())
        tarjan(m)
        n,m = map(int,stdin.readline().split())
    
main()