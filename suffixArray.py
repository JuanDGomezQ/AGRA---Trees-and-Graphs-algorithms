from sys import stdin

def build(text):
    text = text + "$"
    ans = []
    pos = 1
    for i in range(len(text)):
        if text[i:][0] == " ": pos += 1
        else:
            newtext = text[i:] + str(pos)
            ans.append(newtext)
    ans.sort()
    #print(ans)
    #print(len(ans))
    return ans

def binsearch(A, x):
    ans,N= True,len(A)-1
    lenx = len(x)
    if N!=0:
        low,hi = 0,N
        while low+1!=hi:
            mid = low+((hi-low)>>1)
            assert low<mid<hi
            if A[mid]<=x: low = mid
            else: hi = mid
        #print("hi",hi)
        #if len(A) <= hi: return False,0
        #if len(A[hi]) < lenx: return False,0
        for i in range(lenx):
            if A[hi][i] != x[i]:
                return(False,None)
        return ans, A[hi][-1]

def solve(ar,p):
    ans,pos = binsearch(ar,p)
    if ans == False:
        print("n")
    else:
        print(pos)

def main():
    n,q = map(int,stdin.readline().split())
    while n != 0 and q != 0:
        volum = ""
        texts = []
        for i in range(n):
            v = stdin.readline().strip()
            if i != 0:
                v = " " + v
            volum = volum + v 
        for j in range(q):
            t = stdin.readline().strip()
            texts.append(t)
        #print(volum)
        ar = build(volum)
        for w in texts:
            solve(ar,w)
        n,q = map(int,stdin.readline().split())
main()