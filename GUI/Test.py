import pandas as pd

inputfile_1 = "D:\\chaoyang.xlsx"

df = pd.read_excel(inputfile_1)#,index_col = '序号'

df = df.iloc[:,[0,2]]
print(df)

test_data=[]

dict = df.set_index("字段名称").to_dict()['类型']
print(dict)

# for key in dict.keys():
#     print(key)
#
# for value in dict.values():
#     print(value)
for key,value in dict.items():
    print(key)
    print(value)

S = ""



# for i in df.index.values: #获取行号的索引，并对其进行遍历：
# #根据i来获取每一行指定的数据 并利用to_dict转成字典
# row_data=df.ix[i,[‘ID’,‘name’,‘age’,‘sex’]].to_dict()
# test_data.append(row_data)
# print(“最终获取到的数据是：{0}”.format(test_data))