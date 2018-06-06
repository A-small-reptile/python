class Tickets:
         def __init__(self,adult_num,child_num):
                  self.adult_num=adult_num
                  self.child_num=child_num
         def fare_calculation(self):
                  import time
                  current_week =time.localtime(time.time())[6]
                  if current_week == 6:
                           print('周末票价上涨20%')
                           total_fare = (100*1.2)*int(self.adult_num) +(100*1.2)*0.5* (int(self.child_num))
                           return total_fare
                  else:
                            total_fare = 100* int(self.adult_num) +100*0.5* (int(self.child_num))
                            return total_fare
def input_num():
         adult_num=input('请输入购买的成人票张数：')
         child_num= input('请输入购买的儿童票张数：')
         user_fare=Tickets(adult_num,child_num)
         print('票价共计%d元' % user_fare.fare_calculation())
         print('祝你玩的愉快')

input_num()   
         
