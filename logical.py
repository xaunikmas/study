#logical ops : and, or, not 

temp = int(input("what is the temperature outside? "))

if temp > 15 and temp <= 30:
    print("it's good shiny day")
elif temp < 25 and temp > 10:
    print ("the temperature a bit cold today")
elif temp < 0 or temp < 10:
    print ("the temperature is quite cold today, stay inside and warm")