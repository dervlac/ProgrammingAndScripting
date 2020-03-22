###Dervla Candon
### then return every second character of a sentence
### in reverse
### updated following feedback

x = str(input("Please type a sentence: "))  
## user input above is required to start
n = len(x) 
## using variable n to reduce clutter
## for loop cycles through each character in the input string
for i in range(n):
    ## below if loop means only every second character is printed
    if i%2==0:
        print(x[n-i-1], end="")
        ## end value means there is no line break between characters
  