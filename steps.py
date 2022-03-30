""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin

alfa = [0,1]

def binsearch(A, x):
  ans,N = 0,len(A)
  if N!=0:
    low,hi = 1,N
    while low+1!=hi:
      mid = low+((hi-low)>>1)
      assert low<mid<hi
      if A[mid]<=x: low = mid
      else: hi = mid
    if(A[low] < x):
        ans = low +1
    else:
        ans = low
  return ans

def solve(x, y):
  global alfa
  ans = 0
  dist = y - x
  if(dist != 0):
    ans = binsearch(alfa,dist)
  return ans

def main():
    global alfa
    steps = None
    for n in range(2,190000):
        if( n%2 == 0):
            mid = n/2
            steps = mid*(mid+1)
            alfa.append(steps)
        else:
            mid = n//2
            steps = mid*(mid+1) + mid +1
            alfa.append(steps)
    tcnt = int(stdin.readline())
    while tcnt!=0:
        tok = stdin.readline().split()
        print(solve(int(tok[0]), int(tok[1])))
        tcnt -= 1

main()