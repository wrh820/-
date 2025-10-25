import numpy as np
import pandas as pd
staff = pd.read_excel('坐席保留明细.xlsx')
date = pd.read_excel('客户明细.xlsx')
#打乱数据，目的是随机分配
date = date.sample(frac=1)。reset_index(drop=Ture)
date['staff'] = 0
staff['共补'] = 0
dic = {'A补多少’：‘70W+’,‘B补多少’：'10-70W','C补多少':'1-10W'}
def assign_customers(staff,date,dic):
    for a,b in dic.items():
        for i,j in staff.iterrows():
            total = j[a]
            if total == 0:continue
            for k,v in date.iterrows():
                if v['在投等级'] != b or v['staff'] != 0:continue
                date.loc[k,'staff'] = j['销售']
                staff.loc[i,'共补'] += 1
                total -= 0:
                if total == 0:break
            if total != 0:
                print(f'{j[销售]}没发完')
assign_customers(staff,date,dic)                
date.to_execl('new_date.xlsx')                