def search_file(file_path,file_name):
         os.chdir(file_path)
         os.getcwd()
         for each_file in os.listdir(os.curdir):
                  if os.path.isdir(each_file):
                           search_file(file_path,file_name)
                           os.chdir(os.pardir)
                  elif each_file == file_name:
                           print(os.getcwd()+os.sep+each_file)
file_path=input('请输入待查找的初始目录：')
file_name = input('请输入需要查找的目录文件：')
import os
search_file(file_path,file_name)
                           
