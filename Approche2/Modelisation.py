import numpy as np
import networkx as nx

def Maillage():
    n = 11
    m = 5 + 2 + 2

    # Générer et tracer une grille de points sur la route et les trottoirs
    x_points = np.linspace(0.5, 10.5, 11)
    y_points_road = np.linspace(-2, 2, 5)
    y_points_sidewalk = np.linspace(-4.5, -3.5, 2).tolist() + np.linspace(3.5, 4.5, 2).tolist()
    
    points_road = [(x, y) for x in x_points for y in y_points_road]
    points_sidewalk = [(x, y) for x in x_points for y in y_points_sidewalk]
    points = points_road + points_sidewalk

    return points, n, m

def Create_graph(points, n, m):
    # Extraire et enlever les doublons des colonnes
    x_points = np.unique(np.array(points)[:, 0])
    y_points = np.unique(np.array(points)[:, 1])

    # Générer les vertices
    vertices = [tuple([x, y * (-1)**i]) for i, x in enumerate(x_points)\
                for y in y_points]
    num_topo = [k for k in range(len(vertices))]

    G = nx.DiGraph()
    for x, y in vertices:
        G.add_node((x, y))

    for i in range(len(vertices) - 1):
        G.add_edge(vertices[i], vertices[i + 1], weight=1)
        if i < len(points) - m:
            G.add_edge(vertices[i], (vertices[i][0] + 1, vertices[i][1]), weight=1)
    
    return G

def Bellman(G):
    vertices = list(G.nodes())
    n = len(vertices)

    # Initialisation
    father = []
    pi = [float('inf')] * n
    pi[0] = 0
    l = [0] * n
    l_max = 9
    horizontal = True

    # Itération
    for j in range(1, n):
        y = vertices[j]
        C_min = float('inf')
        k_min = -1

        for x in G.predecessors(y):
            k = vertices.index(x)
            
            if horizontal and x[1] == y[1]:
                l[j] = l[k] + 1
                coude = 0
            elif not horizontal and x[1] == y[1]:
                l[j] = 1
                coude = 1
            elif not horizontal and x[1] != y[1]:
                l[j] = 0
                coude = 0
            else:
                l[j] = 0
                coude = 1

            if l[j] == l_max:
                continue

            cout = pi[k] + G[x][y]['weight'] + coude

            if cout <= C_min:
                C_min = cout
                k_min = k
                length = l[j]
        
        horizontal = (vertices[k_min][1] == y[1])

        pi[j] = C_min
        father.append(k_min)
        l[j] = length

    return father

def Chemin_optimal(father): #ajouter le point d'arrivée num_topo
    i = len(father)
    chemin = [i]
    while i != 0:
        i = father[i-1]
        chemin.append(i)
    chemin.reverse()
    return chemin
