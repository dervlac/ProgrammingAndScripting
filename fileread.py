###Dervla Candon
###program will take filename from user input
###then read the file and count the number of occurences of the letter e
###and return this figure to the user


x = input("Please enter the file location: ")
with open(x,'r') as f:
    count = 0
    f.read()
    print(f.tell())
    for i in range(0,f.tell()+1):
        f.seek(i)   ###needs debugging
        ###this currently skips the first character
        if f.read(1) == 'e':
            count += 1
            #print("found an e!")
        elif f.read(1) == 'E':
            count +=1
    print("The letter e appears", count, "times in this file")
###works, provided the first character isnt an e/E, in which case it is 1 off