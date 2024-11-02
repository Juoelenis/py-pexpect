import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 7), (3, 8), (5, 8), (7, 9), (8, 9), (6, 10), (9, 10)])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges())
nx.draw_networkx_labels(G, pos)

plt.show()
