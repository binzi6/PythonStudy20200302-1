
print ('Hello, Python!')

# 第一个注释
print ("Hello, Python!")  # 第二个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#作用域同时缩进 不用{}
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
  #print ("False")

#数字类型计算  代码多行显示使用\
item_one =1;item_two=2;item_three=3.567;
total = item_one + \
        item_two + \
        item_three 
print (total)

#字符串
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print (word,sentence,paragraph)

#循环 数组
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
for ssddfd in days:
    print (ssddfd)

a = b = c = 1
print (a,b,c)
a, b, c = 1, 2, "john"
print (a,b,c)

#字符串截取
s = 'abcdef'
print(s[1:5])

str = 'Hello World!'
 
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:5])      # 输出字符串中第三个至第六个之间的字符串
print (str[2:])       # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串
