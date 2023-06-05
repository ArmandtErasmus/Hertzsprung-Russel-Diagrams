#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas, math, numpy and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# suppress warnings (to clear up the notebook)
import warnings
warnings.filterwarnings('ignore')


# In[3]:


# load the hipparcos star astronomy catalog: (European Space Agency's astrometric satellite , Hipparcos)
hipparcos_df = pd.read_csv("hipparcos.csv")


# In[4]:


# view the first five entries of the dataframe
hipparcos_df.head()


# In[5]:


# create a subset of the required columns, Vmag, B-V, Plx, r_Vmag
hipp_df = hipparcos_df[['Vmag', 'Plx', 'r_Vmag', 'B-V']]
hipp_df


# In[6]:


# remove rows containing NaN values from the dataframe
hipp_clean = hipp_df.dropna()


# In[7]:


# Calculate the absolute magnitudes using vectorized operations
hr_diagrams_data = pd.DataFrame({
    'Vmag': hipp_clean['Vmag'],
    'Plx': hipp_clean['Plx'],
    'r_Vmag': hipp_clean['r_Vmag'],
    'B-V': hipp_clean['B-V'],
    'Mv': hipp_clean['Vmag'] + 5 * np.log10(hipp_clean['Plx']/10)
})

# Calculate the luminosity using the absolute magnitudes
hr_diagrams_data['Luminosity'] = 10 ** ((4.83 - hr_diagrams_data['Mv']) / 2.5)


# In[8]:


# view the first five entries of the final dataframe
hr_diagrams_data.head()


# In[11]:


# create a scatter plot of the HR diagram
plt.figure(figsize=(10, 6))
plt.scatter(hr_diagrams_data['B-V'], hr_diagrams_data['Mv'], c=hr_diagrams_data['Luminosity'], cmap='plasma', alpha=0.6, s=5)

# set plot labels and title
plt.xlabel('B-V Colour')
plt.ylabel('Absolute Magnitude (Mv)')
plt.title('Hertzsprung-Russell Diagram')

# add a colorbar to indicate luminosity
cbar = plt.colorbar()
cbar.set_label('Luminosity')

# invert the y-axis to show brighter stars at the top
plt.gca().invert_yaxis()

# Show the plot
plt.show()

