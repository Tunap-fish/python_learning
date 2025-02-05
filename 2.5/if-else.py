num=eval(input('type in your number:'))
if num==5:
    print('Win!')
else:
    print('Lose!')

print('-'*12+'简化if-else语句')

result='Win!' if num==5 else 'Lose!'
print(result)

# 或者
print('Win!' if num==5 else 'Lose!')