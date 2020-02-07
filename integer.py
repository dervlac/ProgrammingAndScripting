

x=int(input("please enter an integer: "))
print(x)
y = 2
while y != 1:
    #if x==1:
        #print(int(x)
    if x%2==0:
        x=x/2
        print(int(x))
    elif x%2==1 and x>2:
        x=(x*3)+1
        print(int(x))
    else:
        y=x
print (int(x))
