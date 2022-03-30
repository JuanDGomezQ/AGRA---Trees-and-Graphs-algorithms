from sys import stdin
import sys
sys.setrecursionlimit(10000)
def create(acum, comp):
    global k, band
    while k < len(arb) and not arb[k].isdigit() and arb[k] != '-':
        k += 1
    j = k + 1
    while j < len(arb) and arb[j].isdigit():
        j += 1
    val = int(arb[k:j])
    k = j
    if(j < len(arb) and arb[j] == '(' and arb[j] != ')'):
        acum2 = acum + val
        x = create(acum2, comp)
        acum2 = acum + val
        y = create(acum2, comp)
        if (len(y) == 1 and comp == acum2 and x == y == [0]): band = True
        tree = [val, x, y, acum2 ]
    else:
        tree = [val]
    return tree
 
def leerNum():
    global i
    while  i < len(line) and not (line[i].isdigit()) and line[i] != '-':
        i+=1
    j = i +1
    while j < len(line) and(line[j].isdigit()):
        j += 1
    val = int(line[i:j])
    i = j
    return val
     
def leerArbol():
    global i
    j = i
    parIzq = 0
    parDer = 1
    i += 1
    while(i  < len(line) and parIzq != parDer):
        if(line[i] == '('): parDer += 1
        elif(line[i] == ')'): parIzq += 1
        i += 1
    val = line[j:i]
    return val
     
def main():
    global i, line, k, arb, band
    i = 0
    line = ''.join(''.join(stdin.readlines()).split())
    tam = len(line)
    while i < tam:
        if(i + 1 < tam and line[i] == '(' and line[i + 1] == ')'):
            line = line[0:i +1] + '0' + line[i +1: tam]
            tam += 1
        i += 1
    i = 0
    print(line)
    while(i < len(line)):
        k = 0
        band = False
        comp = leerNum()
        print(comp)
        arb = leerArbol()
        print(arb)
        create(0, comp)
        print("-")
main()