"""
用于存放功能使用的各种函数
"""
import networkx as nx

def transform_dict_to_list(dict_target):
    """
    Transporting {(a,b):0,(c,d):0} to [(a,b,0),(a,b,0)]
    :param dict_target: a dictionary like {(a,b):0,(c,d):0}
    :return list_result: a list like [(a,b,0),(a,b,0)]
    """
    list_result = []
    list_element = []
    for i in dict_target:
        list_element.append(i[0])
        list_element.append(i[1])
        list_element.append(dict_target[i])
        list_result.append(tuple(list_element))
        list_element = []
    return list_result

def optimize_dict_target(dic_target,dic_optimization,i):
    """
    Take in or change the elements in dic_target according to dic_optimization
    :param dic_target: The dictionary of optimization transportation network
    :param dic_optimization: # the dictionary of road optimization plan
    :param i: the position of ith element
    :return: a changed dic_target
    """
    dic_result = dic_target
    dic_result[i]=dic_optimization[i]
    return dic_result

def transform_to_dict(list_resource):
    """
    Transporting [(1,2,3),(4,5,6)] to {(1,2):0,(4,5):0,(2,1):0,(5,4):0}
    :param list_resource: A list like [(1,2,3),(4,5,6)]
    :return: A dictionary like {(1,2):0,(4,5):0,(2,1):0,(5,4):0}
    """
    result_dict={}
    # Transport (1,2,3) to (1,2) and take (1,2) into result_dict.
    for i in list_resource:
        midd_list = i[:-1]
        midd_value=tuple(midd_list)
        result_dict[midd_value]=0
    # Transport (1,2,3) to (2,1) and take (2,1) into result_dict.
    for i in list_resource:
        midd_list = i[:-1][::-1]
        midd_value=tuple(midd_list)
        result_dict[midd_value] = 0
    return result_dict

def get_shortest_road(G,s,t):
    """
    Finding the shortest way from s-point to t-point in G-net.
    :param G: The given network.
    :param s: Starting point
    :param t: Ending point
    :return: A list like [(s,a),(a,b),(b,t)]
    """
    wayMinWpath = []
    # Finding the shortest way.
    minWPath = nx.dijkstra_path(G,source=s,target=t)
    # Change the shortest way into a list.
    tuple_two_point = (None, None)
    for i in range(len(minWPath)):
        l=len(minWPath)
        if i < l-1:
            tuple_two_point = (minWPath[i],minWPath[i+1])
            wayMinWpath.append(tuple_two_point)
        else:
            break
    return wayMinWpath

def source_target_maker(source_list,target_list):
    """
    Get starting point and endpoint in source_list and target_list.
    :param source_list: The list of starting point.
    :param target_list: The list of starting point.
    :return: (start_point,End_point)
    """
    source_target=(None,None)
    import random
    while True:
        start_point = random.choice(source_list)
        end_point = random.choice(target_list)
        if start_point == end_point:
            continue
        else:
            source_target = (start_point,end_point)
            break
    return source_target

def write_to_database(optimization,way,length):
    """
    Write road and length into the shortest_road table in the road database.
    :param way: the list of road like s to t: [(s,a),(a,b),(b,t)]
    :param length: the length of the road.
    :return: None
    """
    import json
    target_way = json.dumps(way)
    target_optimization = json.dumps(optimization)
    import pymysql
    # link to database
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # Generate cursor object (operate database, execute sql statement)
    cur = db.cursor()
    # Perform various multi-database write operations
    try:
        sql = "insert into shortest_road (optimization,way,length) values(%s,%s,%s);"
        exe = [(target_optimization,target_way,length)]
        cur.executemany(sql, exe)  # executemany
        db.commit()
    except Exception as e:
        db.rollback()  # Rollback
        print(e)
    # close cursor and database
    cur.close()
    db.close()

def read_i_optimization(i):
    """
        Read the record by id =i from shortest_road table.
        :param i: id
        :return: the list of shortest_road from s to t.
        """
    import json
    import pymysql
    # Link to database
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # Generate cursor object (operate database, execute sql statement)
    cur = db.cursor()
    # Find by id
    sql = "select optimization from shortest_road where id=%s;"
    cur.execute(sql, [i])
    # Get result
    all_row = cur.fetchall()
    try:
        result = json.loads(all_row[0][0])
    except:
        return "数据读取完成"
    cur.close()
    db.close()
    return tuple(result)

def read_i_length(i):
    """
    Get the length record in shortest_road table.
    :param i: id = i
    :return: length int
    """
    import pymysql
    # Link to databases
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # Generate cursor object (operate database, execute sql statement)
    cur = db.cursor()
    # find by id
    sql = "select length from shortest_road where id=%s;"
    cur.execute(sql, [i])
    # get result
    length = cur.fetchall()[0][0]
    cur.close()
    db.close()
    return length

def read_i_way(i):
    """
    Get road record in shortest_road table by id = i
    :param i: id
    :return: the list of way
    """
    import json
    import pymysql
    # Link to database
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # Generate cursor object (operate database, execute sql statement)
    cur = db.cursor()
    # find by id
    sql = "select way from shortest_road where id=%s;"
    cur.execute(sql,[i])
    # get result
    all_row = cur.fetchall()
    result = json.loads(all_row[0][0])
    # close
    cur.close()
    db.close()
    # Transport [[],[],[]] into [(),(),()]
    result_01 =[]
    for i in result:
        element = tuple(i)
        result_01.append(element)
    return result_01

def calculate_iway_road_use(list_need_calculate,result_dict):
    """
    Count the number of times the path has been used
    :param list_need_calculate: the name list of road needed to count
    :param result_dict: a dictionary record name and number
    :return:
    """
    for i in list_need_calculate:
        result_dict[i]+=1

def delete_record():
    """
    clear database
    :return: None
    """
    import pymysql.cursors
    # link to database
    con = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         database='road',
                         charset='utf8')
    # Generate cursor object (operate database, execute sql statement)
    cursor_01 = con.cursor()
    # delete record
    sql = "delete from shortest_road;"
    cursor_01.execute(sql)
    con.commit()
    # close cursor
    cursor_01.close()
    #Generate a new cursor object
    cursor_02 = con.cursor()
    #change id to 1
    sql = "alter table shortest_road AUTO_INCREMENT = 1;"
    cursor_02.execute(sql)
    con.commit()
    cursor_02.close()
    con.close()
