'''添砖加瓦-练习一'''

# 定义最大值函数
def mymax(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m

