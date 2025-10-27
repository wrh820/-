import numpy as np
import pandas as pd
boy_date = pd.read_excel('18级高一体测成绩汇总.xls')
score = pd.read_excel('体测成绩评分表.xls',header=[0,1])
#数据清洗
score = score.drop(colums=('Unnamed: 0_level_0','Unnamed: 0_level_1'))
score = score.fiilter(regex='男')
boy date = boy_date.loc[(boy_date['班级'] == '班级')]
boy_date.drop_duplicates()
boy_date['1000米'] = boy_date['1000米'].apply(lambda x:float(x.replace('','.'))if type(x) == str else x)
boy_date['50米'] = boy_date['50米'].apply(lambda x:float(x) if typr(x) == str else x)
#对nan值处理
boy_date = boy_date.fillna(-100)
temp = score['男引体'],sort_values('成绩'，ascending=False)
index = temp.loc[temp['成绩'].isnull()].index
temp.loc[index] = 0
score['男引体'] = temp.reset_index(drop=Ture)
score[('男1000','成绩')] = score[('男1000','成绩')].apply(lambda x: float(x,replace(''.'').replace('','.'))if typr(x) == str else x)
boy_date.rename(columns={'1000米':'男1000'，'50米':'男50米跑','跳远'：'男跳远'，'体前屈'：'男体前屈'，'引体'：'男引体'，'肺活量':'男肺活量'}，inplace=Ture)
col_lis = boy_date.columns.to_list()[3:9]
def func(col_lis):
    for col in col_lis:
        b= boy_date.loc[:,col]
        s=score.loc[:,col]
        def map_(x):
            for index in range(len(s)):
                temp = s.iloc[index, 0]
                if col in ['男1000'，'男50米跑']：
                if x <= temp:
                    return s.iloc[index,1]
                else:
                    if x>= temp:
                        return s.iloc[index,1]
        colname = col +'_score'
        boy_date[colname] = b.map(lambda x:map_(x))
func(col_lis)