#!/usr/bin/env python3.7
#

try:
#    a=1
    a=a+1 # NameError
#    print(try)
except Exception as er:
    print(111111, er)
    print(Exception('messages'))
except NameError as wer:
    print(wer)
except OSError as eee:
    print('ososos')
except:
    print(123123)
else:
    print(55555)
