daysOfTheWeek= ("Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# weeklyPlans=list([[""]*24]*7)
#Initialize the list
weeklyPlans=[["" for i in range(24)] for j in range(7)]

# Adds the activity to the day
def add_activity(day, time, activity):
    #Finds the index of the day and converts the time to an int
    dayIndex=daysOfTheWeek.index(day)
    hour= int(time)
    #Checks to see if the day and time is within the parametes. Then adds the activity if it is
    if 0 <= dayIndex < len(daysOfTheWeek) and 0 <= hour < 24:
        weeklyPlans[dayIndex][hour] = activity

# Lists out all the activities of the chosen day
def list_plans(day):
    # Finds the index of the day
    dayIndex = daysOfTheWeek.index(day)
    # Uses the day to find the list
    planner = weeklyPlans[dayIndex]
    # Goes through the list
    for id, i in enumerate(planner):
        #Prints out all the activities of the chosen day
        print( f"{id:02d}:00"+ f" {i}")

while True:
     print("s - Store plans \nl - list plans \nx - exit")
     action = input("Choose from the list: ")
     if action == "s":
         day = input("Which day? ")
         time = input("What time? ")
         activity = input("What is the plan? ")
         add_activity( day, time, activity)
     elif action == "l":
         day = input("Which day? ")
         list_plans(day)
     elif action == "x":
         print(weeklyPlans)
         break

