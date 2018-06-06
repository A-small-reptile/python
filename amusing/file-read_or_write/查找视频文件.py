def search_vedio(file_path,file_type):
         os.chdir(file_path)
         for each_file in os.listdir(os.curdir):
                  if os.path.isfile(each_file):
                           ext = os.path.splitext(each_file)[1]
                           if ext ==file_type:
                                    content.append(file_path+os.sep+each_file)
                                    print(file_path+os.sep+each_file)
                  if os.path.isdir(each_file):
                           search_vedio(file_path,file_type)
                           file_path.os.pardir
file_type=['.mp4','.rmvb','.avi']
content =[]
import os
file_path = input('请输入待查找的初始目录：')
search_vedio(file_path,file_type)
f = open('file_path+os.sep+vedioList.txt','w')
f.writelines(content)
f.close()
