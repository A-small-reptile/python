import urllib.request
import chardet
input_url =input('请输入URL:')
response = urllib.request.urlopen('http://'+input_url)
html = response.read()
decode_dict ={}
decode_dict =chardet.detect(html)
print('该网页使用的编码是:%s' % decode_dict['encoding'])
