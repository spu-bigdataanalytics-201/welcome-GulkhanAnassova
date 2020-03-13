#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)


# In[7]:


import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)


# In[8]:


$pip install scipy


# In[6]:


from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)


# In[9]:


from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)


# In[11]:


import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)


# In[12]:


import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)


# In[13]:


import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)


# In[14]:


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)


# In[15]:


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)


# In[17]:


import numpy
x = numpy.random.uniform(0.0, 5.0, 250)

print(x)


# In[18]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()


# In[19]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()


# In[20]:


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()


# In[21]:


import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


# In[26]:


import pandas
df = pandas.read_csv("cars.csv")
df


# In[29]:


import pandas
df = pandas.read_csv("cars.csv")
print(df)


# In[ ]:





# In[28]:


import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()


# In[30]:


import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


# In[ ]:





# In[ ]:




