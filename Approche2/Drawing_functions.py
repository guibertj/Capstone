import matplotlib.pyplot as plt
import numpy as np

def draw_paris_street(fig, ax):
    ax.set_xlim(0, 11)
    ax.set_ylim(-5, 5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    # Dessiner la route
    road = plt.Rectangle((0, -3), 11, 6, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(road)
    
    # Dessiner les trottoirs
    sidewalk_top = plt.Rectangle((0, 3), 11, 2, edgecolor='black', facecolor='none', linewidth=2)
    sidewalk_bottom = plt.Rectangle((0, -5), 11, 2, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(sidewalk_top)
    ax.add_patch(sidewalk_bottom)

def draw_graph(fig, ax, G):
    # Afficher le maillage
    for x, y in G.nodes():
        ax.plot(x, y, 'bo', markersize=5)
    # Affiches les arrêtes
    for (x1, y1), (x2, y2) in G.edges():
        ax.annotate("",
                    xy=(x2, y2), xycoords='data',
                    xytext=(x1, y1), textcoords='data',
                    arrowprops=dict(arrowstyle="->", color='b', lw=1.5))

def draw_chemin(fig, ax, G, chemin):
    vertices = list(G.nodes())
    for i in range(len(chemin)-1):
        (x1, y1) = vertices[chemin[i]]
        (x2, y2) = vertices[chemin[i+1]]
        ax.annotate("",
                        xy=(x2, y2), xycoords='data',
                        xytext=(x1, y1), textcoords='data',
                        arrowprops=dict(arrowstyle="->", color='r', lw=1.5))