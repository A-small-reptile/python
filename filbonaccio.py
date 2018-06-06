def filbo():
         a,b=0,1
         while True:
                  num=(yield)
                  if num is None:
                           raise AttributeError('expected num>0')
                  else:
                           while num:
                                    a,b=b,a+b
                                    num-=1
                           print(b)
