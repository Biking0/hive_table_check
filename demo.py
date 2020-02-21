# encoding=utf8
# hive_table_check
# by hyn
# 20200220

import os
import time
import datetime
import config

input_data = '202002'

hadoop_path = 'hadoop fs -du /test/'
month_day = ['01', '02', '03', '04', '05', '06', '07', '10',
             '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
# 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

for i in config.day_table:
    print i[0]
    table_name = i[0]
    table_info_sh = hadoop_path + table_name + '/month_id=' + input_data + '/ > table_info.txt'
    print table_info_sh

    # 执行命令
    # os.popen(table_info_sh)

# 处理表信息
get_table_info = open('table_info.txt', 'r').readlines()
for i in get_table_info:
    print i
# get_date = int(time.strftime('%d', time.localtime(time.time())))
# print get_date
# for j in month_day:
#     print j
#     if int(j) > get_date:
#         break
