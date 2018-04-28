#!/bin/python
from datetime import datetime
odds = [ i  for i in range(1 , 60 , 2 ) ] 
print(odds)
right_this_min = datetime.today().minute

if right_this_min in odds:
	print("This min seems little odd")
else:
	print('Not an odd min')
