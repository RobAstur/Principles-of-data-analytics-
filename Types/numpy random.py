import numpy as np

x = np.random.randint(1,7)
print(x)

#calculate average roll
y = np.random.randint(1,7, 100)
mean = np.mean(y)
standard_dev= np.std(y)
mediam = np.median(y)
print (y)
print(mean)
print(standard_dev)
print(mediam)