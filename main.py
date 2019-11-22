# -*- coding: utf-8 -*-
from igraph import*
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
plot(g)
bronKerbosh(n, cliqueMax, g.simplify().complementer().simplify(), list(), list(g.vs.indices), list())

print("\n{} soluções distintas para o problema das {} rainhas foram encontradas.".format(len(cliqueMax), n))

while (True):
    try:
        op = input('\n[0] Fechar programa\n[1] Listar todas as soluções encontradas\n>>> ')
    except NameError:
        print("\nDigite uma das opções acima.")
    else:
        if op == 1:
            for clique in cliqueMax:
                print("{}. {}".format(cliqueMax.index(clique)+1, clique))
            break

        elif op == 0:
            print("\nPrograma finalizado.")
            break

        else:
            print("\nDigite uma das opções acima.")
