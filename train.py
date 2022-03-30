""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin
setrecursionlimit(10**8)

MAX = 25010
train = None
inversions = 0
AUX = [ None for i in range(MAX) ]

def mergesort(A, low, hi):
  assert 0 <= low <= hi <= len(A)
  if low+1<hi:
    mid = low+((hi-low)>>1)    # mid = (low+hi)//2
    mergesort(A, low, mid)
    mergesort(A, mid, hi)
    merge(A, low, mid, hi)

def merge(A, low, mid, hi):
  global inversions
  for i in range(low, hi): AUX[i] = A[i]
  i,l,r = low,low,mid
  while i!=hi:
    if l==mid: A[i],r = AUX[r],r+1
    elif r==hi:
      A[i],l = AUX[l],l+1
    else:
      if AUX[l]<=AUX[r]: 
          A[i],l = AUX[l],l+1
      else: 
            A[i],r = AUX[r],r+1
            inversions += (mid - l)
    i += 1

def solve(n):
  global inversions
  mergesort(train,0,n)
  ans = inversions
  inversions = 0
  return ans


def main():
  global train
  global inversions
  cases = int(stdin.readline())
  while cases>0:
    n = int(stdin.readline())
    train = list(map(int, stdin.readline().split()))
    #for j in range(n):
      #print("Train in",j,":",train[j])
    print('Optimal train swapping takes {0} swaps.'.format(solve(n))) # Imprime retorno de solve, train es global por lo que no hace falta mandarle parametro
    cases -= 1

main()