
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[1]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[31]:

import matplotlib.animation as animation
get_ipython().magic('matplotlib notebook')

fig = plt.figure()

# Generate 16 subplots
sp1 = plt.subplot2grid((4,3),(0,0))
sp2 = plt.subplot2grid((4,3),(0,1))
sp3 = plt.subplot2grid((4,3),(0,2))
#sp4 = plt.subplot2grid((4,4),(0,3))
sp5 = plt.subplot2grid((4,3),(1,0))
sp6 = plt.subplot2grid((4,3),(1,1))
sp7 = plt.subplot2grid((4,3),(1,2))
#sp8 = plt.subplot2grid((4,4),(1,3))
sp9 = plt.subplot2grid((4,3),(2,0))
sp10 = plt.subplot2grid((4,3),(2,1))
sp11 = plt.subplot2grid((4,3),(2,2))
#sp12 = plt.subplot2grid((4,4),(2,3))
sp13 = plt.subplot2grid((4,3),(3,0))
sp14 = plt.subplot2grid((4,3),(3,1))
sp15 = plt.subplot2grid((4,3),(3,2))
#sp16 = plt.subplot2grid((4,4),(3,3))
    
plt.tight_layout()

n = 100

x11 = np.random.normal(-2.5, 1, 10000)
x22 = np.random.gamma(2, 1.5, 10000)
x33 = np.random.exponential(2, 10000)
x44 = np.random.uniform(0, 10, 10000)

def update(curr):
    
    if curr==n:
        a.event_source.stop()
    
    sp1.cla()
    sp2.cla()
    sp3.cla()
    sp5.cla()
    sp6.cla()
    sp7.cla()
    sp9.cla()
    sp10.cla()
    sp11.cla()
    sp13.cla()
    sp14.cla()
    sp15.cla()
    
    # Plot histograms in subplot
    sp1.hist(x11[0:curr], bins=6, color='blue')
    sp1.axis([-5,0,0,50])
    sp2.hist(x11[5000:5000+curr], bins=6, color='blue')
    sp2.axis([-5,0,0,50])
    sp3.hist(x11[9000:9000+curr], bins=6, color='blue')
    sp3.axis([-5,0,0,50])
    #sp4.hist(x11[9000:9500], bins=8)
    
    sp5.hist(x22[:curr], bins=6, color='red')
    sp5.axis([0,12,0,50])
    sp6.hist(x22[5000:5000+curr], bins=6, color='red')
    sp6.axis([0,12,0,50])
    sp7.hist(x22[9000:9000+curr], bins=6, color='red')
    sp7.axis([0,12,0,50])
    #sp8.hist(x22[:curr], bins=7)
    
    sp9.hist(x33[:curr], bins=6, color='green')
    sp9.axis([0,12,0,60])
    sp10.hist(x33[5000:5000+curr], bins=6, color='green')
    sp10.axis([0,12,0,60])
    sp11.hist(x33[9000:9000+curr], bins=6, color='green')
    sp11.axis([0,12,0,60])
    #sp12.hist(x33[:curr], bins=7)
    
    sp13.hist(x44[:curr], bins=6, color='black')
    sp13.axis([0,10,0,40])
    sp14.hist(x44[5000:5000+curr], bins=6, color='black')
    sp14.axis([0,10,0,40])
    sp15.hist(x44[9000:9000+curr], bins=6, color='black')
    sp15.axis([0,10,0,40])
    #sp16.hist(x44[:curr], bins=8)


a = animation.FuncAnimation(fig, update, interval=10)




