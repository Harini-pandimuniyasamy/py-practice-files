n=int(input())
n1=int(str(n)[::-1])
if(int(str(n*n)[::-1])==n1*n1):
    print("Adam number")
else:
    print("Not adam")
