""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin

rows,cols,plot = 0,0,None
delta = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]

def dfs(row, col, visited):
  sis = 0
  stack = [ (row, col) ] ; visited[row][col] = 1
  while len(stack)!=0:
    r,c = stack.pop()
    for dr,dc in delta:
      tmpr,tmpc = r+dr,c+dc
      if 0<=tmpr<rows and 0<=tmpc<cols and visited[tmpr][tmpc]==0 and plot[tmpr][tmpc]=='1':
        stack.append((tmpr, tmpc)) ; visited[tmpr][tmpc] = 1
    visited[r][c] = 2
    sis += 1 
  return sis

def solve():
  ans = 0
  max = 0
  visited = [ [ 0 for _ in range(cols) ] for _ in range(rows) ]
  print("vis:",visited)
  for r in range(rows):
    for c in range(cols):
      if visited[r][c]==0 and plot[r][c]=='1':
        max  = dfs(r, c, visited)
        if ans < max:
          ans = max
  return ans

def main():
  global rows,cols,plot
  casos = int(stdin.readline())
  stdin.readline().strip()
  while casos !=0:
    plot = []
    f = stdin.readline().strip()
    while len(f) != 0:
        plot.append(f)
        f = stdin.readline().strip()
    rows,cols = len(plot),len(plot[0])
    print("plot:",plot)
    print(solve())
    if casos != 1:
      print("")
    casos -= 1

main()