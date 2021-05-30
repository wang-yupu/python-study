'''添砖加瓦-练习一&练习二'''
# import compare.mymax 
import compare.mymin 
# from compare import mymin 
from compare import mymax

# 定义排序函数
def mysorted(y, reverse=False):
    y = list(y)
    # 结果列表
    s = []
    # 默认升序排序
    if reverse == False:
        while y:
            # 调用最小值函数
            m = compare.mymin.mymin(y) #一种调用方法
            y.remove(m)
            s.append(m)
    # 降序排序
    else:
        while y:
            # 调用最大值函数
            m = mymax.mymax(y) #另一种调用方法
            y.remove(m)
            s.append(m)
    return s

# 调用排序函数
res1 = mysorted((1,26,0,1,34,0))
print('升序排列：'+str(res1))


