def file_size(file_path):
         import os
         file_dict = {}
         os.chdir(file_path)
         os.getcwd()
         all_file =os.listdir(os.curdir)
         for each_file in all_file:
                  if  not os.path.isdir(each_file):
                           each_file_size= os.path.getsize(each_file)
                           file_dict.setdefault(each_file,each_file_size)
                           print('%s 【%sBytes】'%(each_file,each_file_size))
file_path=input('请输入需要查看的文件夹：')
file_size(file_path)
