class Person:
         def __init__(self,f_n):
                  self.f_n=f_n

         def get_f_n(self):
                  return self.f_n
         def set_f_n(self,value):
                  if not isinstance(value,str):
                           raise TypeErro('ecpected a string')

                  self.f_n

         def del_f_n(self):
                  raise AttributeError('can not delete string')


         x=property(get_f_n,set_f_n,del_f_n,'this is a attr')
