import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
from scipy.interpolate import interp1d

delta_t = 0.01 # sample interval 
f = 1 # the frequency of the signal HZ

x = np.arange(0,1,delta_t) #make a vector from 0 to 1
y = np.sin(2*np.pi*f *(x)) 

def reconstruc(x_in,y_in,interval,instant_t):
    interval = Decimal(str(round(interval,15))) #Transform to Decimal for precision 
    x_in = [Decimal(str(round(i,15))) for i in x_in]#Transform to Decimal for precision 

    previousTime = 0
    x = []
    y = []

    y.append(y_in[0])
    x.append(x_in[0])

    for index, time in enumerate(x_in):
        if time - previousTime >= interval:#Do in every interval lapse and append
            previousTime = time
            x.append(time)
            y.append(y_in[index])

    x = [float(i) for i in x]

    interp_func = interp1d(x, y)#interpolation function, call with new x and returns with y
    value = interp_func(instant_t)
    return x,y,value

interval = 0.1 #Sampling time for reconstruction
instant_t =.9  #Instant t value
x_new,y_new,value = reconstruc(x,y,interval,instant_t) #Main function

# Initialise the subplot function using number of rows and columns
plt.subplot(2, 1, 1)
plt.plot(x,y, marker = 'o')
plt.title("Original Function")

plt.subplot(2, 1, 2)
plt.plot(x_new, y_new, marker = 'o', color = 'black')
plt.title("Reconstructed Function")

plt.show()

print(f"size of x is {len(x)}")
print(f"size of x_new is {len(x_new)}")
print(f"size of y is {len(y)}")
print(f"size of y_new is {len(y_new)}")
print(f"x_new is {x_new}")
print(f"y_new is {y_new}")
print(f"Value Ys for a given t is {value}")