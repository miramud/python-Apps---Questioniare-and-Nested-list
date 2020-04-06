#REQUESTING FOR VALUE
val = input("Enter number of Cars to be generated: ")

#CHECK FOR EMPTINESS
while len(val) < 1:
    val = input("Ensure to enter a value: ")

#CHECK FOR VALIDITY OF THE NUMBER
#while val.isdigit == False 
#OR
while not val.isdigit():
    val = input("Please Ensure that value is a number: ")

#TYPECASTING TO INTEGER SINCE WE ARE SURE THAT 
# VALUE CAN NEVER BE NON-DIGIT AT THIS POINT
val = int(val)


#RUN COMPARISON (CHECKING IF NUMBER IS GREATER THAN 10 OR NEGATIVE)
while val > 10:
    val = input("Please enter a number less than 10: ")
    while not val.isdigit():
        val = input("Please input a number that must be less than 10: ")
    val = int(val)
    """ while val < 0:
        val = input("Please enter a non-negative number: ") """

print("You have chosen to generate {} cars".format(val))
# RUN OUR LOOP
counter = 0
cars = []


while counter < val:
    q = 0   # REINITIALIZING QUESTIONS TO BE ZERO, 
            # SO AS TO REPEAT THE QUESTIONS ALL OVER AGAIN

    car = []    # SINCE THE LIST "CAR" WILL BE ACCEPTING ITEMS FROM THIS LOOP,
                # WE DECLARE THE VARIALBLE FOR THE LIST INSIDE THE COUNTER LOOP

    while q < 3:    # DECLARE THE WHILE LOOP FOR THE QUESTIONS
        
        # q is 0 (WHICH IS THE FIRST INDEX FOR THE CAR[] LIST)

        temp_val = counter + 1
        name = input("Enter name of car {}: ".format(temp_val))
        car.append(name)
        while car[q].isdigit():
            car[q] = input("User must enter a string for car name {}: ".format(temp_val))
        
        q = q + 1   # q BECOMES 1 (WHICH IS THE NEXT INDEX FOR THE CAR[] LIST)

        model = input("Enter model of car {}: ".format(temp_val))
        car.append(model)
        while car[q].isdigit():
            car[q] = input("Please enter a string for car {} model: ".format(temp_val))
        
        q = q + 1   # q BECOMES 2 (WHICH IS THE NEXT INDEX FOR THE CAR[] LIST) 
        
        numberOfTyres = input("Enter number of tyres of car {}: ".format(temp_val))
        car.append(numberOfTyres)
        while not numberOfTyres.isdigit():
            numberOfTyres = input("Please input must be a number: ")
        
        q = q + 1   # q BECOMES 3 AND BREAKS THE LOOP FOR THE FIRST CAR,
                    # THEN ENTERS COUNTER LOOP WHERE IT COUNTER HAS INCREASED TO 1,
                    # THEN THE q BECOMES 0 AGAIN
        
        cars.append(car)    # APPEND THE FIRST LIST GENERATED INTO
                            # THE MAIN CONTAINER CARS[] LIST
                            # MOVE TO THE NEXT COUNTER LOOP

    counter = counter + 1   # REPEAT THE ABOVE PROCESSES FOR COUNTER IS LESS THAN VAL,
                            # UNTIL COUNTER BECOMES = VAL, THEN LOOP ENDS 
                            # AND BREAKS OUT INTO PRINTING                    

    print(car)
print(cars)    