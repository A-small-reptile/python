#基类
class Desc:
         def __init__(self,name=None,**opts):
                  self.name=name
                  for key,value in opts.items():
                           setattr(self,key,value)

         def __set__(self,instance,value):
                  instance.__dict__[self.name]=value


#限制类
class Type(Desc):
         expected_type=type(None)
         def __set__(self,instance,value):
                  if not isinstance(value,self.expected_type):
                           raise TypeError('expected'+str(self.expected_type))
                  super().__set__(instance,value)

class Unsigned(Desc):
         def __set__(self,insatnce,value):
                  if value<0:
                           raise ValueError('expected >=0')
                  super().__set__(instance,value)

class Maxsized(Desc):
         def __init__(self,name=None,**opts):
                  if 'size' not in opts:
                           raise TypeError('missing size option')
                  super().__init__(name,**opts)

         def __set__(self,instance,value):
                  if len(value)>=self.size:
                           raise ValueError('size must be '+str(self.size))
                  super().__set__(instance,value)

class Integer(Type):
         expected_type=int

class UnsignedInteger(Integer,Unsigned):
         pass
class Float(Type):
         expected_type= float
class UnsignedFloat(Float,Unsigned):
         pass
class String(Type):
         expected_type=str
class StringMaxsized(String,Maxsized):
         pass


if __name__=='__main__':
         class Stock:
                  name=StringMaxsized('name',size=7)
                  shares=UnsignedInteger('shares')
                  price=UnsignedFloat('price')
                  def __init__(self,name,shares,price):
                           self.name=name
                           self.shares=shares
                           self.price=price
                           
