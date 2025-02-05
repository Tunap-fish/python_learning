num=1234 # 十进制
num2=0b01010101 # 二进制 0b
num8=0o1263432 # 八进制 0o
num16=0x58A73F # 十六进制 0x

numf=1.23 # float 浮点数
nume=1.34E8 # 科学计数法
print(nume,type(nume))
# 不确定尾数问题
print(0.1+0.2) # 0.30000000000000004
# 使用round函数保留
print(round(0.1+0.2,1)) # 保留一位小数

# 复数类型
# 整数 + 虚数
x = 123 + 456j
print("real part",x.real)
print("imaginary part",x.imag)
print(x)

# 字符串类型
# '' 或 "" 皆可
# ''' ''' 三引号一般用于多行书写
info='''welcome to the internet!
have a nice trip here!
We can see you anywhere!
'''
print(info)
# 转义字符
# \n 换行
# \t 进入下一个制表位(8位)
# \'  \"  \\
# 原字符 r or R，使转义字符失效
print('hello\nword')
print(r'hello\nword')
# 字符串的检索和切片
str='helloworld'
print(str[0],str[-10]) # 都是h，从左到右从0开始，从右到左从-1开始数
print(str[2:7]) # 2到6位，不包括7
print(str[-8:-3]) # 反向也行
print(str[:7]) # 默认从0开始
print(str[5:]) # 默认延续到字符串的结尾
# 字符串操作
# x+y + 为链接符
# x*n 把字符串x复制n次
# x in s 若x是s的子串，则为True，否则为False
print(10*str)
print('hello' in str)
print('hollo' in str)

# 布尔类型
# True 为1，False 为0
# 一切变量皆对象
x_bool=True
print(type(x_bool))
print(x_bool+1)
print(False+1)
# 检测布尔值
print(bool(18))
print(bool(0),bool(0.01),bool(0.0))
# 所有非0数字皆为True
print(bool('bool'))
print(bool(' '))
print(bool(''))
# 所有非空字符（串）皆为True
print(bool(False)) # False
print(bool(None)) # False
# 所有空序列，如空字符串，空元组，空列表，空字典，空集合
# 以及自定义对象方法返回False或0

# 数据类型之间的转换
# int()
# float()
# str()
# chr() 将一个整数x转化成对应字符
# ord() 将一个字符转化成对应整数x
# hex()
# oct()
# bin() # 以上三个转成字符串类型 （十六，八，二进制）

# 将int转成float
# 只保留整数部分
# 不考虑进位