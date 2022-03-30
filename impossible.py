""" 
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(999999999)

depth, low, stack, in_stack = None,None,None,None
G = None
ans = None

def dfs(u):
    global ans,depth, low, stack, in_stack,G
    assert low[u]==depth[u]
    stack.append(u)
    in_stack[u] = 1
    for v in G[u]:
        if depth[v]==-1: 
            depth[v] = low[v] = depth[u]+1
            dfs(v)
            low[u] = min(low[u], low[v])
        elif in_stack[v]: 
            low[u] = min(low[u], depth[v])
            
    if low[u]==depth[u]:
        aux = []
        while stack[-1]!=u:
            aux.append(stack.pop())
        aux.append(stack.pop())
        for x in aux:
            in_stack[x] = 0
        ans.append(aux)


def tarjan():
    global depth, low, stack, in_stack,G
    n = len(G)
    depth = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    stack = []
    in_stack = [0 for i in range(n)]

    for i in range(n):
        if depth[i]==-1:
            depth[i] = low[i] = 0
            dfs(i)

def main():
    global G,ans
    line = [int(x) for x in stdin.readline().split()]
    while len(line) != 0:
        ans,G = [],[]
        vert,fil = line[0],line[1]
        G = [[] for _ in range(vert)]
        for _ in range(fil):
            con = [int(x) for x in stdin.readline().split()]
            if con[0] == 1:
                G[con[1] -1].append(con[2] -1)
            else:
                it = 1
                while it < con[0]:
                    G[con[it]- 1].append(con[it + 1] -1)
                    G[con[it + 1] -1].append(con[it] -1)
                    it += 1
                G[con[1]-1].append(con[len(con)-1]-1)
                G[con[len(con)-1]-1].append(con[1]-1)
        tarjan()
        if len(ans) == 1:
            print("YES")
        else:
            print("NO")
        line = [int(x) for x in stdin.readline().split()]
main()