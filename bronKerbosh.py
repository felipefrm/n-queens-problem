from igraph import*

def bronKerbosh(n, cliqueMax, g, r, p, x):

    if len(p) == 0 and len(x) == 0:
        if len(r) == n:
            cliqueMax.append(r)
        return

    u = escolheVertice(g, list(set().union(p, x)))

    for v in list(set(p) - set(g.neighbors(u))):
        bronKerbosh(n, cliqueMax, g, r + [v], list(set(p) & set(g.neighbors(v))), list(set(x) & set(g.neighbors(v))))
        p.remove(v)
        x.append(v)

def escolheVertice(g, vertices):
    grau = []
    for v in vertices:
        grau.append(g.degree(v))

    return vertices[grau.index(max(grau))]
