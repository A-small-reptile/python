def print_pos(key_dict):
         keys =key_dict.keys()
         keys =sorted(keys)
         for each_key in keys:
                  print('关键字出现在第%s行，第#s个位置。'%(each_key,key_dict[each_key])
def pos_in_file(line,key):
         pos =[ ]
         begin = line.find(key)
         while begin != -1:
                  pos.append(begin+1)
                  begin = line.find(key,begin+1)
         return pos        
def search_in_file(file_name,key):
         f = open(file_name)
         count = 0
         key_dict ={}
         for each_line in f:
                  count +=1
                  if key in each_line:
                           pos =pos_in_file(each_line,key)
                           key_dict[count]=pos
         f.close()
         return key_dict
def search_file(key,detail):
         os.chdir('G:\\test')
         txt_files =[]
         file_detail =os.walk(os.getcwd())
         for i in file_detail:
                  for each_file in i[2]:
                           if os.path.splitext(each_file)[1] == '.txt':
                                    file_path = os.path.join(i[0]+os.sep+each_file)
                                    txt_files.append(file_path)
         #找到并生成.txt文件路径
         for each_txt_file in txt_files:
                  key_dict = search_in_file(each_txt_file,key)
                  if key_dict:
                           print('========================================')
                           print('在文件【%s】中找到关键字【%s】'%(each_txt_file,key))
                           if detail in ['YES','Yes','yes']:
                                    print
key = input ('请将该脚本放于待查找的文件内，请输入关键字：')
detail= input('请问是否打印关键字【%s】在文件中的具体位置【yes/no】:')
search_file(key,detail)
                        
