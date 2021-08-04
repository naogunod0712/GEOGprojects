#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Code/ Framework for the sensitivty analysis
#Group 1


# In[ ]:


#Note the code is used as a framework to understand how programming can be used to perform sensitivity analysis, 
#however the results were subpar and will not be used as final consensus for the project.


# In[5]:


#import the raster
import rasterio
import rasterio.plot as pplt
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[6]:


#Open a raster file
c1=file_name =c3 =c4 = rasterio.open("C:/Users/Adeol/GEOG_481/country_raster_dataset.tif")


# In[7]:


#The name of the raster
file_name.name


# In[8]:


#import python modules 
from rasterio.plot import show


# In[9]:


#Show the raster file
show(file_name)


# In[10]:


# count of the bands in the image
print(c1.indexes)
print(file_name.indexes)
print(c3.indexes)
print(c4.indexes)


# In[11]:


#Read the raster file
band1 = file_name.read(1)
band2=c1.read(1)
band3=c3.read(1)
band4=c4.read(1)


# In[12]:


#show the array of it
band1


# In[13]:


#weightings to be used for the raster input

w = 0.5


# In[14]:


#Show the different rasters that have been stored
show(c1)
show(file_name)
show(c3)
show(c4)


# In[85]:


#weight class used, the [hazard weight, risk weight]
wgt_set = [1, 2,3,4]


# In[86]:


wgt_set[0]


# In[87]:


#Store the different rasters
rast_stack= [c1,file_name, c3, c4]


# In[88]:


#show the arrays
rast_stack[1].read(1)


# In[98]:


#loop to multiply different raster to each other
#four rasters where combined into one multiplied by the hazard and risk
size_raster= len(rast_stack)
for i in range(4):
        weighted_raster=rast_stack[i].read(1)
        set_w= wgt_set[i]
        total_raster=[weighted_raster*set_w]


# In[99]:


#show the arrays of after it has been looped
total_raster


# In[100]:


#show the combined the raster together
show(total_raster)


# In[ ]:




