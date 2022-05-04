"""
Demo of shortest path with Networkx
"""
import networkx as nx
G2 = nx.Graph()
from demo_data import *
from demo_function import *
from time import *

def path_maker(dic_target,dic_optimization, times):
    """
    According to given network dic_target and optimization plan dic_optimization
    perform multiple simulations
    :param dic_target: given_network
    :param dic_optimization: optimization plan
    :param times: the times of simulation
    :return: None
    """
    for i in dic_optimization:
        G2.clear()
        optimization = i
        # Deep copy to ensure that the route returns
        # to the original state after each optimization
        b=dic_target.copy()
        a = optimize_dict_target(b,dic_optimization,i)
        list_a = transform_dict_to_list(a)
        G2.add_weighted_edges_from(list_a)
        for l in range(times):
            lm = source_target_maker(list_source, list_target)
            way = get_shortest_road(G2, lm[0], lm[1])
            length = nx.dijkstra_path_length(G2, lm[0], lm[1])
            write_to_database(optimization, way, length)

def calculate_way(dic_target,dic_optimization):
    """
    Calculate the usage frequency of each channel under each optimization mode
    :return:None
    """
    file_object = open('record_road_used_times.txt', 'a')
    index = 1
    while True:
        optimization = read_i_optimization(index)
        print(optimization)
        file_object.write(str(optimization)+'\n')
        # Deep copy to ensure that the route returns
        # to the original state after each optimization
        dic_calculated = dic_target.copy()
        dic_opt = optimize_dict_target(dic_calculated,dic_optimization,optimization)
        list_opt = transform_dict_to_list(dic_opt)
        dict01 = transform_to_dict(list_opt)
        while True:
            data = read_i_way(index)
            calculate_iway_road_use(data, dict01)
            index += 1
            if optimization != read_i_optimization(index):
                for item in dict01:
                    print(item, dict01[item])
                    file_object.write(str(item)+str(dict01[item])+'\n')
                break

def caculate_time():
    """
    Calculate the average duration of each optimization mode
    :return:None
    """
    file_object = open('record_length_need_time.txt','a')
    index = 1
    a = 0
    while True:
        optimization = read_i_optimization(index)
        print(optimization)
        sum = 0
        count = 0
        if a == 1:
            break
        while True:
            try:
                data = read_i_length(index)
            except:
                print("aa")
                a = 1
                break
            sum += data
            count += 1
            index += 1
            if optimization != read_i_optimization(index):
                data = str(sum//count)
                file_object.write(data+'\n')
                #return sum // count
                print("The average duration is %d minutes" % (sum // count))
                break
    file_object.close()

def calculate_variance(groups_calculation,simulation_times_list):
    """
    Calculate multiple results under a certain number of simulations to calculate variance
    :param groups_calculation: How many groups of results do you need?
    :param simulation_times_list: Store a list of different simulation times
    :return: None
    """
    file_object02 = open('record_time.txt', 'a')
    for simulation_times in simulation_times_list:
        time_begin = time()
        data = str(simulation_times)
        file_object02.write(data + '\n')
        print(simulation_times)
        for i in range(groups_calculation):
            path_maker(dic_targetG,dic_optimization_1,simulation_times)
            caculate_time()
            delete_record()
        time_end = time()
        time_need = str(round(time_end - time_begin, 3))
        print(time_need)
        file_object02.write(time_need + '\n')
        file_object02.write('\n')
    file_object02.close()

#生成路径时请注释掉路径统计,统计路径时请注释掉生成路径

#生成路径
path_maker(dic_targetG_c,dic_optimization_1,100)

#统计每种方案中每条路径使用频率
#calculate_way(dic_targetG_c,dic_optimization_1)

#统计每种方案的平均时长
#caculate_time()

#计算40次为,cishu_list中各种模拟次数的模拟值,此函数独立运行,无需先运行path_maker
#calculate_variance(5,times_list)

#清空数据库记录,如果需要查看时间分布,请备注本行
delete_record()

