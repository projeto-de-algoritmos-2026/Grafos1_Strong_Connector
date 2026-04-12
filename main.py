from node import *
from dfs_visit import DFS_visit
import graph_ops as ops
import vals as dbg

def main():
    a1 = Node("A1", 0, 0)
    a2 = Node("A2", 0, 0)
    a3 = Node("A3", 0, 0)
    b1 = Node("B1", 0, 0)
    b2 = Node("B2", 0, 0)
    b3 = Node("B3", 0, 0)
    c1 = Node("C1", 0, 0)
    c2 = Node("C2", 0, 0)
    c3 = Node("C3", 0, 0)

    a1.connect(a2)
    a2.connect(a3, b3)
    a3.connect(a1)

    b1.connect(b2)
    b2.connect(b3)
    b3.connect(b1)

    c1.connect(c2)
    c2.connect(c3)
    c3.connect(c1, b2)

    g = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    gi = ops.invert(g)

    if(dbg.debug):
        print(f"{DFS_visit(gi).name} está em um componente sink")

    gp = ops.minus(g, gm)




if __name__ == "__main__":
    main()
