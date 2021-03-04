import csv
import pandas as pd 
# with open('ip_pool.csv', encoding='utf-8') as f:
#     reader = csv.reader(f)

#     header = next(reader)
#     # 你的命名头
#     print(header)
#     print(reader[3])
#     for row in reader:
#         print(row)
# 得出的是该行的字符串
# with open('ip_pool.csv', encoding='utf-8') as f:
#     lines=f.readlines()
#     print(lines[0])
import pandas as pd 
df = pd.read_csv("ip_pool.csv")

# 下面都是没变成数组处理的
# print(df)
# 获取某一行的值
# print(df.iloc[1])

# 获取某一列的值
# print(df["type"]) # 列名是item_id的列

# 获取某一行某一列的值
# print(df.iloc[1]["item_id"])

#  这里直接变成数组格式
list=df.values.tolist()
print(list[0][0])



