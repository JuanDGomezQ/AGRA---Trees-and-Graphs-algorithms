from sys import stdin
"""
  Nombre: Juan David Gomez
  Codigo: 8939024
"""

orda = ord('A')
table = None

def binsearch(A, x):
  ans,N = 0,len(A)
  if N!=0:
    low,hi = 0,N
    while low+1!=hi:
      mid = low+((hi-low)>>1)
      assert low<mid<hi
      if A[mid]<=x: low = mid
      else: hi = mid
    if(A[low] >= x):
        ans = low
    else:
        if(low + 1 < len(A)): 
            if (A[low] < x and A[low + 1] >= x):
                ans = low + 1
        else:
            ans = -1
  if(len(A) == 0):
    ans = -1
  return ans

def builder(text):
    global orda
    table = [list() for _ in range(orda,ord('z') + 1)]
    for j in range(len(text)):
        i = ord(text[j]) - orda
        table[i].append(j)
    return table

def solve(text, p):
  global orda,table
  it,fst,lst = 0,0,0
  prim = False
  ans = True
  for j in range(len(p)):
    elem = binsearch(table[(ord(p[j]) - orda)],it)
    if elem == -1:
      ans = False
    else:
      if(prim == False):
        fst = table[(ord(p[j]) - orda)][elem]
        prim = True
      it = table[(ord(p[j]) - orda)][elem] + 1
  lst = it - 1
  return ans,fst,lst

def main():
  global table
  text = stdin.readline().strip()
  tcnt = int(stdin.readline())
  table = builder(text)
  while tcnt!=0:
    p = stdin.readline().strip()
    ans,first,last = solve(text, p)
    if ans: print('Matched {0} {1}'.format(first, last))
    else: print('Not matched')
    tcnt -= 1

main()
