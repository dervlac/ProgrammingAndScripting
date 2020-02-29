## Dervla Candon
## functions repository
## used to store all functions created from week 6 onwards

###function to calculate square root using newtons method
###using half of the input as the initial estimate
###stops iterating when runs of the iteration vary by less than or equal to 0.01

def sqrt(x):
    old_i = x/2
    tracker = 0
    new_i = x/2
    while abs(new_i - tracker) > 0.01:
        tracker = old_i
        new_i = 0.5*(old_i + (x/old_i))
        old_i = new_i
    return(round(new_i,1))

