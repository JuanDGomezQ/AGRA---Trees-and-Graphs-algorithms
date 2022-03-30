"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin
import math

estados = 1
rutas,rieles = 0,0

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the numnber of components"""
    return self.__ccount
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1
      self.__ccount -= 1

def kruskal(graph, lenv,r):
  global estados,rutas,rieles
  ans = list()
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans.append((u, v, d))
      if(r<d):
          estados +=1
          rieles += d
      else:
          rutas += d
      df.union(u, v)
    i += 1
  assert df.ccount()==1
  assert df.csize(df.find(0))==lenv
  return ans

def main():
    global estados,rutas,rieles
    c = stdin.readline().split()
    cases = int(c[0])
    for i in range(cases):
        n,r = map(int,stdin.readline().split())
        g,G = [list() for _ in range(n)],[]
        rutas = 0
        rieles = 0
        estados = 1
        for m in range(n):
            x,y =map(int,stdin.readline().split())
            g[m].append(x)
            g[m].append(y)
        for j in range(len(g)):
            x1 = g[j][0]
            y1 = g[j][1]
            for k in range(j+1,n):
                x2 = g[k][0]
                y2 = g[k][1]
                dist =  math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                G.append([j,k,dist])
        kruskal(G,n,r)
        print("case #{}:".format(i + 1),estados,int(round(rutas)),int(round(rieles)))


main()