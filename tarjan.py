""" Tarjan Algorithm: 
    In: Un grafo G = (V,E).
    Out: Una particion de V en componentes fuertemente conexos.

   Nota: Una particion es una division de un conjunto X donde la union de todas las particiones
   de X me tiene que dar X y donde la intercepcion de todas las particiones me tiene que dar vacio. 

"""
def dfs(u):
    assert low[u]==depth[u]
    stack.append(u)
    in_stack[u] = 1
    for v in G[u]:
        if depth[v]==-1: # tree-edge
            depth[v] = low[v] = depth[u]+1
            dfs(v)
            low[u] = min(low[u], low[v])
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
        print(aux)
    return


def tarjan():
    global depth, low, stack, in_stack
    n = len(G)
    depth = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    stack = []
    in_stack = [0 for i in range(n)]

    for i in range(n):
        if depth[i]==-1:
            depth[i] = low[i] = 0
            dfs(i)

G = [
    [3],
    [3,7],
    [5,7],
    [4,6],
    [1,5],
    [2],
    [0,2],
    []
]

tarjan()