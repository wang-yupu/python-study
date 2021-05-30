'''添砖加瓦-练习一'''

# 定义最小值函数
def mymin(x):
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m

