"""
Estudiante: Juan David Gomez
Codigo:8939024
"""

from sys import stdin
from collections import deque

matrix = None

def bfs(r,c,rows,cols):
    global matrix
    ans = []
    delta = [ (1,0),(0,-1), (0,1), (1,-1), (1,1) ]
    distancia = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    visited = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    queue = deque()
    queue.append((r,c))
    while (len(queue) != 0):
        r,c = queue.popleft()
        for dr,dc in delta:
            tmpr,tmpc = r +dr,c+dc
            if 0<= tmpr<rows and 0<=tmpc<cols  and matrix[tmpr][tmpc] == 1 and visited[tmpr][tmpc] == 0:
                dist = 0
                distancia[tmpr][tmpc] += distancia[r][c] + 1
                visited[tmpr][tmpc] = 1
                while matrix[tmpr][tmpc] != 0 and 0<= tmpr + 1<rows and 0<=tmpc + 1<cols:
                    dist = distancia[tmpr][tmpc] 
                    visited[tmpr][tmpc] = 1
                    tmpr += dr
                    tmpc += dc
                    dist = dist + 1
                nezt = False
                if 0<= tmpr<rows and 0<=tmpc<cols and visited[tmpr][tmpc] == 0:
                    distancia[tmpr][tmpc] = dist
                    for deltl,deltc in delta:
                        nexl,nexc = tmpr + deltl, tmpc + deltc 
                        if 0<= nexl<rows and 0<=nexc<cols:
                            if matrix[nexl][nexc] == 1:
                                nezt == True
                    if nezt == True:
                        queue.append((tmpr,tmpc))
                    else:
                        ans.append((tmpr + 1,tmpc + 1,distancia[tmpr][tmpc] - 1))
                        matrix[tmpr][tmpc] == 3
            elif 0<= tmpr<rows and 0<=tmpc<cols  and matrix[tmpr][tmpc]== 0 and visited[tmpr][tmpc] == 0 and (dr,dc) != (1,1) and (dr,dc) != (-1,1):
                ans.append((tmpr,tmpc,distancia[tmpr][tmpc]))
                matrix[tmpr][tmpc] == 3
    return ans

def orden(ans):
    return(-ans[0],ans[1])
def solve(r,c,rows,cols):
    global matrix
    ans = bfs(r,c,rows,cols)
    if len(ans) != 0:
        ans = sorted(ans,key = orden)
        for i in range(len(ans)):
            print("{0} {1} {2}".format(ans[i][0], ans[i][1], ans[i][2]))
        print("")
def main():
    global matrix
    lis = stdin.readline().strip()
    while(len(lis) != 0): 
        l,c = map(int,lis.split())
        matrix = [[ 0 for _ in range(c)] for _ in range(l)]
        for _ in range(c*4):
            x,y = map(int,stdin.readline().split())
            matrix[x-1][y-1] = 1
        sl,sc = map(int,stdin.readline().split())
        matrix[sl-1][sc-1] = 2
        lis = stdin.readline().strip()
        solve(sl - 1,sc - 1,l,c)
main()