n=int(input())
i=0
dec=0
while n>0:
    r=n%10
    dec=dec+r*(8**i)
    n=n//10
    i=i+1
m=dec
bin=''
while m>0:
    r=m%2
    bin=str(r)+bin
    m=m//2
print(bin)    

