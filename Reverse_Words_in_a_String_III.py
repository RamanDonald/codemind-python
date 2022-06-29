s=input()
c=s.split()
rev_l=[]
for ch in c:
    rev_l.append(ch[::-1])
d=' '.join(rev_l) 
print(d)