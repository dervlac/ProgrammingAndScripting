###rverse a sentence
###then return every second character

x = str(input("Please type a sentence: "))
s1 = []
s2 = []
n = len(x)
for i in range(n):
    s1.append(x[n-i-1])
    
for j in range(n):
    if j%2==0:
        s2.append(s1[j])
print(s2)