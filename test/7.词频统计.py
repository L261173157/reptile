# 分析这个文本文档里的词频，按照出现频率由高到低排列结果，不区分大小写，过滤掉标点（可以使用正则表达式）。
# 结果类似ok：234，play：122，funny：78
# 需要正则表达式 http://www.runoob.com/python3/python3-reg-expressions.html
# \s?\S+\s?
import re
f=open('1.txt','r')
line=f.read().lower()
# print(line)
line1=re.sub('\.','',line)
# print(line1)
pattern=re.compile('\S+',re.I)
wordline=pattern.findall(line1)
print(wordline)
wordFre=[]
wordFre.append(wordline[0])
for word in wordline:
    a=0
    for wordf in wordFre:
        if wordf==word:
            a=1
    if a==0:
        wordFre.append(word)
print(wordFre)
worddict=dict.fromkeys(wordFre,0)
# for wordf in wordFre:
#     i=0
#     for word in wordline:
#         if wordf==word:
#             i+=1
#     print(wordf,':',i)
for word in wordline:
    if word in worddict:
        worddict[word]=worddict[word]+1
print(worddict)
worddictnew=sorted(worddict.items(),key=lambda item:item[1],reverse=True)
print(worddictnew)






