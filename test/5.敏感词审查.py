# 要审查的帖子在这个文本文档里，要求将所有的和谐，三个代表，言论自由，64替换为*号
import sys
f=open('1.txt','r')
line=f.read()
newline=line.replace('和谐','**')
print(newline)
f.close()
f=open('1.txt','w')
f.write(newline)
f.close()

