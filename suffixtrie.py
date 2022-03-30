from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**8)

class nodo(object):
    def __init__(self,valor = None,hijos = []):
        self.val = valor
        self.hijos = hijos

class suffixtrie(object):
    def __init__(self,text = ""):
        self.text = text + "$"
        self.n = len(self.text)
        self.trie = nodo()
        for i in range(self.n):
            self.build(self.trie,i)

    def build(self,node,sufind):
        if sufind < self.n:
            bandera = False
            suffix = self.text[sufind]
            pos = None
            for i in range(len(node.hijos)):
                if node.hijos[i] == suffix:
                    bandera = True
                    pos = i
                    break
            if bandera == False:
                nuevo = nodo()
                nuevo.val = suffix
                node.hijos.append(nuevo)
                self.build( node.hijos[-1],sufind + 1)
            else:
                self.build(node.hijos[pos],sufind + 1)

def search(pat,node,indi):
    bol = False
    pos = 0
    if indi == len(pat):
        return True
    else:
        for i in range(len(node.hijos)):
            if pat[indi] == node.hijos[i].val:
                bol = True
                pos = i
                break
        if bol:
            ans = search(pat,node.hijos[i],indi+1)
        else:
            return False
    return ans

def solve(triee,w):   
    ans = search(w,triee.trie,0)


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
        triee = suffixtrie(volum)
        for w in texts:
            solve(triee,w)
        n,q = map(int,stdin.readline().split())
main()

"""
t = "aba"
triee = suffixtrie(t)
print(triee.trie.hijos[3].val)
p = search("za",triee.trie,0)
print(p)"""