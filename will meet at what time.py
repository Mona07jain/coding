
d=float(input('enter initial distance'))
a=float(input('enter speed'))
b=float(input('enter speed'))

print ('will_meet')
if a>b and d>0:
 time_to_meet=d/(a-b)
 print('will meet in '+str(time_to_meet)+'second')
else:
     print('will not meet')


    


