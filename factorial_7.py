def fac(x):
    if x==0 or x==1 :
        return 1
    else:
        return x*fac(x-1)
    
l=[7,5,3]
for i in l:
    print(fac(i))
