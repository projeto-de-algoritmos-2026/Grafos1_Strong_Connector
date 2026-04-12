from node import *


# Inversão de grafo
def invert(graph : list[Node]) -> list[Node]:
    g = []
    for n in graph:
        g.append(n.copy_shallow())
    
    
    for i in range(len(g)-1, -1, -1):
        for j in range(len(graph[i].neighbors)-1, -1, -1):
            ind = Node.find_node(graph[i].neighbors[j], graph)
            g[ind].connect(g[i])

    return g        


# Subtração de conjuntos
def minus(g1: list[Node], g2: list[Node]) -> list[Node]:
    g = []
    for n in g1:
        g.append(n.copy_shallow())
    
    for i in range(0, len(g)):
        for neigh in g1[i].neighbors:
            if(Node.find_node(neigh, g2) == -1):
                g[i].connect(neigh)

    for node in g:
        if(Node.find_node(node, g2) != -1):
            g.remove(node)
    return g

def print_graph(graph: list[Node]) -> None:
    for n in graph:
        print(f"{n.name}-> ", end="")
        n.print_vizinhos()