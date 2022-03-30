"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""
from sys import stdin

class state(object):
    def __init__(self):
        self.nxt = {}
        self.ln = 0
        self.link = 0

st = [state() for _ in range(200000)]
sz = 0
last = 0

def init():
    global st,sz,last
    st[0].ln = 0
    st[0].link = -1
    sz += 1
    last = 0

def extend(c):
    global st,sz,last
    cur = sz + 1
    sz += 1
    st[cur].ln = st[last].ln + 1
    p = last
    while ((p != -1) and not( st[p].nxt.get(c) != None)):
        st[p].nxt[c] = cur
        p = st[p].link
    if p == -1:
        st[cur].link = 0
    else:
        q = st[p].nxt[c]
        if st[p].ln + 1 == st[q].ln:
            st[cur].link = q
        else:
            clone = sz + 1
            sz += 1
            st[clone].ln = st[p].ln + 1
            st[clone].nxt = st[q].nxt
            st[clone].link = st[q].link
            while p != -1 and st[p].nxt[c] == q:
                st[p].nxt[c] = clone
                p = st[p].link
            st[q].link = st[cur].link = clone
    last = cur

def search(pat):
    global st
    i = 0
    for j in range(len(pat)):
        if st[i].nxt.get(pat[j]) != None:
            i = st[i].nxt[pat[j]]
        else: return False
    return True

def main():
    global st,sz,last
    n,q = map(int,stdin.readline().split())
    init()
    while n != 0 and q != 0:
        volum = []
        texts = []
        for i in range(n):
            v = stdin.readline().strip()
            volum.append(v)
        for j in range(q):
            t = stdin.readline().strip()
            texts.append(t)
       # print("volum:",volum)
        for w in texts:
            for v in volum:
                for i in range(len(v)):
                    extend(v[i])
            ans = search(w)
            if ans:
                pass
            
        n,q = map(int,stdin.readline().split())
main()
