# for循环的使用
# 每次取对象的一个元素
# 若没有元素可以取
# 那么循环结束
# for 循环变量 in 遍历对象：
# 语句块

for i in 'hello world': # 每次循环将字符串里下一个字符赋给 i
    print(i)

# range() 可产生一个 [n,m) 的整数序列
for i in range(1,11):
    print(i)

# example
# 水仙花数
for i in range(100,1000):
    sd=i%10
    ten=i//10%10
    hundred=i//100
    result=sd**3+ten**3+hundred**3
    if result==i:
        print("水仙花数：",i)

# for...else... 结构
# for 循环变量 in 遍历对象：
# 语句块
# else：
# 语句块
# 只有当循环正常结束才执行else后面的语句块
# 异常结束如 break跳出循环


