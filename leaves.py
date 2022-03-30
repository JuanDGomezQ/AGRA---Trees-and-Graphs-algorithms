"""
    Estudiante: Juan David Gomez
    Codigo: 8939024

    Nota: La solucion a este problema se trabajo en clase.
"""

from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**8)

from sys import stdin

def parse(td):
	ans = None
	if td[-1] == -1:
		ans = list(); td.pop()
	else:
		ans = [td.pop(), parse(td), parse(td) ]
	return ans

def cnt_leaves(tree,col,d):
	if len(tree) != 0:
		if col not in d: d[col] = 0
		d[col] += tree[0]
		cnt_leaves(tree[1], col-1, d)
		cnt_leaves(tree[2], col+1, d)

def solve(td):
	ans = list()
	td.reverse()
	while len(td) != 0:
		tree = parse(td)
		d = dict() ; cnt_leaves(tree,0,d)
		l = [ (i, d[i]) for i in d ]; l.sort()
		l = [v for i, v in l]
		ans.append(l)
	return ans

def main():
    td = list(map(int,stdin.read().split()))
    ans = solve(td)
    ans.pop()
    it = 1
    for i in range(0,len(ans)):
        it = i + 1
        print("Case "+ str(it)+":")
        print(*ans[i])
        print("")
main()