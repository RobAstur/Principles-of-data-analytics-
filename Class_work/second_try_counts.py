import numpy as np
roll = np.random.randint(1,7, 100)
a = roll[0:10]
print(a)

# unique values in the data set. shows 
print(np.unique(a))
print(np.unique(a,return_counts=True))

# bar chart
d, counts = np.unique(a,return_counts=True)

print(d,counts)
import matplotlib.pyplot as plt
plt.bar(d,counts)