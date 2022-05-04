"""
networkx学习
"""
import networkx as nx
"""
G = nx.Graph()

G.add_node(1)

G.add_nodes_from([2,3])

G.add_nodes_from([
    (4,{"color":"red"}),
    (5,{"color":"green"}),
])

H = nx.path_graph(10)

print("H")
print(H.nodes)

#G.add_nodes_from(H)
G.add_node(H)

print("G")
print(list(list(G.nodes)[-1].nodes))

G.add_edge(1,2)
#e = (2,3)
#G.add_edge(*e)

G.add_edges_from([(1,2),(1,3)])

dict01={"weight":3.15}
G.add_edge(2,3,**{'weight':5.14})

G.add_edges_from(H.edges)

print('edge')
print(G.edges)
print('-----------------------------------------')
#清除加入的所有边
G.clear()

#增加新的边
G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")
G.add_nodes_from("spam")
G.add_edge(3,'m')
print("nodes")
print(G.nodes)
print("edges")
print(G.edges)
print("打印点的数量")
print(G.number_of_nodes())
print("打印边的数量")
print(G.number_of_edges())
#边的相邻关系
DG=nx.DiGraph()
DG.add_edge(2,1)
DG.add_edge(1,3)
DG.add_edge(2,4)
DG.add_edge(1,2)
assert list(DG.successors(2)) == [1,4]
assert list(DG.edges) == [(2,1),(2,4),(1,3),(1,2)]
print("打印与1连接的点")
print(list(G.adj[1]))
print("打印与3相连点的数量")
print(G.degree[3])
print(G.edges([1,'m']))
print(G.degree([2,3]))
#删除图中元素
G.remove_node(2)
G.remove_nodes_from("spam")
print(list(G.nodes))
G.remove_edge(1,3)

G.add_edge(1,2)
print(G.edges)
H = nx.DiGraph(G)
print(list(H.edges))
edgelist = [(0,1),(1,2),(2,3)]
H = nx.Graph(edgelist)

G = nx.Graph([(1,2,{"color":"yellow"})])
print(G[1])
print(G[1][2])
print(G.edges[1,2])

G.add_edge(1,3)
G[1][3]['color']='blue'
G.edges[1,2]['color']='red'
print(G.edges[1,2])

FG = nx.Graph()
FG.add_weighted_edges_from([(1,2,0.125),(2,4,1.2),(3,4,0.375)])
for n,nbrs in FG.adj.items():
    print(n)
    for nbr,eattr in nbrs.items():
        wt=eattr['weight']
        print(nbr)
        print(f"({n},{nbr},{wt})")


for (u,v,wt) in FG.edges.data('weight'):
    if wt < 0.5:
        print(f"({u},{v},{wt})")


G=nx.Graph(day="Friday")
print(G.graph)

G.graph['day']="Monday"
print(G.graph)
print()

G.add_node(1,time='1pm')
G.add_nodes_from([(2,{'time':2}),(4,{"time":4})])
print(G.nodes[4])
G.nodes[1]['room']=714
print(G.nodes.data())

G.add_edge(1,2,weight=4.7)
G.add_edges_from([(3,4),(4,5)],color='red')
G.add_edges_from([(1,2,{'color':'blue'}),(2,3,{'weight':8})])
print(G[1][2]['weight'])
print(G.edges[3,4]['color'])

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5),(3,1,0.75)])
print(DG.out_degree(1,weight='weight'))
print(DG.degree(1,weight='weight'))

H = nx.Graph(DG)
print(H.degree(1,weight='weight'))
print(H[1][2])

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1,2,0.75),(1,2,0.5),(2,3,0.5)])
print(dict(MG.degree(weight='weight')))
GG=nx.Graph(day="Friday")

for n,nbrs in MG.adjacency():
    for nbr,edict in nbrs.items():
        minvalue = min([d['weight'] for d in edict.values()])
        print(n,nbr)
        GG.add_edge(n,nbr,weight=minvalue)

print(nx.shortest_path(GG,1,3))
"""
G=nx.Graph()
G.add_edges_from([(1,2),(1,3)])
G.add_node('spam')
print(list(nx.connected_components(G)))

for n,d in G.degree():
    print(d)

import matplotlib.pyplot as plt

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G,with_labels=True,font_wight='bold')
subax2=plt.subplot(122)
nx.draw_shell(G,nlist=[range(5,10),range(5)],with_labels=True,font_weight='bold')
plt.show()

