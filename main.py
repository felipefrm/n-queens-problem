# -*- coding: utf-8 -*-
from igraph import *
from bronKerbosh import bronKerbosh
import sys

n = int(sys.argv[1])
g = Graph()
g.add_vertices(n*n)

for i in range(n*n):
    for j in range(n*n):
        if i != j and ((j-i) % n == 0 or ((j-i) % (n+1) == 0 and abs(i//n - j//n)*(n+1)+i == j) or ((j-i) % (n-1) == 0 and abs(i//n - j//n)*(n-1)+i == j) or i//n == j//n):
            g.add_edge(g.vs[i].index, g.vs[j].index)

cliqueMax = []
bronKerbosh(n, cliqueMax, g.simplify().complementer().simplify(), list(), list(g.vs.indices), list())

tab = [[x for x in range(n)] for y in range(n)]

# print(tab)
print("\n{} soluções distintas para o problema das {} rainhas foram encontradas.".format(len(cliqueMax), n))

while (True):
    try:
        op = int(input('\n[0] Fechar programa\n[1] Listar todas as soluções encontradas\n>>> '))
    except NameError:
        print("\nDigite uma das opções acima.")
    else:
        if op == 1:
            for clique in cliqueMax:
                print("{}. {}".format(cliqueMax.index(clique), clique))

            op = int(input("\nDeseja ver alguma destas soluções no tabuleiro?\n[0] Não, fechar programa \n[1] Sim\n>>> "))

            if op == 0:
                break

            else:
                op = int(input("\nQual solução? 0 a {}: ".format(len(cliqueMax))))
                for i in range(n):
                    for j in range(n):
                        if i+j*n in cliqueMax[op]:
                            tab[i][j] = '♛'
                        else:
                            tab[i][j] = '○'

            print("")
            for i in range(n):
                for j in range(n):
                    print("{} ".format(tab[i][j])),
                print("")
            print("")
            break


        elif op == 0:
            print("\nPrograma finalizado.")
            break

        else:
            print("\nDigite uma das opções acima.")
