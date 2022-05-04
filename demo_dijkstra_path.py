"""
无向图有权图的最短路径问题
networkx
Demo of shortest path with Networkx
"""
import networkx as nx
import matplotlib.pyplot as plt

G2 = nx.Graph() #创建空的无向量图
G2.add_weighted_edges_from([(1,2,2),(1,3,8),(1,4,1),
                            (2,3,6),(2,5,1),(3,4,7),
                            (3,5,5),(3,6,1),(3,7,2),
                            (4,7,9),(5,6,3),(5,8,2),
                            (5,9,9),(6,7,4),(6,9,6),
                            (7,9,3),(7,10,1),(8,9,7),
                            (8,11,9),(9,10,1),(9,11,2),
                            (10,11,4)])#向图中添加多条赋值边

list_source=[1,2,3,4,5,6,7,8,9,10,11]
list_target=[1,2,3,4,5,6,7,8,9,10,11]


def get_shortest_road(G,s,t):
    """
    发现网络中起点s与终点t之间的最短路径
    :param G: 目标网络
    :param s: 起点
    :param t: 终点
    :return: 返回值为一个列表,元素是包含各段起点和终点的2元量表
    """
    wayMinWpath = []
    #两个指定顶点之间的最短加权路径
    minWPath_v1_v11 = nx.dijkstra_path(G,source=s,target=t)
    #将其转化为路径元祖的格式
    a = (None, None)
    for i in range(len(minWPath_v1_v11)):
        l=len(minWPath_v1_v11)
        if i < l-1:
            a = (minWPath_v1_v11[i],minWPath_v1_v11[i+1])
            wayMinWpath.append(a)
        else:
            break
    return wayMinWpath

def source_target_maker(source_list,target_list):
    """
    随机在起点列表和终点列表中选取起点和终点
    :param source_list: 起点池
    :param target_list: 终点池
    :return: (起点,终点)
    """
    soutce_target=(None,None)
    import random
    while True:
        a = random.choice(source_list)
        b = random.choice(target_list)
        # a = source_list
        # b = target_list
        if a == b:
            continue

        else:
            soutce_target = (a,b)
            break

    return soutce_target

def write_to_database(way,length):
    import json
    target_way = json.dumps(way)
    import pymysql
    # 链接数据库
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # 生成游标对象(操作数据库,执行sql语句)
    cur = db.cursor()
    # 执行各种多数据库的写操作
    try:
        sql = "insert into shortest_road (way,length) values(%s,%s);"
        exe = [(target_way,length)]
        cur.executemany(sql, exe)  # executemany 多次执行sql语句
        db.commit()
    except Exception as e:
        db.rollback()  # 事物回滚
        print(e)
    # 关闭游标和数据库链接
    cur.close()
    db.close()

for i in range(100):
    lm = source_target_maker(list_target,list_source)
    way = get_shortest_road(G2,lm[0],lm[1])
    length = lMinWPath_v1_v11 = nx.dijkstra_path_length(G2,lm[0],lm[1])
    write_to_database(way,length)







