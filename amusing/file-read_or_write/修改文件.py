def save_file(save_result,file_content,user_path):
         if save_result == '覆盖保存':
                  with open(user_path,'w',encoding='UTF-8') as  old_file:
                           old_file.writelines(file_content[:-1])
                           choices_result = g.ccbox('文件已更新','保存提示',choices=('继续查找','退出程序'))
                           if choices_result ==1:
                                    input_file()
                           else:
                                    sys.exit(0)
         elif save_result =='另存为...':
                  save_path =g.diropenbox(default='F:\Program Files\Python36')
                  if save_path != '':
                           save_name =g.enterbox('请输入文件名','提示')
                           if save_name=='': 
                                   save_name =g.enterbox('请输入文件名进行保存','提示')
                           else:
                                    with  open(save_path+os.sep+save_name,'w',encoding='UTF-8') as new_file: 
                                             new_file.writelines(file_content[:-1])
                                             g.msgbox('文件已保存，请进入文件夹中查看','提示',ok_button='退出程序')
                  else:
                           choices_result2=g.ccbox('是否继续查找文件','提示',choices=('继续查找','退出程序'))
                           if choices_result2 ==1:
                                    input_file()
                           else:
                                    sys.exit(0)
def compare_file(user_choices,user_path):
         try:
                  with open(user_path,encoding='UTF-8') as old_file:
                           text=old_file.read()
                           display_msg =('文件%s的内容显示如下：' % user_choices)
                           display_title ='显示文本内容'
                           file_content =g.textbox(display_msg,display_title,text )
                           if text != file_content[:-1]:
                                    compare_msg ='检测的文件内容发生改变，请选择以下操作：'
                                    compare_title ='警告'
                                    compare_choices = ('覆盖保存','放弃保存','另存为...')
                                    save_result =g.buttonbox(compare_msg,compare_title,choices=compare_choices)
                                    save_file(save_result,file_content,user_path)
                           else:
                                    user_cho=g.ccbox('文件未做更改，是否查找其他的文件？')
                                    if user_cho ==1:
                                          input_file()
                                    else:
                                             sys.exit(0)
         except UnicodeDecodeError:
                  print('所打开的文本有不支持的字符，程序已退出')
def choices_file(content_name,path_dict):
         try:
                  msg ='以下是查找到的文件，请选择：'
                  title ='文件选择'
                  choices = content_name
                  user_choices = g.choicebox(msg,title,choices)
                  if user_choices !='' :
                           user_path=path_dict[user_choices]
                           compare_file(user_choices,user_path)
                  else:
                           input_file()
         except KeyError:
                  user_cho1=g.ccbox('你没有进行文件选择，手否重新输入？','提示',choices=('重新输入','退出程序'))
                  if user_cho1 ==1:
                           input_file()
                  else:
                           sys.exit(0)
def search_file(file_root,file_name):
         try:
                  os.chdir(file_root)
                  all_file = os.walk(os.getcwd())
                  content_name=[]
                  path_dict ={}
                  for i in all_file:
                           for each_file in i[2]:
                                    if os.path.splitext(each_file)[0] ==file_name:
                                             file_path =os.path.join(i[0]+os.sep+each_file)
                                             content_name.append(each_file)
                                             path_dict[each_file]=file_path
                                             choices_file(content_name,path_dict)
         except (TypeError,FileNotFoundError):
                  g.msgbox('输入错误，请参照提醒进行输入查找','错误提醒',ok_button='重新输入')
                  input_file()
def input_file():
         file_root = g.enterbox('请输入需要查找的根目录【如c:\\user\】','文件路径输入') 
         file_name=g.enterbox('请输入需要查找的文件名【如record.txt】','文件名字输入')
         if file_root !='' and file_name !='':
                  search_file(file_root,file_name)
         else:
                  user_cho1=g.ccbox('没有进行输入，是否再次查找','提示',choices=('重新输入','退出程序'))
                  if user_cho1 ==1:
                           input_file()
                  else:
                           sys.exit(0)
import easygui as g
import os
import sys
input_file()
