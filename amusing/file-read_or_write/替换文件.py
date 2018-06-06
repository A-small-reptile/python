def file_replace(file_name,old_word,new_word):
         f_read =open (file_name)
         count =0
         content=[]
         for find_word in f_read:
                  if old_word in find_word:
                           count =find_word.count(old_word)
                           find_word=find_word.replace(old_word,new_word)
                  content .append(find_word)
         decide = input("文件%s中共有%s个【%s】\n 你确定要把所有的【%s】替换为【%s】吗？\n 【YES/NO】："
                        %(file_name,count,old_word,old_word,new_word))
         if decide in ['YES','Yes','yes']:
                  f_write = open (file_name,'w')
                  f_write.writelines(content)
                  f_write.close()
         f_read.close()
file_name = input('请输入文件名：')
old_word= input('请输入需要替换的单词或是字符：')
new_word= input('请输入新的单词或是字符：')
file_replace(file_name,old_word,new_word)

