sum=0
avg=0
lst=[]
p=0
n=int(input("Enter number of elements"))
while p <n:
    for i in range(0,n):
        p=int(input("Enter elements"))
        lst.append(p)
        print("The list is",lst)
    for m in lst:
        sum = sum+m
        avg = (avg+m)/n
else:
    print("sum=",sum)
    print("avg=",avg)
    print("count=",n)
