import urllib.request
response=urllib.request.urlopen('https://www.baidu.com/')
result=response.getcode()
print(result)