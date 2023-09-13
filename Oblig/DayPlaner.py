#initializes the dictonary
weeklyPlans={}

def load():
    #opens file with the intent of reading the file
    with open("WeekPlans.txt", 'r') as file:
        #Reading the file line for line
        for line in file:
            #It strips the sentence of spaces and divides the sentence up into 4 pieces day, start, end, and desc from the delimiter provided. 
            day, start, end, desc = line.strip().split(",")
            #Adds the plan into the dictonary in the preferd format
            weeklyPlans[day] = (start, end, desc)

def save():
    #Opens file with the intent of writing or saving something onto the file
    with open("WeekPlans.txt", 'w') as file:
        #Goes through the dictonary and seperates all the values into 4 pieces
        for day, [start, end, desc] in weeklyPlans.items():
            #Writes the plan in the preferd format and saves
            file.write(f"{day},{start},{end},{desc}\n")

def add(day, start, end, description):
    #Adds the values into the dictonary in the preferd format
    weeklyPlans[day]=(start, end, description)

def show(day):
    print(f"\nYour plans for {day} is:")
    #Finds the day in the dictonary that you are looking for
    if day in weeklyPlans:
        #Splits the values into 3 pieces start, end, desc
        start_time, end_time, desc = weeklyPlans[day]
        if desc:
            print(f"{start_time} - {end_time}  {desc}\n")
    else:
        print(f"No plans found for {day}.")

while True:
    print("Choose: load, save, add, show or exit")
    action = input("Choose from the list: ")
    if action == "add":
        day = input("Which day? ").capitalize()
        start = input("When does it start? (HH:MM) ")
        end = input("When does ut end? (HH:MM) ")
        description = input("What is the plan? ")
        add(day, start, end, description)
    elif action == "load":
        load()
    elif action == "save":
        save()
    elif action == "show":
        day = input("Which day? ").capitalize()
        show(day)
    elif action == "exit":
        break
