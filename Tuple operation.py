Tuple1=('hi',3,6.7,False,"bye")
print('\n\n',Tuple1)

Tuple1=Tuple1+(9,)
print('The New Tuple1 is',Tuple1)

tuplex=(67,'five',9.0,2,50,60,False,67,41,92,67)
print('\nIn tuplex;',tuplex,'67 comes',tuplex.count(67),'times.')

Tuple3=(Tuple1+tuplex)
slice_=Tuple3[3:7]

print('Tuple3 is',Tuple3)
print('slice_ = Tuple3[3:7], so slice_ is',slice_)