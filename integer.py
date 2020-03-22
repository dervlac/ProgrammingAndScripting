

###Dervla Candon
####integers formula
###takes an integer and manipulates it depending on whether it is odd or even and returns the results
###repeated until 1 is reached 
###updated following feedback


x=int(input("please enter an integer: "))
print(x, end = " ")        ##print the integer entered to begin with

while x != 1:       ##keeps repeating the process while the value is not one
    if x%2==0:      ##assesses if the number is even
        x=x/2       ##all even numbers are halved     
    elif x%2==1:        ##indicates odd numbers, else may work too?
        x=(x*3)+1       ##trebles the number an adds one
    print(int(x), end=" ")   ##new value is returned
    
    ##print was previously duplicated within if statement
    ##reduced to 1 print outside if statement following feedback


##no further print is required - the algorithm will always get to 2, which still satisfies the while loop
##as 2 is even, it will be halved and 1 will be the result
##one will be returned, and the while loop is no longer true, so the algorithm ends.