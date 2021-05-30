'''添砖加瓦-练习一'''
#导入mymin和mymax模块
import compare.mymax,compare.mymin

# 定义排序函数
def mysorted(y, reverse=False):
    y = list(y)
    # 结果列表
    s = []
    # 默认升序排序
    if reverse == False:
        while y:
            # 调用最小值函数
            m = comparemymax.mymin(y) # 调用mymin模块中的函数
            y.remove(m)
            s.append(m)
    # 降序排序
    else:
        while y:
            # 调用最大值函数
            m = compare.mymin.mymin(y)  # 调用mymax模块中的函数
            y.remove(m)
            s.append(m) 
    return s



