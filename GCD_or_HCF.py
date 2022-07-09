a,b=map(int,input().split())
if a>b:
    mn=b
else:
    mn=a
for i in range(1,mn+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)
        
    
    