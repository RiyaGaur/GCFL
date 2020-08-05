n=int(input())
sum=7
if(n==1):
    print(sum)
else:
    for i in range(1,n):
        sum = (sum * 2) + i
    print(sum)
    
