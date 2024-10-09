# **Earthquake Dataset Analysis and EDA**

| Contents 											 	   	|
| -------- 											 	   	|
| [Project Overview](#Project-Overview)			   	|
| [Dataset Description](#Dataset-Description)			   	|
| [Analysis](#Analysis) 		   		|
| [Data Exploration](#Data-Exploration) 		   		|
| [Data Quality Assessment and Cleaning](#Data-Quality-Assessment-and-Cleaning)							|
| [Univariate Analysis of Earthquake Magnitudes](#Univariate-Analysis-of-Earthquake-Magnitudes)					   		|
| [Data Visualisation](#Data-Visualisation)						   	|
| [Summary of Derived Insight](#Summary-of-Derived-Insight)					|
| [Conclusion](#Conclusion)									|
| [Built with](#Built-with)							   		|

## Project Overview
This project represents an execution of an Exploratory Data Analysis (EDA) of earthquake data collated in the US between July 14th to August 13th, 2018. This EDA was performed with a view to exploring key statistical features of earthquake incidents and magnitudes, drawing valuable insight from the data, and presenting visualisations to aid the understanding of earthquake patterns in the US within the specified time period. 

## Dataset Description
The earthquake dataset used in this EDA, originally from United States Geological Survey (USGS), includes 22 columns representing attributes presented below (https://earthquake.usgs.gov/data/comcat/#meta-terms);

1.	time: timestamp of the earthquake occurrence generally recorded in UTC. 
2.	latitude: latitude of the earthquake location
3.	longitude: longitude of the earthquake location
4.	depth: the depth of the earthquake’s hypocentre measured in kilometres.
5.	mag: this attribute represents the magnitude of the earthquake, which measures the energy released. 
6.	magtype: this attribute communicates the type of magnitude measurement employed, such as ml for local magnitude. 
7.	nst: this attribute indicates the total number of seismic stations used to determine the earthquake location. 
8.	gap: gap column represents the azimuthal gap, reported in degrees, between the seismic stations around the epicentre. As a general rule, a smaller gap value is indicative of higher reliability while an azimuthal gap exceeding 180 degrees suggest higher uncertainties with regards location and depth.  
9.	dmin: the horizontal distance from the epicentre to the nearest seismic station. 
10.	rms: the root square mean travel time residual providing a measure of the fit of the observed arrival times to the predicted arrival times for this location. 
11.	net: this attribute identifies the data contributor, identifying the network providing information for the event. 
12.	id: the unique identifier for the event.
13.	updated: time the event was most recently updated.
14.	place: the textual description of named geographic region near to the event.
15.	type: this column conveys the type of seismic event such as earthquake, quarry blast, explosion. 
16.	horizontalError: the uncertainty of reported location of the event in kilometres. 
17.	depthError: This communicates the uncertainty of reported depth of the event in kilometres. 
18.	magError: the uncertainty of reported magnitude of the earthquake events, ie, the estimated standard error of the magnitude.         
19.	magNst: the total number of seismic stations used to calculate the magnitude of the earthquake.         
20.	status:  this attribute indicates the status of the product.       
21.	locationSource: the network that originally authored the reported location of this event.
22.	magSource:  the network that originally authored the reported magnitude for the event.

## Analysis
The analysis of the earthquake dataset includes the following key steps: 

### Data Exploration
Before performing the EDA, the dataset was explored to uncover its statistical properties and summaries. earthquake_df.head(), earthquake_df.info(), and earthquake_df.describe() were used to determine the data structure, properties, and to reveal the summary of numerical statistics. 

### Data Quality Assessment and Cleaning
The quality of the data, measured in terms of missing values, was assessed using earthquake_df.isnull().sum(). This revealed that columns ‘nst’, ‘dmin’, ‘horizontalError’, ‘magError’, and ‘magNst’ had missing data. This was handles using the following two approaches: 

#### Imputation
Missing values in ‘magError’, ‘nst’, and ‘dmin’ were handled using mean/ median imputation. Considering that the mean provides a good central tendency for the number of seismic stations and measurement error, mean imputation was used for the 148 and 119 missing values in ‘magError’ and ‘nst’ columns respectively. 
Mean imputation was equally used for handling the  38 missing values in ‘dmin’ column because it represents a continuous value which justifies its suitability for mean-based imputation. On the other hand, median imputation was used to handle the the ‘magNst’ column based on the fact that the attribute is a count-based variable (see dataset description) and the median is generally less sensitive to outliers than the mean. 

#### Dropping
The ‘horizontalError’ column contained 924 missing values, posing a significant risk to the overall quality of the analysis Since this column was not the focus of the EDA, it was dropped. 

### Univariate Analysis of Earthquake Magnitudes
Earthquake Magnitude Distribution: A Kernel Density Estimation (KDE) plot and histogram were plotted to provide visualisation of the distribution of earthquake magnitudes 
While the histogram presented an overview of the frequency distribution, the KDE curve provided insight into the probability density function. 

#### Central Tendency
A detailed analysis of the mean, median, and mode of the magnitudes was provided alongside, indicating the typical magnitude of this period. 

### Data Visualisation
3 major visualisations were created to provide a pictorial understanding of earthquake activity. 
1.	Magnitude Distribution: This visualisation aided a comparison between the histogram and KDE of earthquake magnitudes. 
2.	Central Tendency Visualisation: This plot provided an illustration of  the mean, median, and mode of magnitudes overlaid on the KDE curve. 
3.	Geospatial Analysis: Visualisation mapping the longitude and latitude of earthquakes was plotted to aid the identification of clusters of seismic activity in different regions. 

## Summary of Derived Insight
•	In this analysis, key statistical measures of the earthquake magnitudes were calculated to determine central tendency and variability of the earthquake magnitudes in the dataset.

•	The mean magnitude (0.9555) derived suggests that the earthquakes recorded had a magnitude slightly below 1, while the median magnitude (0.83) suggests that 50% of recorded event had magnitudes greater than 0.83 and the other 50% had magnitudes lower than 0.83.

•	The fact that the mean is higher than the median suggests that there might be a few high-magnitude earthquakes in the dataset, indicating a slight skew in the data.

•	The variance of magnitudes (0.4003) on the other hand suggests a moderate spread in the magnitude value.  

•	Although most earthquakes in the dataset are of low magnitude (below 2.4), the scatterplot presenting the result of the geospatial analysis suggests that certain areas may be more prone to intense seismic activity as indicated by the notable instances of higher magnitude of up to 4.0 scattered across the region. 

## Conclusion
This analysis provided valuable insights into the characteristics and distribution of earthquake magnitudes in the United States over the studied time period. The visualizations and statistics provide a clear understanding of earthquake behaviour, which could be useful for further research or predictive modeling. In addition, the geospatial analysis performed could be useful to identify areas prone to intense seismic activity to aid disaster preparedness and risk mitigation efforts.

## Built With:		
- JupyterLab	
- Python3	   	
- Pandas		
- Numpy			
- Matplotlib	
- Seaborn
- OS Module (os)


