n=list(map(int,input().split()))
l=len(n)
s=0
for i in range(l):
    if(n[i]%2==0):
        s=s+n[i]
print(s)
