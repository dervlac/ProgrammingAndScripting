

###Dervla Candon
####integers formula
###takes an integer and manipulates it depending on whether it is odd or even and returns the results
###repeate until 1 is reached  
x=int(input("please enter an integer: "))
print(x)        ##print the integer entered to begin with

while x != 1:       ##keeps repeating the process while the value is not one
    if x%2==0:      ##assesses if the number is even
        x=x/2       ##all even numbers are halved
        print(int(x))   ##new value is returned
    elif x%2==1:        ##indicates odd numbers, else may work too?
        x=(x*3)+1       ##trebles the number an adds one
        print(int(x))   ##new value is returned
##no further print is required - the algorithm will always get to 2, which still satisfies the while loop
##as 2 is even, it will be halved and 1 will be the result
##one will be returned, and the while loop is no longer true, so the algorithm ends.