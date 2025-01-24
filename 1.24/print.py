# print(value,...,sep=' ',end='\n',file=None)
# sep=' '是空格符
#可以修改 sep 和 end

print('hello world')
print("hello world")
#单双引号皆可

a = '!'
print('hello','world',a)
#中间有空格

print(chr(98))
#chr(98) = 'b'
#chr() 可以将ASCII码Unicode码等转成字符
#Unicode码字符编码，双字节16位进行编码，含中文

print(ord('我'))
print(ord('b'))
#ord('...')可以将字符转成对应码

#写入文件
fp = open('file.txt', 'w')#打开并找到文件的地址
print('北京欢迎你 welcome to Shenzhen',file = fp)#写入
fp.close()#关闭文件

#修改 sep 和 end
print('hello',end='-->')
print('world')
print('hello'+'world')#加号只能连接字符串
print('hello','world',sep='---')