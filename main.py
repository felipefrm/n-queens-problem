from igraph import*
from bronKerbosh import bronKerbosh
import sys

n = int(sys.argv[1])
g = Graph()
g.add_vertices(n*n)
# for i in range(n*n):
#     g.add_vertex(i)
# for i in range(n*n):
#     for j in range(n*n):
#         if ((abs(j-i))%n == abs(i-j)/9 and abs(i-j) <= 9 and i!=j)or (abs(j-i))%n == 0 and i!=j:
#             g.add_edge(g.vs[i].index,g.vs[j].index)
#         elif abs(i-j) <= n and (i+(i%n))%n == (j+(j%n))%n and i!= j:
#             g.add_edge(g.vs[i].index,g.vs[j].index)
# plot(g)
# print(str(len(g.neighbors(g.vs[0].index))))

# g.complementer().simplify()

for i in range(n*n):
    for j in range(n*n):
        if i != j and ((j-i) % n == 0 or (j-i) % (n+1) == 0 or (j-i) % (n-1) == 0 or i//n == j//n):
            g.add_edge(g.vs[i].index, g.vs[j].index)

# plot(g)
for v in range(n*n):
    print(len(g.simplify().neighbors(v)))
# plot(g.complementer().simplify())
cliqueMax = []
bronKerbosh(cliqueMax, g.complementer().simplify(), list(), list(g.vs.indices), list())
# print(cliqueMax)
print(len(cliqueMax))
