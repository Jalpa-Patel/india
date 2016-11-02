
# coding: utf-8

# In[5]:


import math
import random
import matplotlib.pyplot as plt

# Function to Generate a random number sequence of 10 values between 0 to 90
def randomFunction(a):
    randNum = random.sample(range(0,90),a)
    return randNum

# Function to perform sine and cosine operation on generated random number and store it in sine and cosine array
def trigoFunction(numberArray):
    sineArray = [math.sin(r) for r in numberArray]
    cosineArray = [math.cos(r) for r in numberArray]
    return (sineArray,cosineArray)

# Calling Function
randomArray = randomFunction(10)
trigValues = trigoFunction(randomArray)

# Plot the sine and cosine values into graph with labeled axes and legend in two different color.
plt.plot(randomArray,trigValues[0], 'go')
plt.plot(randomArray,trigValues[1], 'bo')
plt.title('Scatter graph to plot Sine and Cosine values')
plt.xlabel('Random Number')
plt.ylabel('sine and cosine')
plt.show()

