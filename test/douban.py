import urllib.request
import urllib.error
import urllib.parse
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
         ,'Accept-Language': 'zh-CN,zh;q=0.9'
         ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
         }
value = {'source': 'index_nav',
     'form_password': '',
     'form_email': ''
     }
try:
    data=urllib.parse.urlencode(value).encode('utf8')
    response=urllib.request.Request('https://www.douban.com/login',data=data,headers=headers)
    html=urllib.request.urlopen(response)
    result=html.read().decode('utf8')
    print(result)
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print('错误原因是'+str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e,'code'):
        print('错误代码是'+str(e.code))
    else:
        print('请求成功通过')