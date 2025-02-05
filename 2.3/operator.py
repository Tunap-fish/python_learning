# 算术运算符
# 除了正常的 + - * / %
# 还有
# ** 幂运算
# // 整除
# / 是正常除法，发生隐式类型转换，得到浮点数
# // 得到整数

# 赋值运算符
# += -= %= //= **= 等
# 先运算左边，再赋值

# 比较运算符
# > < <= >= == !=
# return True or False

# 逻辑运算符
# and or not
# return True or False
print(True and True)
print(False and True)
print(True or False)
print(8<7 and 10/0) # although 10/0 is invalid, but it didn't be implemented
# 没有执行 程序在看到第一个False之后便直接输出
print(8>7 or 10/0) # 同理or只要第一个是True便直接输出

# 位运算
# & | ~ ^ << >>

# 神奇的赋值
a=10
b=20
a,b=b,a # 交换a与b的值
print(a,b)

x=eval(input('4 bitwise number:'))
print(x%10,end='-')
x//=10
print(x%10,end='-')
x//=10
print(x%10,end='-')
x//=10
print(x%10)

