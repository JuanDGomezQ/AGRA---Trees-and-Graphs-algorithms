from sys import stdin

n,distMax,nodoMax,wa = None,None,None,None
G = None

def dfs(v, padre, dist):
    global G,n,distMax,nodoMax,wa
    if(dist > distMax):
        distMax = dist
        nodoMax = v

    for i in range(len(G[v])):
        w = G[v][i][0]
        if(w != padre):
            #print("hijo:",w)
            dfs(w,v,dist + G[v][i][1])

def diametro():
    global G,n,distMax,nodoMax
    distMax = 0
    dfs(1, 0, 0)
    dfs(nodoMax,0,0)
    return distMax

def main():
    global G,n,distMax,nodoMax
    l = stdin.readline()
    while len(l) != 0:
        G = [[] for i in range(10000)]
        distMax,nodoMax = 0,0
        while len(l) != 0:
            n,a,p = map(int,l.strip().split())
            G[n].append((a,p))
            G[a].append((n,p))
            #print(G)
            l = stdin.readline().strip()
        print(diametro())
        l = stdin.readline()
main()