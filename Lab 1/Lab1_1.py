name = input("What is your name? ")
cookies = int(input("How many cookies would you like to have? "))

print("Hello, " + name + "!")

if(cookies < 10 and cookies > 0):
    print("Are you sure it's enough?")
elif(cookies < 20 and cookies >= 10):
    print("I agree, cookies are delicious!")
elif(cookies < 50 and cookies >= 20):
    print("Be careful, it's getting too much!")
elif(cookies >= 50):
    print("No way, it's getting too much")
else:
    print("Something must be wrong, I'll give you 10 cookies")
    cookies = 10

i = 0
print("Here are your cookies:")
while i < cookies:
    print("Cookies")
    i=i+1
