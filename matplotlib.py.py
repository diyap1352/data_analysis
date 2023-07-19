#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib


# In[4]:


print(matplotlib.__version__)


# In[6]:


import matplotlib.pyplot as plt 
import numpy as np


# In[7]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d)
plt.show


# In[8]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d, linewidth = 2)
plt.show


# In[10]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.show


# In[11]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days')
plt.ylabel('Months')
plt.show


# In[12]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.show


# In[14]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.grid()
plt.show()


# In[15]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.grid(axis = 'y')
plt.show()


# In[16]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.grid(axis = 'x')
plt.show()


# In[21]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.grid(color = 'blue', linestyle = '--', linewidth = 1 )
plt.show()


# In[22]:


p = np.array([4,7,8,9])
d = np.array([3,7,8,10])
plt.plot(p,d,marker = '^',linewidth = 2,c = 'pink' , linestyle = '--')
plt.xlabel('Days', c = 'blue')
plt.ylabel('Months', c = 'blue')
plt.grid(color = 'blue', linestyle = '--', linewidth = 1 )
plt.show()


# In[25]:


#plot1
d = np.array([4,6,8,9])
s = np.array([7,1,4,3])
plt.subplot(1,2,1)
plt.plot(d,s,c= 'blue', ls = '--' , linewidth = 2)

#plot2
a = np.array([3,5,7,6])
b = np.array([4,7,1,2])
plt.subplot(1,2,2)
plt.plot(a,b,c = 'pink', ls = '--', linewidth = 2)

plt.show()


# In[28]:


#plot1
d = np.array([4,6,8,9])
s = np.array([7,1,4,3])
plt.subplot(2,3,1)
plt.plot(d,s,c= 'blue', ls = '--' , linewidth = 2)

#plot2
a = np.array([3,5,4,6])
b = np.array([4,2,1,2])
plt.subplot(2,3,2)
plt.plot(a,b,c = 'pink', ls = '--', linewidth = 2)

#plot3
c = np.array([1,5,7,6])
e = np.array([4,7,1,2])
plt.subplot(2,3,3)
plt.plot(c,e,c = 'orange', ls = '--', linewidth = 2)

#plot4
f = np.array([3,5,7,6])
h = np.array([4,7,1,5])
plt.subplot(2,3,4)
plt.plot(f,h,c = 'green', ls = '--', linewidth = 2)

#plot5
g = np.array([3,5,7,10])
i = np.array([4,7,1,2])
plt.subplot(2,3,5)
plt.plot(g,i,c = 'magenta', ls = '--', linewidth = 2)

#plot6
z = np.array([3,5,7,6])
y = np.array([4,7,12,2])
plt.subplot(2,3,6)
plt.plot(z,y,c = 'grey', ls = '--', linewidth = 2)




plt.show()


# In[29]:


#plot1
d = np.array([4,6,8,9])
s = np.array([7,1,4,3])
plt.subplot(2,1,1)
plt.plot(d,s,c= 'blue', ls = '--' , linewidth = 2)

#plot2
a = np.array([3,5,7,6])
b = np.array([4,7,1,2])
plt.subplot(2,1,2)
plt.plot(a,b,c = 'pink', ls = '--', linewidth = 2)

plt.show()


# In[ ]:




