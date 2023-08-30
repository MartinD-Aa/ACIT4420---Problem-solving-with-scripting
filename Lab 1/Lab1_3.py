total = 1000
i = 0
sum=0
while(i < total):
    if(i%5==0):
        sum+=i
        i+=1
    elif(i%3==0):
        sum+=i
        i+=1
    else:
        i+=1

print(sum)