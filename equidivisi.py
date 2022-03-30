"""
Estudiante: Juan David Gomez
Codigo:8939024
"""

from sys import stdin

delta = [(-1, 0),(0, -1), (0, 1),(1, 0) ]
visited = None

def dfs(matrix,n,i,j,elem):
    global delta,visited
    ans = 1
    stack = [(i,j)]
    while len(stack) != 0:
        r,c = stack.pop()
        for dr,dc in delta:
            tmpr,tmpc = r+dr,c+dc
            if 0<=tmpr<n and 0<=tmpc<n and visited[tmpr][tmpc]==0 and matrix[tmpr][tmpc]== elem:
                stack.append((tmpr, tmpc)) ; visited[tmpr][tmpc] = 1
                ans += 1
        visited[r][c] = 2
    return ans
    
def solve(matrix,n):
    global visited
    ans = True
    visited = [ [0 for _ in range(n) ] for _ in range(n) ]
    conjuntos = [ 0 for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if (visited[i][j] == 0 and ans == True):
                conjuntos[matrix[i][j]] += 1 
                number = dfs(matrix,n,i,j,matrix[i][j])
                if(number != n):
                    ans = False
    for w in range(1,len(conjuntos)):
        if conjuntos[w] != 1:
            ans = False
    return ans
    
def main():
    n = int(stdin.readline())
    while n != 0:
        matrix = []
        for i in range(n): 
            lst = []
            for _ in range(n):
                lst.append(n)
            matrix.append(lst)
        for i in range(1,n):
            f = 0
            lista = [ int(x) for x in stdin.readline().split() ]
            while f < len(lista):
                matrix[lista[f] - 1][lista[f+1] - 1] = i
                f += 2
        if solve(matrix,n):
            print("good")
        else:
            print("wrong")
        n = int(stdin.readline())
main()