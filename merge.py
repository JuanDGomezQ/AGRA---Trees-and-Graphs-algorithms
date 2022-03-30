MAX = 100000
AUX = [ None for _ in range(MAX) ]

def mergesort(A, low, hi):
  assert 0 <= low <= hi <= len(A)
  if low+1<hi:
    mid = low+((hi-low)>>1)    # mid = (low+hi)//2
    mergesort(A, low, mid)
    mergesort(A, mid, hi)
    merge(A, low, mid, hi)
inversions = 0
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

Array = [2,1]
mergesort(Array,0,2)
print(inversions)