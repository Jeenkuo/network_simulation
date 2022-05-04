"""
Constants needed to implement the function
"""
# The list of transportation network
list_targetG = [("MRK","DY",120),("MY","DY",23),("GY","DY",52),
                ("GY","NC",40),("NC","BZ",30),("NC","DZ",30),
                ("NC","GA",20),("SN","NC",35),("CD","SN",30),
                ("CD","DY",43),("CD","YA",30),("YA","KD",60),
                ("CD","MS",15),("CD","ZY",25),("MS","LS",17),
                ("ZY","NJ",20),("NJ","ZG",21),("ZG","LZ",18),
                ("LS","YB",20),("LS","XC",183),("XC","PZH",75)]

# The dictionary of transportation network
dic_targetG = {("Chengdu","Deyang"):59,("Deyang","Mianyang"):47,
               ("Mianyang","Suining"):143,("Chengdu","Suining"):88,
               ("Chengdu","Yaan"):96,("Chengdu","Meishan"):62,
               ("Chengdu","Ziyang"):35,("Yaan","Meishan"):105,
               ("Yaan","Leshan"):114,("Meishan","Leshan"):49,
               ("Meishan","Ziyang"):89,("Ziyang","Suining"):111,
               ("Ziyang","Neijiang"):40,("Leshan","Neijiang"):148,
               ("Leshan","Yibin"):71,("Zigong","Yibin"):141,
               ("Zigong","Neijing"):50,("Zigong","Luzhou"):59,
               ("Yibin","Luzhou"):125,("Suining","Neijiang"):116,
               ("Neijiang","Luzhou"):109,("Neijiang","Rongchang"):28,
               ("Luzhou","Qijiang"):130,("Rongchang","Yongchuan"):25,
               ("Yongchuan","Bishan"):20,("Tongliang","Bishan"):85,
               ("Tongliang","Tongnan"):74,("Suining","Tongnan"):57,
               ("Suining","Nanchong"):65,("Nanchong","Dazhou"):80,
               ("Nanchong","Guangan"):46,("Guangan","Dazhou"):59,
               ("Dazhou","Liangping"):98,("Tongnan","Hechuan"):25,
               ("Hechuan","Chongqing"):25,("Guangan","Chongqing"):76,
               ("Guangan","Dianjiang"):89,("Bishan","Chongqing"):25,
               ("Chongqing","Changshou"):25,("Chongqing","Nanchuan"):81,
               ("Chongqing","Qijiang"):26,("Qijiang","Nanchuan"):69,
               ("Nanchuan","Fuling"):84,("Fuling","Qianjiang"):139,
               ("Changshou","Fuling"):12,("Changshou","Dianjiang"):25,
               ("Dianjiang","Zhongxian"):106,("Dianjiang","Liangping"):23,
               ("Liangping","Wanzhou"):27,("Zigong","Luzhou"):27,
               ("Hechuan","Guangan"):35}

# the dictionary of optimization transportation network
dic_targetG_c ={("Chengdu","Deyang"):59,("Deyang","Mianyang"):47,
               ("Mianyang","Suining"):62,("Chengdu","Suining"):24,
               ("Chengdu","Yaan"):35,("Chengdu","Meishan"):62,
               ("Chengdu","Ziyang"):35,("Yaan","Meishan"):105,
               ("Yaan","Leshan"):44,("Meishan","Leshan"):49,
               ("Meishan","Ziyang"):45,("Ziyang","Suining"):111,
               ("Ziyang","Neijiang"):40,("Leshan","Neijiang"):148,
               ("Leshan","Yibin"):71,("Zigong","Yibin"):141,
               ("Zigong","Neijing"):50,("Zigong","Luzhou"):59,
               ("Yibin","Luzhou"):45,("Suining","Neijiang"):63,
               ("Neijiang","Luzhou"):109,("Neijiang","Rongchang"):28,
               ("Luzhou","Qijiang"):130,("Rongchang","Yongchuan"):25,
               ("Yongchuan","Bishan"):20,("Tongliang","Bishan"):35,
               ("Tongliang","Tongnan"):74,("Suining","Tongnan"):57,
               ("Suining","Nanchong"):20,("Nanchong","Dazhou"):40,
               ("Nanchong","Guangan"):46,("Guangan","Dazhou"):30,
               ("Dazhou","Liangping"):98,("Tongnan","Hechuan"):25,
               ("Hechuan","Chongqing"):25,("Guangan","Chongqing"):40,
               ("Guangan","Dianjiang"):89,("Bishan","Chongqing"):25,
               ("Chongqing","Changshou"):27,("Chongqing","Nanchuan"):35,
               ("Chongqing","Qijiang"):26,("Qijiang","Nanchuan"):69,
               ("Nanchuan","Fuling"):84,("Fuling","Qianjiang"):139,
               ("Changshou","Fuling"):12,("Changshou","Dianjiang"):22,
               ("Dianjiang","Zhongxian"):106,("Dianjiang","Liangping"):20,
               ("Liangping","Wanzhou"):27,("Tonglang","Ziyang"):45,
               ("Deyang","Ziyang"):54,("Meishan","Neijiang"):145,
               ("Leshan","Zigong"):56,("Zigong","Rongchang"):20,
               ("Zigong","Luzhou"):29,("Yibin","Luzhou"):45,
               ("Luzhou","Yongchuan"):27,("Rongchang","Tongliang"):36,
               ("Tongliang","Hechuan"):15,("Hechuan","Changshou"):43,
               ("Dazhou","Wanzhou"):20,("Wanzhou","Zhongxian"):40,
               ("Zhongxian","Qianjiang"):62}

# the dictionary of road optimization plan
dic_optimization = {("Chengdu","Yaan"):35,("Yaan","Leshan"):44,
                    ("Chengdu","Suining"):44,("Deyang","Ziyang"):54,
                    ("Meishan","Ziyang"):45,("Meishan","Neijiang"):145,
                    ("Leshan","Zigong"):56,("Luzhou","Yibin"):45,
                    ("Zigong","Rongchang"):20,("Suining","Neijiang"):63,
                    ("Ziyang","Tongliang"):40,("Mianyang","Suining"):62,
                    ("Suinning","Nanchong"):20,("Nanchong","Dazhou"):40,
                    ("Dazhou","Wanzhou"):40,("Guangan","Dazhou"):30,
                    ("Tongliang","Rongchang"):36,("Tongliang","Bishan"):35,
                    ("Tongliang","Hechuan"):25,("Luzhou","Yongchuan"):27,
                    ("Rongchang","Yongchuan"):20,("Guangan","Chongqing"):40,
                    ("Chongqing","Nanchuan"):35,("Hechuan","Changshou"):43,
                    ("Changshou","Fuling"):12,("Wanzhou","Zhongxian"):40,
                    ("Zhongxian","Qianjiang"):62,("Nanchuan","Qianjiang"):80,}

# the dictionary of road optimization plan
dic_optimization_1 = {("Chengdu","Deyang"):59}
# the list of starting point
list_source=["Chengdu","Chengdu","Chengdu","Chengdu","Chengdu","Chengdu",
             "Chengdu","Chengdu","Chengdu","Mianyang","Mianyang","Yibin",
             "Yibin","Deyang","Nanchong","Nanchong","Nanchong","Luzhou",
             "Dazhou","Dazhou","Dazhou","Dazhou","Dazhou","Leshan","Yaan",
             "Leshan","Leshan","Neijiang","Neijiang","Neijiang","Neijiang",
             "Neijiang","Neijiang","Neijiang","Neijiang","Zigong","Zigong",
             "Meishan","Suining","Suining","Suining","Suining","Suining",
             "Guangan","Ziyang","Chongqing","Chongqing","Chongqing",
             "Chongqing", "Chongqing", "Chongqing", "Chongqing",
             "Chongqing", "Fuling","Yongchuan","Yongchuan","Yongchuan",
             "Hechuan","Hechuan","Wanzhou","Bishan","Changshou","Changshou",
             "Qijiang","Rongchang","Rongchang","Rongchang","Tongliang",
             "Tongliang","Tongliang","Liangping","Liangping","Tongnan",
             "Tongnan","Tongnan","Dianjiang","Zhongxian","Nanchuan","Qianjiang"]

#the list of ending point
list_target=["Chengdu","Chengdu","Chengdu","Chengdu","Chengdu","Chengdu",
             "Chengdu","Chengdu","Mianyang","Mianyang","Mianyang","Mianyang","Yibin","Yibin",
             "Yibin","Yibin","Deyang","Deyang","Nanchong","Nanchong",
             "Nanchong","Nanchong","Luzhou","Luzhou","Dazhou","Dazhou",
             "Dazhou","Dazhou","Dazhou","Dazhou","Leshan","Leshan",
             "Leshan","Leshan","Neijiang","Neijiang","Neijiang","Neijiang",
             "Neijiang","Neijiang","Neijiang","Neijiang","Neijiang","Zigong",
             "Zigong","Meishan","Suining","Suining","Guangan","Ziyang",
             "Chongqing","Chongqing","Chongqing","Chongqing","Chongqing",
             "Chongqing", "Chongqing","Yaan",
             "Chongqing","Fuling","Fuling","Yongchuan","Yongchuan","Yongchuan",
             "Hechuan","Hechuan","Wanzhou","Bishan","Bishan","Changshou",
             "Changshou","Changshou","Changshou","Qijiang","Qijiang"]

list_city = ["Chengdu","Chongqing","Neijiang","Suining","Dazhou",
             "Rongchang","Tongliang","Tongnan","Leshan",
             "Nanchong","Changshou","Yongchuan","Yibin","Liangping",
             "Hechuan","Zigong","Mianyang","Meishan","Guangan",
             "Nanchuan","Fuling","Yaan","Deyang","Luzhou",
             "Qijiang","Dianjiang","Bishan","Wanzhou","Zhongxian",
             "Qianjiang","Ziyang"]

#the list of simulation times
times_list = [100]
#cishu_list = [100,200]