#keyword
#保留字
import keyword
print(keyword.kwlist)
#保留字严格区分大小写

#给变量命名的时候
#第一个字符不能是数字
#不能使用python中的保留字
#严格区分大小写

#常量命名时采用全部大写字母可以使用下划线
#使用但下划线开头的变量或函数是受保护的
#在使用"from xxx import*"
#从模块中导入的时候
#这些模块变量和函数不能被导入
#双下划线开头的是类私有的
#开头和结尾有双下划线的是python的专用标识，如__init__()表示初始化函数

#type()函数查看数据类型
lucky_number=8
print('lucky_number\'s datatype is',type(lucky_number))

#python可以动态修改数据类型
#通过赋不同的值就可以动态修改
lucky_number='can you guess?'
print('lucky_number\'s datatype is',type(lucky_number))

#在python中允许多个变量指向同一个值
num=number=1024#两个变量名都指向1024
print(num,number)
print(id(num))#id()这个函数可以查看对象的内存地址
print(id(number))
#发现地址其实是一样的

#常量
#全部使用大写字母和下划线命名
#值不允许改变
PI=3.1415926 # 定义了一个常量