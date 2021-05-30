'''添砖加瓦-练习一工程包'''

#导入mysorted模块
import compare.mysorted,random
#调用mysorted模块中的mysorted()函数
j = []
for x in range(random.randint(15,30)):
    j.append(random.randint(0,200))
print(j)
print(compare.mysorted.mysorted(j))