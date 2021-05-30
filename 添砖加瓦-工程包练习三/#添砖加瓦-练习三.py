'''添砖加瓦-练习四'''

#导入myreverse模块，myreverse模块待修改
from compare import myreverse as mr

#调用myreverse模块中的两个函数
msg = input('请输入字符串：')
print("迭代",mr.reverse_str1(msg))
print("递归",mr.reverse_str2(msg))
