class Person:
         def __init__(self,name):
                  self.name=name

         @property
         def name(self):
                  return self._name
         @name.setter
         def name(self,value):
                  if not isinstance(value,str):
                           raise TypeError('expected a string')
                  self._name= value

         @name.deleter
         def name(self):
                  raise AttributeError('can not delete attr')

class subperson(Person):
         @property
         def name(self):
                  print('geting name')
                  return super().name
         @name.setter
         def name(self,value):
                  print('setting name to ',value)
                  super(subperson,subperson).name.__set__(self,value)

         @name.deleter
         def name(self,):
                  print('deleting name')
                  super(subperson,subperson).name.__delete__(self)

                  
