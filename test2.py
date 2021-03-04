import requests
import pandas as pd 

index=1

df = pd.read_csv("ip_pool.csv")
#  这里直接变成数组格式
# 一:proxies 1.2版本
df_list=df.values.tolist()

csv_ip_local = 0   # csv中用到第几个Ip了

proxies = {
        # type :ip   行列定位
        df_list[csv_ip_local][0]: df_list[csv_ip_local][1]
    }
def deal_proxes(csv_index):
    new_proxies = {
            # type :ip   行列定位
            df_list[csv_index][0]: df_list[csv_index][1]
        }

print(proxies)


print(proxies)

