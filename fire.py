""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin

rows,cols,G = 0,0,None
delta = [(-1, 0),(0, -1), (0, 1),(1, 0) ]

def bfs(posf):
    global rows,cols,G,delta
    visited = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    distancia = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    stack = []
    for i in range(len(posf)):
        row = posf[i][0]
        col = posf[i][1]
        stack.append((row,col))
        visited[row][col] = 1 
        distancia[row][col] = 1
    while len(stack)!=0:
        r,c = stack.pop()
        for dr,dc in delta:
            tmpr,tmpc = r+dr,c+dc
            if 0<=tmpr<rows and 0<=tmpc<cols and visited[tmpr][tmpc]==0 and (G[tmpr][tmpc] == '.' or G[tmpr][tmpc] == 'J'):
                stack.append((tmpr, tmpc)) ; visited[tmpr][tmpc] = 1
                distancia[tmpr][tmpc] += distancia[r][c] + 1
        visited[r][c] = 2
    return distancia

def bfsj(posf,timef):
    global rows,cols,G,delta
    visited = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    distancia = [ [0 for _ in range(cols) ] for _ in range(rows) ]
    stack = []
    row = posf[0][0]
    col = posf[0][1]
    stack.append((row,col))
    visited[row][col] = 1 
    distancia[row][col] = 1
    ans = 99999999999
    while len(stack)!=0:
        r,c = stack.pop()
        for dr,dc in delta:
            tmpr,tmpc = r+dr,c+dc
            if 0<=tmpr<rows and 0<=tmpc<cols and visited[tmpr][tmpc]==0 and G[tmpr][tmpc] == '.' and timef[tmpr][tmpc] > distancia[r][c] + 1:
                stack.append((tmpr, tmpc)) ; visited[tmpr][tmpc] = 1
                distancia[tmpr][tmpc] += distancia[r][c] + 1
            if(tmpr >= rows or tmpc >= cols or tmpc < 0 or tmpr < 0):
                if (distancia[r][c] < ans):
                    ans = distancia[r][c]
        visited[r][c] = 2
    return ans

def solve(posf,posj):
    timef = bfs(posf)
    timej = bfsj(posj,timef)
    if(timej != 99999999999):
        print(timej)
    else:
        print("IMPOSSIBLE")



def main():
    global G,rows,cols
    casos = int(stdin.readline())
    while casos != 0:
        G = []
        posf = []
        posj = []
        rows,cols = map(int,stdin.readline().split())
        for v in range(0,rows):
            f = str(stdin.readline().strip())
            for j in range(0,len(f)):
                if f[j] == "F":
                    posf.append([v,j])
                elif f[j] == "J":
                    posj.append([v,j])
            G.append(f)
        solve(posf,posj)
        casos -= 1    
main()