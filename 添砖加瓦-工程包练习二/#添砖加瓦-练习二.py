'''添砖加瓦-练习一'''
print("Test")
#导入mymax模块
from compare import mymax

#调用mymax模块中的mymax()函数,完成top3()函数
def top3(ls):
 res = []
 for x in range(3):
  temp = mymax.mymax(ls)
  res.append(temp)
  ls.remove(temp)
 return res

def mk():
 ik = input("输入多个数字 使用' '隔开")
 res = list(map(int,ik.split()))
 return res

print(top3(mk()))
print("Test")