###reverse a sentence
###then return every second character

x = str(input("Please type a sentence: "))  ##user input required to start
s1 = ""     ##two empty strings needed - one to reverse, then one to record every second character
s2 = ""  ##initial attempt was with lists, but strings returns the results in a better format
n = len(x)
for i in range(n):
    s1 += (x[n-i-1])     ##remove 1 as the count starts at zero, not one. removing i from n then counts down, rather than up
    
for j in range(n):
    if (j-1)%2==0:  #looks at every second character, starting with the first character s1[0]
        s2 += s1[j-1]       
print(s2)   ##returns the finished result