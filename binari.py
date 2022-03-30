def binsearch(A, x):
  print(x)
  ans,N = 0,len(A)
  print(len(A))
  if N!=0:
    low,hi = 0,N
    while low+1!=hi:
      mid = low+((hi-low)>>1)
      assert low<mid<hi
      if A[mid]<=x: low = mid
      else: hi = mid
      print(mid)
      print(low,hi)
    print(low)
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


A = []
print(binsearch(A,3))
