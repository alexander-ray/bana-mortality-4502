# Bana Mortality -- Data Mining 4502 Final Project

## Team Members
### Alex Ray, Bryan Brent, Austin Pearman, Nathan Lile

## Description
<em>Abbreviated version of abstract.</em>

The goal of this project is to investigate mortality data from the CDC using a variety of classification and clustering methods, primarily decision trees. This analysis will primarily be focused on features of the deceased such as age, race, sex, month of death, and education level.

We use decision trees to perform a binary classification to predict whether or not an instance had their manner of death listed as suicide or not as well as whether or not the death was by homicide. This analysis was then expanded to One vs Rest multiclass classification with both decision trees and random forests. We broadly investigate relics of these computational tools in the form of feature importances to better understand the computational techniques as well as gain insight into the data.

Finally, we look into an unsupervised learning analysis using K-means. While this did not provide us with much information or insight, we present potential future avenues of work to further investigate unsupervised learning in the context of mortality data.

## Summary of Questions and Answers
<em>Conglomeration from final presentation and paper.</em>
<em>Given the mortality dataset:</em>
### Question 1
What is the effect of target class choice and number of target classes when attempting to predict manner of death?
### Answer 1
The effect is substantial, with classes such as homicide and suicide having significantly better performance using decision trees and random forests than other classes such as "accident". We hypothesize this is due to the presence of more useful, important features for these classes than other classes. Note that our multiclass analysis focuses on the One vs Rest approach, which is essentially agnostic to the number of target classes.

### Question 2
How can feature importances from decision trees and random forests be used as analytic tools?
### Answer 2
Feature importances from decision trees and random forests provide great insight into the performance of classifiers, context on the nature of the data, ideas and background for future research questions, and also significantly contribute to knowledge gained and the application of that knowledge. 
  
### Question 3
What interesting results can be gained from a clustering analysis?
### Answer 3
We were unable to achieve significant meaningful results from a cluster analysis with K-means. We assert that this is, in part, due to our one-hot encoding in the preprocessing for the classification analyses as well as the general lack of variety in features between instances. Furthermore, future work may be able to leverage additional features or non-distance based clustering methods such as DBSCAN.

## Applications of Knowledge
<em>Summary from final paper.</em>
1. Contribution to existing literature

   Our work, particularly binary suicide vs non-suicide and homicide vs non-homicide provides additional context and validation to existing social research and intuition surrounding these causes of mortality. Corroboration and exploration of existing work is an important and necessary part of academic advancement.
2. Proof of Concept for Social Work Applications

   This binary classification work, due to its relative success, can be viewed as a proof of concept for similar models integrated into social programs. These programs could use a similar model with additional contextual features to provide important resource and outreach targeting for at-risk groups. As is noted in the paper, this application would require extensive work from domain experts to ensure safety and privacy of groups in question.
3. Data Preprocessing Tool

   Our multiclass classification tool can be used as a basis for future work in the area of predicting manner of death from attributes of the deceased. Future work may be able to leverage this into a preprocessing tool for the CDC dataset; as mentioned in the paper, there were millions of instances without listed manner of deaths that were discarded so this model could be a suitable method for predicting manner of death. This would allow manner of death to be used as a feature in future analyses.
4. Demographic Risk Publicization

   Connecting back to the contribution to existing literature, this work and particularly the insights gained from feature importances can be used as additional resources to help publicize the existence and importance of acknowledging groups at risk of certain negative outcomes (such as suicide or homicide).

## Link to Video
[Video found here](23_AnalysisOfDeathInTheUS_Part5.swf)

## Link to Final Report
[Final report found here](23_AnalysisOfDeathInTheUS_Part4.pdf)

## References
1. [n. d.]. ROC Curve Example Scikit-learn. ([n. d.]). Retrieved April 8, 2018 from http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-auto-examples-model-selection-plot-roc-py

2. 2013. Receiver Operating Characteristic (ROC) Curve Analysis for Medical
Diagnostic Test Evaluation. (2013). Retrieved March 27, 2018 from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3755824/

3. 2015. NVSS - Mortality Data. (2015). Retrieved March 2, 2018 from https://www.cdc.gov/nchs/nvss/deaths.htm

4. 2016. Suicide Rates by age, USA 2000 to 2016. (2016). Retrieved March 22, 2018 from https://www.sprc.org/scope/age/

5. 2017. Mortality Trends in the United States, 1900-2015. (2017). Retrieved March 5, 2018 from https://www.cdc.gov/nchs/data-visualization/mortality-trends/

6. 2018. Death in the United States. (2018). Retrieved March 5, 2018 from https://www.kaggle.com/cdc/mortality/kernels

7. Bureau of Justice Statistics 2008. Homicide Trends in the United States, 1980-2008. (2008). Retrieved March 22, 2018 from https://www.bjs.gov/content/pub/pdf/htus8008/

8. W. Paoin. 2011. Lessons Learned from Data Mining of WHO Mortality Database. Methods of Information in Medicine 50, 4 (jun 2011), 380–385. https://doi.org/10.3414/me10-02-0019

9. M. H. Saraee, Z. Ehghaghi, H. Meamarzadeh, and B. Zibanezhad. 2008. Applying data mining in medical data with focus on mortality related to accident in children. In 2008 IEEE International Multitopic Conference. 160–164. https://doi.org/10.1109/INMIC.2008.4777728

###### This project used the following dataset provided by the CDC: https://www.kaggle.com/cdc/mortality/data

