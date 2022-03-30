from sys import stdin

"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""
def automata(word):
    T = [-1 for _ in range(len(word))]
    cnt,pos = 0,1
    while pos < len(word):
        if word[pos] == word[cnt]:
            T[pos] = T[cnt]
        else:
            T[pos] = cnt
            cnt = T[cnt]
            while cnt >= 0 and word[pos] != word[cnt]:
                cnt = T[cnt]
        pos += 1
        cnt += 1
    return T

def KMP(text,word,T):
    n,nw = len(text),len(word)
    aln = [0 for r in range(len(text))]
    k,j,ans = 0,0,1
    while j < n:
        if text[j] == " " and aln[j] == 0:
            ans += 1
            aln[j] = 1
        if word[k]  == text[j]:
            j += 1
            k += 1
            if k == nw:
                return ans
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
    return "n"

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
       # print("volum:",volum)
        for w in texts:
            #print("words:",w)
            print(KMP(volum,w,automata(w)))
        n,q = map(int,stdin.readline().split())
main()
