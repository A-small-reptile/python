import urllib.request
import os 
def open_url(url):
         req =urllib.request.Request(url)
         req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
         response = urllib.request.urlopen(req)
         html = response.read()
         return html
def find_addr(page_url):
         html =open_url(page_url).decode('utf-8')
         img_addrs= [ ]
         a =html.find('img src=')
         while a != -1:
                  b =html.find('jpg', int(a), int(a+255))      
                  if b != -1:
                           img_addrs.append(html[(a+9):(b+3)])
                  else:
                           b =a+9
                  a = html.find('img src=', b)
         
         return img_addrs
                
def save_images(filer,image_addrs):
         for each in image_addrs:
                  file_name =each.split('/')[-1]
                  with open(file_name,'wb') as f:
                           img =open_url(each)
                           f.write(img)
def get_page(url):
         html =open_url(url).decode('utf-8')
         a =html.find('current-comment-page')+23
         b =html.find(']',a)
         return html[a:b]
def download_girl(filer='girl_photo',pages=10):
         os.mkdir(filer)
         os.chdir(filer)
         url =r'http://jandan.net/ooxx/'
         page_num =int(get_page(url))
         for i in range(pages):
                  page_num -=i
                  page_url =url+'page-'+str(page_num)+'#comments'
                  image_addrs =find_addr(page_url)
                  save_images(filer,image_addrs)
if __name__ == '__main__':
         download_girl()
         



         
