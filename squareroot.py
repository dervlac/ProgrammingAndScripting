### Dervla Candon
### Squareroot program using the function sqrt()

x = float(input("Please enter a positive number: "))
check1 = -1
##using a check value to allow for rerunning of the while loop
##in the event of user input of a negative number
import functions    ##for sqrt() function
while check1 < 0:
    if x < 0:
        print("This value is negative, please try again.")
        x = float(input("Please enter a positive number: "))
        ##no change to check value so that while loop will run again with new value for x
    else:
        print("\nThe squareroot of", x, "is", functions.sqrt(x), "\n")
        check1 = x  ##ends the while loop