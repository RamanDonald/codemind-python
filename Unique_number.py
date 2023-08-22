n=int(input())
k=str(n);
l=[]
for i in range(len(k)):
    r=n%10
    if r not in l:
        l.append(r);
    n=n//10
if(len(k)==len(l)):
    print("Unique Number")
else:
    print("Not Unique Number")