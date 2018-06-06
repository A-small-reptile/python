class MetaClass(type):
         def __new__(cls,name,bases,dicts):
                  print('new class %s'%name)
                  print('attributes:%s'%dicts)
                  return super().__new__(cls,name,bases,dicts)
         def __init__(cls,name,beses,dicts):
                  print('init class %s'%name)
                  print('attributes:%s'%dicts)
                  super().__init__(name,bases,dicts)

class SubMetaClass(MetaClass):
         def __new__(cls,name,bases,dicts):
                  print('new class %s'%name)
                  print('attributes:%s'%dicts)
                  return super().__new__(cls,name,bases,dicts)
         def __init__(cls,name,bases,dicts):
                  print('init class%s'%name)
                  print('attributes:%s'%dicts)
                  super().__init__(name,bases,dicts)

print('------define test class')

class TestClass(object):
         print('enter test class body')

         __metaclass__=MetaClass
         attr=1

         def method(self):
                  pass
         print('---create test class body')

print('---create test onject---')

TestClass()
print('---define test sub class')

class TestSubClass(TestClass):
         print('enter test sub class body')

         __metaclass__=SubMetaClass
         attr=2

         def method2(self):
                  pass
         print('exist test sub class body')

print('---create test sub object')

TestSubClass()
