""" Estudiante : Juan David Gomez
    Codigo: 8939024
"""



from sys import stdin
alfa = [0]

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

def solve(n):
    global alfa
    ans = None
    
    r = (binsearch(alfa,n)) #grupo en el que esta
    x = alfa[r] - n #elemento grupo arreglo - entrada
    ans = r - x + (r//10)
    return ans
  
def main():
    global alfa
    for i in range(1,190000):
        alfa.append(i + alfa[i-1])
    tcnt = int(stdin.readline())
    while tcnt!=0:
        print(solve(int(stdin.readline())))
        tcnt -= 1

main()