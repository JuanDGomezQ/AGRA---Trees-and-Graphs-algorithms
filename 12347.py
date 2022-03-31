from sys import stdin

def post(ino, pre, n):
    if pre[0] in ino:
        raiz = ino.index(pre[0])
    if raiz != 0:
        post(ino[:raiz],  
            pre[1:raiz + 1],  
            len(ino[:raiz])) 
      
    if raiz != n - 1:
        post(ino[raiz + 1:],   
            pre[raiz + 1:],  
            len(ino[raiz + 1:])) 
    print(pre[0]) 

def solve(preorder):
    inorder = preorder.copy()
    inorder.sort()
    return post(inorder, preorder, len(preorder))

def main():
    preorder = []
    x = stdin.readline()
    while x:
        preorder.append(int(x))
        x = stdin.readline()
    solve(preorder)

main()