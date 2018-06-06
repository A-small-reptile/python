def file_view(file_name,line_num):
         if  line_num.strip() == ':':
                  begin ='1'
                  end = '-1'
         (begin,end)= line_num.split(':')
         if begin == ' ':
                  begin ='1'
         if end == ' ':
                  end ='-1'
         if begin == '1' and end =='-1':
                  print('文件%s全文内容如下：' % file_name)
         elif begin =='1':
                  print('文件%s从开始到第%s行的内容如下:' %( file_name ,end))
         elif end =='-1':
                  print('文件%s从第%s行到末尾的内容如下:' % (file_name,begin))
         else:
                  print('文件%s从第%s行到第%s行的内容如下:' %(file_name,begin,end))
         begin = int (begin)-1
         end = int (end)
         lines = end-begin
         for i in range(begin):
                  f.readline()
         if lines <0 :
                 print( f.read())
         for j in range(lines):
                 print( f.readline())
         f.close()
file_name= input('请输入要打开的文件（c：\\test.txt）:')
line_num = input ('请输入需要显示的行数【格式如 13：21或：21或21：】:')
f = open (file_name,'r')
file_view(file_name,line_num)

         
