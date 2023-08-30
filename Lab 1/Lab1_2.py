
amount= int(input("How many numbers do you have? "))
i=0
numbers=0
while(i < amount):
    numbers+=int(input("Give me one of them: "))
    i=i+1
average=numbers/amount
print("Your average is "+ str(average))
