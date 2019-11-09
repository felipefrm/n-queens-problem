from igraph import*

def bronKerbosh(cliqueMax, g, r, p, x):

    if len(p) == 0 and len(x) == 0:
        cliqueMax.append(r)
        return

    # print(p)
    # print(x)
    # print(g.maxdegree(list(set().union(p, x))))
    u = g.maxdegree(list(set().union(p, x)))

    for v in list(set(p) - set(g.neighbors(u))):
        r.append(v)
        bronKerbosh(cliqueMax, g, r, list(set(p) & set(g.neighbors(v))), list(set(x) & set(g.neighbors(v))))
        p = list(set(p) - set(g.neighbors(v)))
        x.append(v)
