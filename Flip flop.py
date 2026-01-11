def flip_flop(x):
    y=len(x)-1
    o=0
    while(o<y):
        if(x[o]!=x[y]):
            return('Your list;',x,'is not the same when turned around.')
        o+=1
        y-=1
    return('Your list;',x,'is the same when turned around.')

r=(1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1)
print('\n\n',flip_flop(r))