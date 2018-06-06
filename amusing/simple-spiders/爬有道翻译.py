import urllib.request
import urllib.parse
import json
import time
while True:
         input_content =input('需要翻译的内容是(输入q!退出程序):')
         if input_content == 'q!':
                  break
         url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
         data ={}
         '''
         head ={}
         head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
         '''
         data['i'] = input_content
         data['from'] ='AUTO'
         data['to'] = 'AUTO'
         data['smartresult'] ='dict'
         data['client']='fanyideskweb'
         data['salt']= '1521623162580'
         data['sign'] ='fbdb9f9d0daf860c35cec14b7804487c'
         data['doctype']='json'
         data['version'] ='2.1'
         data['keyfrom'] ='fanyi.web'
         data['action'] ='FY_BY_CLICKBUTTION'
         data['typoResult']='false'
         data = urllib.parse.urlencode(data).encode('utf-8')
         req =urllib.request.Request(url,data)
         req.add_header('User Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
         response = urllib.request.urlopen(req)
         html = response.read().decode('utf-8')
         tagent =json.loads(html)
         content =tagent['translateResult'][0][0]['tgt']
         print('内容【%s】翻译为：%s'%(input_content,content))
         time.sleep(5)
         
