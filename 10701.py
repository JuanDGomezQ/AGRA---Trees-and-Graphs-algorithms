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
    postorder.append(pre[0]) 

def main():
    global postorder
    postorder = []
    preorder = []
    x = int(stdin.readline())
    while x != 0:
        aux = stdin.readline().split()
        n = int(aux[0])
        preorder = aux[1]
        inorder = aux[2]
        post(inorder, preorder, n)
        string1 = ''.join(postorder)
        print(string1)
        postorder = []
        x -= 1

main()