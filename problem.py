""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin

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

cases = int(stdin.readline())
print('')
alfa = [0,1]
for i in range(2,44725):
  alfa.append(i + alfa[i-1])
while cases != 0:
    y = stdin.readline()
    x = abs(int(stdin.readline()))
    comp = binsearch(alfa,x)
    for j in range (2):
        if((alfa[comp] - x)%2 != 0):
            comp += 1
    print(comp)
    print('')
    cases -= 1