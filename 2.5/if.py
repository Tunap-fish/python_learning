number=eval(input('type in your number:'))
if number==50:
    print('congratulation! you have won the prize!')

n=98
if n%2: # 0 is False
    print('odd')

if not n%2:
    print('even')

# 一切皆对象，每个对象都有一个布尔值
str=input('type in a string:')
if str:
    print('this is not a blank string.')

# 可以直接输入布尔值
bool=eval(input('True or False:'))
print(bool) # 赋值给bool一个布尔值（True or False）
if bool:
    print('True')

if not bool:
    print('False')
