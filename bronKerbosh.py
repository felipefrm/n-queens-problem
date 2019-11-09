from igraph import*

def bronKerbosh(cliqueMax, g, r, p, x):

    if len(p) == 0 and len(x) == 0:
        if len(r) == 8:
        # print("achei clique maxima")
            cliqueMax.append(r)
        return

    # print("P u X: {}".format(list(set().union(p, x))))
    u = escolheVertice(g, list(set().union(p, x)))

    # u = g.maxdegree(list(set().union(p, x)))
    # print("escolhido: ", u)

    # print("P\N({}) = {}".format(u, str(list(set(p) - set(g.neighbors(u))))))
    for v in list(set(p) - set(g.neighbors(u))):
        # print("v: {}".format(v))
        # print("r = {} p = {} x = {}".format(r + [v], list(set(p) & set(g.neighbors(v))), list(set(x) & set(g.neighbors(v)))))
        bronKerbosh(cliqueMax, g, r + [v], list(set(p) & set(g.neighbors(v))), list(set(x) & set(g.neighbors(v))))
        # print("p = {} - {}".format(list(set(p)), list(set(g.neighbors(v)))))
        p.remove(v)
        x.append(v)
        # print("p = {} x = {}".format(p, x))
        # print("fimbk")

def escolheVertice(g, vertices):
    grau = []
    for v in vertices:
        grau.append(g.degree(v))

    return vertices[grau.index(max(grau))]
