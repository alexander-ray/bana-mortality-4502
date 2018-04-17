# Bana Mortality

**Data Mining 4502 Final Project**

**Team Members:** Alex Ray, Bryan Brent, Austin Pearman, Nathan Lile

**Description:**
<p>This project serves to provide a better understanding of mortality, particularly with respect to the interrelationships between day-of-death and historical features such as race, sex, date, age, education, and circumstance of death in the United States from 2005 to 2015. The US Centers for Disease Control and Prevention releases extensive mortality data every year to allow for a variety of census analyses for life expectancy and death statistics, among other uses.

Our project will serve as a study of classification techniques on mortality data. Prior work with similar datasets has achieved mixed results with a number of algorithms including random forests and naive bayes; we hope to perform a more comprehensive survey of classification techniques as well as better understand the affect of different attributes on classification performance.

Finally, this project will delve into utilizing unsupervised learning techniques such as K-means to potentially gain insight into interesting patterns and trends of mortality in the US. </p>
___
**Summary of Questions and Answers:**
<p>Given CDC data on mortality in the United States from 2005 to 2015, which provides day-of-death data such as cause, age, education level, race, and marital status, we will initially attempt to predict the manner of death. Manner of death includes categories such as suicide, homicide, accidental, etc. We will be assessing classification success given only day-of-death information as well as performance with historical features and specific details of the death such as activity (at the time of death), location of injury as well as their family and descendant status.	

Depending on the success of these initial manner of death prediction tasks, this project will also attempt to predict cause of death using the same attributes. Due to the specificity of cause of death in the data, this classification task also requires a preprocessing step to "roll up" the cause of death into meaningful supergroups. In theory, this work would allow for a more in-depth analysis of characteristics of individuals "at risk" for different manners and causes of death; given this information, various forms of government programs, social work, and other support systems may be able to adapt their methodologies.

Finally, we will be attempting to cluster mortality features to recognize interesting patterns or trends. This exploratory analysis affords an opportunity to potentially uncover novel interrelationships between attributes in the dataset as well as assess the "completeness" of the existing feature-set. If notable "holes" in attributes are found, it is possible to integrate past temporal data into the existing dataset--market trends and weather data are examples of readily available data ready to be integrated. </p>
___
**Application of Leanred Knolwedge:**
TBD
___
**Video Demonstration:**
TBD
___
**Final Project Paper:**
TBD
___
###### This project used the following dataset from provided by the CDC: https://www.kaggle.com/cdc/mortality/data

