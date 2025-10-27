import numpy as np
import pandas as pd
df1 = pd.read_excel('京东卡.xlsx')
df2 = pd.read_excel('用户应得奖励金.xlsx')
df2['保单号'] = df2['保单号'].astype(str)
def concat_(x):
    return '_'.join(x)
df3 = df2.groupby(['用户ID','客户姓名','销售']).agg({'活动奖励金额':np.sum,'保单号':concat_}).reset_index()
df1['user'] = 0
df1 = df1.sort_values('面值',ascending=False).reset_index(drop=Ture)
for i,j in df3.iterrows():
    amount = j['活动奖励金额']
    if amount == 0:continue
    for k,v in df1.iterrows():
        if amount < v['面值'] or v['uesr']!=0:continue
        amount -= v['面值']
        df1.loc[k,'user'] = j['用户ID']
        if amount == 0:
            break
    if amount != 0 :
        print(f'{j["用户Id"]}不足派发')
df4 = df1.merge(df3,left_on='user',right_on='用户ID',how='left')
df4 =df4.set_index('user')
for i in df4.index.unique():
    df4.loc[i].to_excel(f'{i}.xlsx',index=False)