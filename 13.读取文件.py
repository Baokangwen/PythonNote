#打开文件
file = open("test.md")
#读取文件内容
text = file.read()
print(text)
print(len(text))
text = file.read()
print(text)
print(len(text))
#关闭文件
file.close()