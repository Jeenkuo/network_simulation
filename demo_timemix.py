"""
生成时间矩阵
"""
from demo_function import *
from demo_data import *
import numpy as np
import networkx as nx

G3 = nx.Graph()
def network_maker(G,dict):
    G.clear()
    dict_copy = dict.copy()
    dict_to_list = transform_dict_to_list(dict_copy)
    G.add_weighted_edges_from(dict_to_list)

def calculate_shortest_time(G,start,end):
    return nx.dijkstra_path_length(G,start,end)

def matrix_maker(i,j):
    return np.zeros((i,j))

a = matrix_maker(31,31)

network_maker(G3,dic_targetG_c)
for i in range(0,31):
    s = list_city[i]
    #print(i)
    for j in range(i+1,31):
        e = list_city[j]
        #print(j)
        #print(s,e)
        time = calculate_shortest_time(G3,s,e)
        a[i][j]=time


file_object = open('time_matrix.txt', 'w')
for i in range(0,31):
    file_object.write('\n')
    for j in range(0,31):
        file_object.write(str(a[i][j])+',')



