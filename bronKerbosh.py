from igraph import*

def bronKerbosh(CliqueMax, g, r, p, x):

    if len(p) == 0 and len(x) == 0:
        cliqueMax.append(r)
        return

    u = g.maxdegree(list(set().union(p, x)))

    for v in list(set(b) - set(g.neighbors(u))):
        bronKerbosh(CliqueMax, g, list(set().union(r, v)), list(set(p) & set(g.neighbors(v))), list(set(x) & set(neighbors(v))))
        p = list(set(p) - set(g.neighbors(v)))
        x = list(set().union(x, v))
