# Introduction to Network Analysis

# Basics of NetworkX

import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
print(G.nodes())
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)]) # add missing points automatycly
G.add_edge("u","w")
print(G.edges())
G.remove_node(2)
print(G.nodes())
G.remove_nodes_from([4,5])
print(G.nodes())
G.remove_edge(1,3)
print(G.edges())
G.remove_edges_from([(1,2),("u","v")])
print(G.edges())
print(G.number_of_nodes(),G.number_of_edges())

# Graph Visualization

G = nx.karate_club_graph()
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")

G.degree()  # node of number - values of friends
G.degree()[33]  # 17
G.degree(33)  # 17

print(G.number_of_nodes(), G.number_of_edges())
print(G.degree(0) is G.degree()[0])

# Random Graphs

# Erdős-Rényi graph

from scipy.stats import bernoulli

bernoulli.rvs(p=0.2)  # give 0 or 1 - like as flip the coin

N = 20
p = 0.2

# create empty Graph
# add all N nodes in the graph
# loop over all pairs
    # add an edge with prob p
'''
G = nx.Graph()
G.add_nodes_from(range(N))
for node1 in G.nodes():
    for node2 in G.nodes():
        if bernoulli.rvs(p=p):
            G.add_edge(node1, node2)
'''

def er_graph(N, p):
    """Generate an ER graph."""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G
G.number_of_nodes()
nx.draw(G)

nx.draw(er_graph(50,0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")

# Plotting the Dregree Distribution

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    #plt.hist(list(G.degree().values()), histtype="step")  # doesn't work
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G = er_graph(50, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.pdf")

G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist11.pdf")

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist3.pdf")

# Descriptive Statistic of Empirical Social Networks
# Adjecency matrix
#https://science.sciencemag.org/content/341/6144/1236498.full

import numpy as np

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))


basic_net_stats(G1)
basic_net_stats(G2)


plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")


# Finding the Largest Connected Component

#nx.connected_component_subgraphs(G1) #Generator object
def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)
gen = connected_component_subgraphs(G1) # nx.connected_component_subgraphs(G1)

g = gen.__next__()

type(g)  # networkx.classes.graph.Graph

g.number_of_nodes()

len(gen.__next__())
len(G1)  # 843

G1.number_of_nodes()  # 843

len(gen.__next__())

G1_LCC = max(connected_component_subgraphs(G1), key=len)
G2_LCC = max(connected_component_subgraphs(G2), key=len)

len(G1_LCC)  # 825
G1_LCC.number_of_nodes()  # 825

len(G1_LCC)  # 810
G1_LCC.number_of_nodes() / G1.number_of_nodes() # 0.978647686327402

G2_LCC.number_of_nodes() / G2.number_of_nodes() # 0.9236031927023945

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")
