'''添砖加瓦-练习一'''
# 递归法反向输出字符串
def reverse_str(s):
    if s == '':
        return ''
    else:
        return reverse_str(s[1:])+s[0]

