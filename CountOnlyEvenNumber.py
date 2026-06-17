n=329652
s=0
while(n):
    a=n%10
    if(a%2==0):
       s=s+1
    n=n//10
print(s)
