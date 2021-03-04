# 导入CSV安装包
import csv

# 1. 创建文件对象
f = open('name.csv','w',encoding='utf-8',newline='' "")

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
csv_writer.writerow(["type","IP"])

# 4. 写入csv文件内容
csv_writer.writerow(["Http",'18'])
csv_writer.writerow(["Http",'20'])
csv_writer.writerow(["Http",'22'])

# 5. 关闭文件
f.close()

