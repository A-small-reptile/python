class LoggedMappingMixin:
         __slots__=()

         def __getattr__(self,key):
                  print('Getting'  +str(key))
                  return super().__getitem__(key)

         def __setattr__(self,key,value):
                  print('setting {}={!r}'.format(key,value))
                  return super().__setattr__(key,value)

         def __delitem__(self,key):
                  print('deleting'+str(key))
                  return super().__delitem__(key)

class LoggedDict(LoggedMappingMixin,dict):
                  
         pass


                        
