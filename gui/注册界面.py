def judge_input(user_choices):
         if user_choices == 1:
                  user_information(msg,title,fields,values)
         else:
                  sys.exit(0)
def user_information(msg,title,fields,values):
         count=0
         content =[]
         content =g.multenterbox(msg,title,fields,values)
         if content ==None:
                  sys.exit(0)
         else:
                  for each_content in content:
                           if  each_content=='' or  each_content[0] ==' ' :
                                    user_choices=g.ccbox(msg_error,title_error,button_error,image)
                                    judge_input(user_choices)
                           else:
                                    count+=1
                                    if count ==5:
                                             g.msgbox('已注册成功','提示',ok_button='确定',image='F:\Program Files\Python36\image1.gif')
                                             sys.exit(0)
import easygui as g
import sys
msg =('【*真实姓名】为必填项.\n','【*手机号码】为必填项.\n','【*E-mail】为必填项.\n')
title='账号中心'
fields=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
values=['','','','','','']
msg_error='输入的内容有误，请重新输入\n 提示：请不要输入空格'
title_error='错误提示'
button_error =['重新输入','退出']
image ='F:\Program Files\Python36\image1.gif'
user_information(msg,title,fields,values)
                           
                  
                  
         




