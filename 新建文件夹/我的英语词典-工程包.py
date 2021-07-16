'''我的英语词典上-工程包'''
import os
import sys

def loading_dict():
    '''加载词典'''
    '''
    输入：无
    输出：包含所有单词的字典，格式如{'apple':{'NO.':'1', 'mean': 'n.苹果'}, ......}
    '''
    #建立空字典用来存储加载出来的单词信息
    wordsDict = {}
    with open("wordsSpace.txt","r",encoding="utf-8") as w:
        word_list = w.readlines()
    for word in word_list:
        wordList = word.split("#")
        wordDict = {
            'NO.':wordList[0],'mean':wordList[2],'link':wordList[3][:-1]}
        wordsDict[wordList[1]] = wordDict
    return wordsDict

def loading_set():
    #加载设置
    setDict = {}
    with open('seetings.txt',"r",encoding="utf-8") as s:
        setl = s.readlines()
    for seet in setl:
        setc = seet.split('#')
        setDict = {setc[0]:setc[1]}
    return setDict

def set_set(sts,b,sd):
    sd[sts] = b

wordsDict = loading_dict()

def save_dict():
    with open("wordsSpace.txt","w",encoding="utf-8") as w:
        for k,v in wordsDict.items():
            line = v['NO.'] + '#' + k + '#' + v['mean'] + '#' + v['link'] + '\n'
            w.write(line)

def add_linked_words(word,addword):
    wordsDict[word]['link'] += addword
    wordsDict[word]['link'] += ','
    return wordsDict

def search_by_ENG(word, wordsDict):
    '''英译中查询'''
    '''
    输入：想要查询的单词word、完整的单词字典wordsDict
    输出：相应单词含义字符串或者没有单词提示字符串res
    '''
    try:
        res = word+'  '+wordsDict[word]["mean"]
        if wordsDict[word]['link']:
            res += "联想词:" + wordsDict[word]['link']
    except KeyError:
        res = "Not found / 无法寻找单词 "+"'",word,"'"
    return res

def search_by_CN(word,wordsDict):
    pass

def menu():
    '''显示功能菜单'''
    print('-------------------------------------------------------------------')
    print("-英语词典菜单-(建议使用Python Shell/CMD/PowerShell运行")
    print("-Commands / 命令")
    print("EC   -  英译中")
    print("CE   -  中译英")
    print("ALW  -  添加联想词")
    print("")
    print("-通用命令")
    print("-V 版本信息")
    print("-S 设置信息")
    print("")
    print("输入quit以退出")
    print("输入clear以清除Shell")
    print('-------------------------------------------------------------------')

    
#主程序
wordsDict = loading_dict()
SetD = loading_set()

menu()
while True:
    cmd = input(">>>")
    #
    if cmd == "EC":
        instr = " "
        instr = input("英译中 - 翻译内容:")
        out = search_by_ENG(instr,wordsDict)
        print(out)
    elif cmd == "ALW":
        aw = input("添加联想词的单词")
        al = input("添加的联想词")
        add_linked_words(aw,al)
        print("添加完成")
    elif cmd == "-S":
        pass
    elif cmd == "-V":
        print("v2021-7.016")
        print("Code by wangyupu and CodeMao")
    elif cmd == "quit":
        print("保存并退出")
        save_dict()
        sys.exit()
    elif cmd == "clear":
        os.system('cls')

    if SetD[clears] == 'true':
        os.system('cls')
        