计算网络中各条道路的使用情况步骤"
1.通过list_targetG构建网络结构,list_targetG中的各个元素表示(起点,终点,距离)
2.构架list_source和list_target分别表示随机选择的起点库和终点库,各个点在各个库中出现的比率由该点的多少决定
3.通过dict01=tansform_to_dict(list_targetG)函数构建一个接收计算结果的字典
4.使用for循环:
    4.1使用lm = source_target_maker(list_target,list_source)函数随机生成起点和终点
    4.2使用way = get_shortest_road(G2,lm[0],lm[1])获取最短路径
    4.3使用write_to_database(way,length)函数存入数据库,在进行这一步之前看id是否需要归零
5.使用while循环:
    4.1设置一个计数器用来控制统计范围
    4.2使用data = read_i_data(index)将记录读取出来
    4.3使用calculate_iway_road_use(data,dict01)计算统计结果,并将结果输入dict01
6.使用delete_record()函数清理数据库,并将id归零

7.使用mysql语句:select length,count(*) as count from
(select * from shortest_road where optimization='["MRK", "DY"]') as total
group by length;

查看优化方法为["MRK","DY"]的length的分布情况
