## Another Simple Program.
## Program after filling the array that compose of 2018 numbers (more than 1 and less than 9999)
## selects numbers. These numbers in hexadecimal-digit form have the same end like in decimal-didigt usual form.
## The minimum of these numbers is a result.

import random

a = [] # Created empty array.
       # Therefore program automatically fills numbers 
N = 2018 # Amount numbers in array

for i in range(0, N): # "Auto" cicle
    a.append(random.randint(1, 9999))

di_16 = [] # Created the array for numbers that
           # ends like the same numbers in hexadecimal-digit

for i in list(a): # Running in the first array
    digit16 = list(hex(i)) # Translated in a list for 
    i_new = list(str(i))   # simple extraction the ends
    if i_new[-1] == digit16[-1]: # If the last digits are equal then..
        di_16.append(i) 
    else: # "else" only for structure.
        pass
    
print(min(di_16)) # Outputs minimum of their
