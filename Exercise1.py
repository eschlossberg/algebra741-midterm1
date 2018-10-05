from SymmetricGroup import SymmetricGroup
import networkx as nx
import matplotlib.pyplot as plt

s = SymmetricGroup(5)
R = []
G = nx.Graph()
for x in s.elements:
    G.add_node(x)
    for y in s.elements:
        if x*y == y*x:
            R.append((x, y))
            G.add_edge(x, y)
print(nx.number_connected_components(G))
nx.draw(G)
plt.draw()
plt.show()
