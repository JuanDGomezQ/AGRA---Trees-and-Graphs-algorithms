"""
    Estudiante: Juan David Gomez
    Codigo: 8939024
"""

from sys import stdin

def main():
    t = map(int,stdin.readline().split())
    for i in range(t):
        ans = 0
        bas = (1<<27) - 1 
        n = map(int,stdin.readline().split())
        for j in range(n):
            string = stdin.readline().strip()
            tmp = 0
            for k in string:
                tmp = tmp | (1<<(ord(k) - ord('a')))
            if (tmp & bas): bas = bas & tmp
            else: ans,bas = ans+1,tmp
        print(str(ans))
main()
