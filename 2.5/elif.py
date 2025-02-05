# 多分支结构
score=eval(input('type in your score:'))
if score<0 or score>100:
    print('invalid input')
elif 10>=score/10>=7:
    print('A')
elif 4<=score/10<7: # 非常灵活的比较书写
    print('B')
else:
    print('C')

# 使用 and 和 or 来链接多个条件