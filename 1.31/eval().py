str='3.14+3'
# eval() 函数会将字符串中的引号去掉，然后执行相应运算
x=eval(str)
print(str,type(str))
print(x,type(x))

# eval() 和 input() 一般一起使用，来获取用户输入的数据
age=eval(input('please type in your age:'))
print('your age is',age,type(age))
height=eval(input('how tall are you?'))
print('you are',height,'cm tall.',type(height))

# 一些小注意
hello='hello world!'
print(hello)
print(eval('hello')) # 这里eval去掉了hello字符串左右的引号，于是就有了变量hello