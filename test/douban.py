import urllib.request
import urllib.error
import urllib.parse
headers={'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*'
         ,'Accept-Language': 'zh-CN'
         ,'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)'
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