#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import libraries 

# Data manipulation
import pandas as pd

# Numerical operations
import numpy as np
import scipy as sp
import scipy.stats as st

# Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid", {'axes.grid' : False})

# Statistics
from statsmodels.distributions.empirical_distribution import ECDF
import statsmodels.api as sm


# In[5]:


# Confirm directory 'Figures'

import os
if not os.path.exists('Figures'):
    os.makedirs('Figures')


# In[6]:


# Read the data

earthquake_df = pd.read_csv('earthquakes_US_14Jul−13Aug_2018.csv') 
earthquake_df.head()


# In[20]:


earthquake_df.info()


# In[21]:


# Summary of numerical statistics

earthquake_df.describe()


# In[22]:


# Missing data

earthquake_df.isnull().sum()


# In[ ]:


# Handling missing data using dropping and imputation methods 
# Dropping column 'horizontalError' 

earthquake_df.drop(columns=['horizontalError'], inplace=True)


# In[26]:


# Mean and median imputation

earthquake_df['magError'].fillna(earthquake_df['magError'].mean(), inplace=True)
earthquake_df['magNst'].fillna(earthquake_df['magNst'].median(), inplace=True)


# In[27]:


earthquake_df['nst'].fillna(earthquake_df['nst'].mean(), inplace=True)
earthquake_df['dmin'].fillna(earthquake_df['dmin'].mean(), inplace=True)


# In[28]:


# Final check

earthquake_df.isnull().sum()


# In[29]:


# Verify cleaned data

earthquake_df.info()
earthquake_df.describe()


# In[30]:


#Univariate dataset of the magnitudes

magnitudes = earthquake_df.mag


# In[36]:


# Setting plot dimensions
widthInInches = 8.5
heightInInches = 4
plt.figure( figsize=(widthInInches, heightInInches) )

kdeAxes = sns.kdeplot( magnitudes, color="black", label="Kernel Density")
sns.histplot( magnitudes, stat="density", color = "lightsteelblue", label="Histogram"  )

# Rug plot
sns.rugplot( magnitudes, label="Rug Plot" )

# Labels
plt.xlabel('Earthquake Magnitude')
plt.ylabel('Estimated Density')

# Tick marks & axes limit
plt.xticks((0,1,2,3,4,5))
plt.xlim([0,5])
plt.legend()
plt.tight_layout()

plt.savefig('Figures/earth_distplot.pdf')
plt.show()


# In[38]:


meanMagnitude = np.mean(magnitudes)
medianMagnitude = np.median(magnitudes)
varianceMagnitude = np.var(magnitudes, ddof=1)  # Sample variance
print(f"Mean: {meanMagnitude}, Median: {medianMagnitude}, Variance: {varianceMagnitude}")


# In[39]:


# Measures of central tendency 

meanMagnitude = np.mean(magnitudes)
medianMagnitude = np.median(magnitudes)

kdeX, kdeY = kdeAxes.get_lines()[0].get_data()
kdeYLimits = kdeAxes.get_ylim()
kdeYMax = kdeYLimits[1]
posOfMax = 0 
maxSoFar = kdeY[0] 
for j in range(len(kdeY)):
    if( kdeY[j] > maxSoFar ):
        posOfMax = j
        maxSoFar = kdeY[j]
        
magnitudeMode = kdeX[posOfMax]


# In[40]:


# Plot dimensions
plt.figure( figsize=(widthInInches, heightInInches) )

# Kernel density estimate curve
plt.plot(kdeX, kdeY, '-k')

xx = np.ones(2)
yy = np.array([0, kdeYMax])

# Vertical lines for the measures of central tendency

plt.plot( meanMagnitude*xx, yy,'--b',label='Mean')
plt.plot( medianMagnitude*xx, yy,'-.r',label='Median')
plt.plot( magnitudeMode*xx, yy,':m',label='KDE-estimated Mode')

# Labels & tick marks
plt.xlabel('Earthquake Magnitude')
plt.ylabel('Estimated Density')
plt.ylim(kdeYLimits)
plt.xlim([0,5])
plt.xticks((0,1,2,3,4,5))

plt.legend()
plt.tight_layout()

plt.savefig('Figures/earth_central.pdf')
plt.show()


# In[43]:


# Geospatial Analysis
# Create scatter plot of earthquakes by latitude and longitude
# Color-coded by magnitude (mag)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='longitude', y='latitude', hue='mag', size='mag', 
                sizes=(20, 200), palette='coolwarm', data=earthquake_df, legend=True)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geospatial Distribution of Earthquakes (Color-coded by Magnitude)')

plt.legend(title="Magnitude")

plt.tight_layout()
plt.show()


# In[ ]:




