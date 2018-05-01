# Bana Mortality

**Data Mining 4502 Final Project**

**Team Members:** Alex Ray, Bryan Brent, Austin Pearman, Nathan Lile

**Description:**
<p>This project serves to provide a better understanding of mortality,
particularly with respect to the interrelationships between day-of-
death and historical features such as race, sex, date, age, education,
and circumstance of death in the United States from 2005 to 2015.
The US Centers for Disease Control and Prevention releases ex-
tensive mortality data every year to allow for a variety of census
analyses for life expectancy and death statistics, among other uses.
Our project will serve as a study of binary and multiclass classifi-
cation techniques on mortality data, primarily using decision trees.
Prior work with similar datasets has achieved mixed results with a
number of algorithms including random forests and naive bayes;
we hope to perform a novel survey of classification techniques for
manner of death using a variety of day-of-death attributes of the
deceased. In addition to evaluating the performance of decision
trees and random forests with binary and multiclass classification,
we hope to utilize the interpretability of the decision tree classi-
fier to gain insight into attribute importances in mortality-related
classification tasks.
Finally, this project will delve into utilizing unsupervised learn-
ing techniques such as K-means to potentially gain insight into
interesting patterns and trends of mortality in the US.
This work hopes to utilize common computational methods
and attributes to gain context into the manner of death. Using the
concept of feature importance, we seek to connect classification
results to existing knowledge on the demographics of suicide and
murder and by doing so add to the general body of literature on
the subject. Furthermore, results and feature importances can then
be used in a number of practical applications.</p>

___
**Summary of Questions and Answers:**
<p>Given CDC data on mortality in the United States from 2005 to 2015,
which provides day-of-death data such as cause, age, education
level, race, and marital status, we will initially attempt to predict
the manner of death. Manner of death includes categories such as
suicide, homicide, accidental, etc. We will be assessing classification
success given only day-of-death information as well as performance with historical features and specific details of the death such as
activity (at the time of death), location of injury as well as their
family and descendant status.
Depending on the success of these initial manner of death pre-
diction tasks, this project will also attempt to predict cause of death
using the same attributes. Due to the specificity of cause of death
in the data, this classification task also requires a preprocessing
step to "roll up" the cause of death into meaningful supergroups.
In theory, this work would allow for a more in-depth analysis of
characteristics of individuals "at risk" for different manners and
causes of death; given this information, various forms of govern-
ment programs, social work, and other support systems may be
able to adapt their methodologies.
Finally, we will be attempting to cluster mortality features to
recognize interesting patterns or trends. This exploratory analysis
affords an opportunity to potentially uncover novel interrelation-
ships between attributes in the dataset as well as assess the "com-
pleteness" of the existing feature-set. If notable "holes" in attributes
are found, it is possible to integrate past temporal data into the
existing dataset–market trends and weather data are examples of
readily available data ready to be integrated.
Interesting patterns would–like the supervised learning analysis–
provide further context regarding what constitutes an individual
with notable risk of some manner of death. Even a relatively unsuc-
cessful analysis as determined by quantitative evaluation metrics
provides insight into what sorts of features or attributes are neces-
sary to meaningfully predict or cluster mortality events. </p>

___
**Related Work:**
<p>The Kaggle page for the CDC mortality dataset being used in this
paper is a good resource for research questions, discussion on rele-
vant topics, and a repository of existing non-academic work. For
example, the main overview page contains interesting ideas on
expanding previous work through increasing granularity in age
data.
The discussion page contains useful threads on dealing with
cause of death recodes (a significant part of our project goals).
Discussions also include interesting, specific prior work using this
dataset including clustering and predictive analyses.
Finally, the kernel page contains a curated, ranked list of prior
work with this dataset. These provide examples of previous work,
examples of handling a variety of cleaning and preprocessing steps
in Python, and examples of analyses with varying levels of success
and interestingness. [6]</p>

___
**Lessons learned from data mining WHO
mortality database (Paoin W):**
<p>Previous studies of the CDC’s mortality database have provided
a template for the most effective data mining methods. Past re-
searchers have concluded that, due to the issues mentioned in our
problem statement, classification was generally ineffective for pre-
dicting cause of death.
The study cites a lack of correlation between variables and death
cause as the root of the issue. On the contrary, it was found that
clustering as well as association produced the most interesting
patterns. The exact quote from the study can be found below:
"Classification tools produced the poorest results in predicting
cause of death. Given the inadequacy of variables in the WHO
database, creation of a classification model to predict specific cause
of death was impossible. Clustering and association tools yielded
interesting results that could be used to identify new areas of in-
terest in mortality data analysis. This can be used in data mining
analysis to help solve some quality problems in mortality data."
[8]. Our analysis hopes to elaborate on these classification findings
by introducing algorithms beyond decision trees and naive bayes.
Furthermore, we hope to emulate the prior success of unsupervised
learning techniques on this sort of data.</p>

___
**CDC NVSS (National Vital Statistics
System) Publication Page:**
<p>This is the publication page for our database. It contains a list of
studies that have been previously done with regards to the CDCs
mortality data. We will be using this as a reference for selecting
our clustering and association techniques. It has provided us with
a roadmap for what does and doesn’t work in terms of analyzing
CDC mortality data. [3]</p>

___
**Applying data mining in medical data with
focus on mortality related to accident in
children:**
<p>This study used data mining techniques and was seeking conclu-
sions in line with our objectives. The researchers achieved results
regarding classifying mortality rate with both decision trees as well
as Bayes’ theorem. We intend to use their methods as examples of
possible techniques in our analysis. [9]</p>

___
**DATASET:**
<p>We will be using the CDC mortality dataset [6]. The dataset contains
data extensive data about deaths in the United States from 2005-
2015. The data is compiled yearly by the CDC in the National Vital
Statistics system.
All deaths are accompanied by a wide array of attributes in-
cluding both day-of-death attributes as well as historical and back-
ground features about the individual. In this analysis, we limit our
scope to the following attributes:
(1) age, given as an integer year
(2) race, given as a complex set of recodes. These will be dis-
cussed further in the techniques section.
(3) education level, given as one of two recodes. To be elab-
orated on further in techniques.
(4) month of death, given as an integer between 1 and 12.
(5) manner of death, given as one of:
(a) Accident
(b) Suicide
(c) Homicide
(d) Pending investigation
(e) Could not determine
(f) Self-Inflicted
(g) Natural
Limiting the analysis to this subset of features is first and fore-
most necessary given the size of the dataset. We do not have the
time or computational power to run many of the models we describe
with many more features included. Note that due to limited time,
we consider dimensionality reduction techniques such as Principle
Component Analysis (PCA) to be out of scope of this project.</p>

___
**TECHNIQUES:**
<p>Pandas. Will be utilized for all data analysis and manipu-
lation unless need arises for more powerful tools.
Pandas provides intuitive and easy to use helper functions for
data manipulation, analysis, and cleaning. Pandas dataframes afford
powerful summarization and correlation tools as well as useful
preprocessing functionality such as interpolation.
Scikit-learn. Scikit-learn provides a wide array of machine
learning models and tools. These tools include but are not limited to
classification and clustering algorithms, vectorization algorithms,
and preprocessing algorithms like principal component analysis.
(1) GridSearchCv We leveraged GridsearchCV in all of our bi-
nary classification tasks, an library that methodically eval-
uates every combination of algorithm parameters specified
by the user and also performs k-fold cross validation.
(2) ROC tools in Scikit-learn were utilized to calculate ROC AUC
values and product ROC curves [1].
(3) LogisticRegression for performing multiclass logisitic re-
gression.
(4) DecisionTreeClassifier for performing analyses with de-
cision trees.
4.1.3 Matplotlib. For simple visualizations such as scatter plots,
box and whisker plots, and histograms. Note that Pandas integrates
Matplotlib to provide a simple plotting interface for dataframes.</p>

___
**Data cleaning:**
<p>(1) Several areas in the json files are of an incorrect syntax, es-
sentially missing quotation marks. This will require a hands
on reformatting of the database source.
(2) Converting "recodes" to a more usable format.
(a) age is likely already at a suitable point without factoring
in some of the more granular age recodes. This feature
does not have missing values.
(b) race has a large number of recodes in addition to the
normal "race" feature. This race feature, while not missing
any values, is much too granular for our purposes in and
of itself. It separates into white and black, about 10 Asian
races, and "other". As will be discussed later, we are also
looking to limit the number of features to aid computation
time; thus, we limit our analysis to considering white,
black, Asian, and other (considered to be Hispanic).
(c) education has a flag indicating which of two recode columns
is relevant for the given instance, if any. This flag feature
has no missing values and can therefore be used to com-
bine these features into a single column.
(d) manner_of_death has many missing values. Due to the
size of the dataset, we can remove all instances without
reported manner of death. Furthermore, we need not con-
sider some listed manner of death values as they do not
appear in the dataset. Finally, depending on the classifica-
tion task, we binarize the manner of death values.
(3) Ensuring continuity of feature representation and format
across the entire database.
(a) Attributes such as sex are converted from binary string
values (’M’ and ’F’) into a single numerical binary feature
binary_male to allow for a traditional analysis without
extra vectorization.</p>

___
**Data Preprocessing:**
<p>(1) Identifying extraneous attributes that we can drop from the
study before we begin analysis. Particularly for initial classi-
fication tasks, the analyses begin with a very limited number
of attributes to avoid excessive computation time.
(2) Joining features to decrease dataset complexity while main-
taining continuity and information integrity. Examples of
this were introduced in section 3.1–combining many race
options as well as multiple recodes into four meaningful
categories vastly simplifies the analysis.</p>

___
**Suicide Binary Classification with Decision
Trees:**
<p>Our first classification task is to attempt to classify whether or
not a death was a suicide or not. We begin our analysis with deci-
sion trees using Scikit-learn’s DecisionTreeClassifier. Decision
trees are computationally efficient, relatively performant, and ex-
tremely interpretable which make them great choices for initial
stabs at classifying data. As discussed previously, a recurring con-
sideration throughout this analysis is the computational efficiency
of our models due to the number of instances in the dataset. Fur-
thermore, performance on decision trees affords the ability to make
an informed decision regarding whether or not to delve into more
complex binary classification algorithms such as support vector
machines.
Note that for this analysis, only instances with a reported manner
of death were included. Also note that even with this caveat, this
is a relatively unbalanced binary classification task as the positive
class (suicide) is only 17.3% of the data with reported manner of
death.</p>
<p>Feature Importances. To get a better "feel" for the data
as well as better understand the preprocessed features, Decision
TreeClassifier has a feature_importances_ attribute. From
the official Scikit-learn documentation, "The importance of a fea-
ture is computed as the (normalized) total reduction of the criterion
brought by that feature. It is also known as the Gini importance."
A larger number corresponds to a more important feature when
making the final classification. This table was generated with a de-
cision tree with a maximum depth of 10 on a suicide vs non-suicide
binary classification problem.detail_age–the numeric age attribute–is obviously the most
important feature when classifying suicide vs. non-suicide deaths.
Furthermore, education is the next most important feature, fol-
lowed closely by binary "black" and "male" attributes. All other
features are significantly less important.</p>
<p>Binary Classification Suicide vs Non-Suicide. Results from
classifying suicide vs non-suicide deaths using the features listed
above are as follows. As adjusting the maximum depth (known as
"pruning" the decision tree) is the main way to adjust overfitting
with decision trees, we chose this as the main hyperparameter to
adjust in GridSearchCV to find the most performant model.
Once the grid search of parameter combinations is complete, we
can then fit the a model with the highest scoring combination of
hyperparameters based on any one of a variety of scoring metrics,
for our purposes we chose roc_auc (Reciever Operating Charac-
teristics Area Under the Curve).
Accuracy as a scoring metric does not lend itself to our classifica-
tion task due to the unbalanced class distribution in the dataset (as
discussed previously, instances with suicide as the manner of death
are a significant minority); this skewed distribution leads to artifi-
cially inflated accuracy scores. For example, if 98% of all instances
are the positive label in a binary classification task, guessing the
positive label every time will result in 98% accuracy.
roc_auc is a better model scoring metric as it is known as a
class distribution independent metric. This is because the metric is
simply the area under the true-positive-rate vs false-positive-rate
curve; these values remain stable regardless of skewed distributions.
Furthermore, the Scikit-learn documentation states that "this imple-
mentation is restricted to the binary classification task or multilabel
classification task in label indicator format." which is exactly what
we were looking to accomplish.
This figure presents the mean training roc_auc and the mean
testing roc_auc as a function of the prescribed maximum depth of the decision tree. These averages were calculated using 3-fold cross
validation with GridSearchCV, on 80% of the total instances.
Furthermore, it makes sense that as we "unprune" the tree, test-
ing accuracy gets worse and training accuracy gets better–the
model is able to fit better to the training data, which makes it less
generalizable to new data.
We can now present the test accuracy with the GridSearchCV
"best estimator" on the held-out 20% of the dataset.This ROC curve also shows very good classification performance
on the test data. As mentioned previously, because increasing or de-
creasing the proportion of positives in the set would proportionally
increase both the false positive and the true positive rate equally,
this metric is more class distribution-agnostic than accuracy alone.</p>

___
**Multiclass Classification with Decision
Trees**
<p>Having seen good performance classifying suicide vs non-suicide
using decision trees, we can now extend our analysis to attempt to
classify all manners of death in our dataset. Note that the recode defines more than are listed, but the additional ones do not show
up in practice. Now, instead of making all non-suicide values 0 and suicide
values 1 we can leave the original encoding and run the same
analysis as before using a DecisionTreeClassifier.
Feature importances for the multiclass decision tree look very
similar to binary, though they’re even more skewed towards age.
Just as we did for binary classification, we can explore the perfor-
mance of this classifier with ROC curves. Scikit-learn’s ROC func-
tions do not accept "real" multiclass problems; however, this prob-
lem can be avoided by using a One-vs-Rest classification scheme
where n binary classifiers are trained to classify each class against
all others. Note that in the interest of computational runtime, this
One-vs-Rest analysis does not utilize GridSearchCV for hyperpa-
rameter tuning or cross validation; all classifiers are trained with a
maximum depth of 10, due to the results from the suicide vs non
suicide classification task in section 5.1. Note that the ROC curves for multiclass – because One-vs-Rest
was necessary – is not showing the same information as results
for a single multiclass decision tree. This is essentially 6 separate
binary classification tasks, and the AUC score for suicide reflects
that as it is the same as the AUC score for binary suicide vs non
suicide with a maximum depth of 10.
In general, the further away from the main diagonal the better
performance of the classifier. While interpreting results of multi-
class classification is non-trivial, it makes sense that the two largest classes in terms of number of instances had the smallest area under
the curve (AUC). Being the broadest categories, intuitively it would
be hardest to distinguish instances of those classes from all others.
To expand on this multiclass analysis, we can investigate feature
importances for the One vs Rest classifier–see Appendix A for
results.
Another avenue of approach for this multiclass task is to uti-
lize random forest decision trees in an attempt to see the perfor-
mance differences observed when using a ensemble classification
method, specifically scikit-learn’s RandomForestClassifier when
compared to the One-vs-Rest approach.
As we can see from Figure 7, the multiclass random forest estima-
tor performed similarly to the One vs Rest approach in Appendix A,
with some oddities with the ’pending investigation’ cause of death.
Interestingly enough, it appears that the random forest preformed
ever so slightly worse against the same test-set when compared to
the decision tree classifier, however these results are only marginal.
These preliminary results seem to confirm previously cited chal-
lenges with multi-class classification models for mortality specific
datasets. An additional benefit of utilizing a random forest instead of many
binary classifiers for multiclass classification is the ability to take
a look at feature importances from a statistical viewpoint, namely
looking at variance. Figure 8 shows the feature importances along
with error bars for the random forest multiclass classifier.
Clearly, the two multiclass models both effectively assert that age
is the most important feature when considering splitting criteria
for manner of death.</p>

___
**Homicide and Decision Trees:**
<p>An interesting note from both of the multiclass ROC curves is
the relative performance of the "Homicide" class against all others.
Homicide doesn’t have the lowest or highest number of instances
of all classes and roc_auc works well for skewed data, so there
must something else causing such good results. We can repeat our
previous binary classification analysis steps with Homicide instead
of suicide.
First, we again run GridSearchCV with a decision tree classifier
using 3-fold cross validation. As before, the grid search is looking for
optimal hyperparameter combinations, and in this case we present
results while only varying maximum depth of the decision tree.
Clearly, the same classifier performs significantly better when
classifying homicides vs non-homicides when compared to classify-
ing suicides vs non-suicides, based on the mean training and testing
accuracy curves produced by GridSearchCV. This result is corrobo-
rated when producing an ROC curve using the best estimator from
figure 10.
The ROC area under the curve value for murder vs non-murder
on the held-out test data is 0.938, whereas the area under the curve
value for the same data looking at suicide vs non-suicide is 0.880.
This is a relatively large difference in classification performance,particularly as both experiments end up choosing the same maxi-
mum depth value.
The question then becomes why is the binary murder classifica-
tion task so much more successful than others? Looking back to
feature importances, we can see that a plausible explanation for this
performance increase may lie in the notable increase in importance
in the binary_black feature compared to our previous analysis. When presented as a bar chart, the differences between feature
importances with suicide and feature importances with homicide
become more clear.
As will be discussed more in later sections, the importance of
binary_black with the murder classification task is more than
double that of the suicide task. This is interesting as it confirms
existing knowledge on the demographics of violent crime (see future
sections for more detail) and also speaks to the utility of feature
importance as a metric for information extraction.
We can look more into the relative feature importances of murder
against suicide and see that age plays a lesser role in classification,
which also matches existing intuition.
</p>
___
**K-Means Cluster Analysis:**
<p>As we began to delve into the realm of unsupervised learning, we
took note of the previous literature on this issue. As opposed to
classification, which had been previously proven to be ineffective,
clustering was said to have yielded interesting results.
The recodes that have been done previous to our preprocessing as
well as those done by our team have made replicating those results
difficult. Recodes, while fantastic for classication, made for unvaried
data that led to hard to interpret clusters. This was especially true
when trying to cluster on binary variables, which often led to
clusters with centroids that lied exactly at the 0 or 1 mark for the
attribute in question.</p>
<p>
It was this challenge that led to our rationale on which attributes
would be the most interesting to cluster on. The first obvious choice
was age due to the fact that we had mortality data from infancy to
beyond the 100 year mark. The next was month of death. Month,
while significantly more varied than our binary recodes, still only
contained twelve codes as opposed to the 100+ in the age attribute.
After finding interesting attributes to cluster on, we had to decide
how many clusters we would need in order to produce interesting
results. This was relatively easy using Scikit-learn’s score tool,
which assigns a score based on the variance as indicated by the
number of clusters. Note that the score on the y-axis is scaled
by 1e18, indicating a remarkably high distance between cluster
members and the centroid and centroid:
The performance of this score calculation limited us to testing up
to 6 clusters. That being said, it is clear that the variance levels off at
three clusters, with little increase in score with additional clusters,
after a sharp leveling at 2 centroids. For that reason, we began
clustering between Age and Month of Death with three centroids:
Our goal was to identify distinct groups in the dataset. We would
then be able to use these groups to analyze patterns and perhaps
draw conclusions about new objects based on which cluster they
belong to.</p>
<p>
The above scatter plot demonstrates some of the issues we had
while finding suitable attributes to cluster on. Ideally, we would
see three distinct clusters, with high inter-class dissimilarity and
high intra-class similarity between clusters. These clusters appear
to have little significance with low inter-class dissimilarity and low
intra-class similarity. This is unsurprising given our poor scores in
Figure 12.
The lack of distinct clusters in our dataset made our scatter plots
difficult to interpret and therefore unsuitable for pattern analysis.
What we do learn from this graph is that age and month of death
have no noticeable correlation, implying that age cannot be used
as an accurate predictor of time of death to any more of a specific
degree than the year.
Given our difficulties with clustering attributes, potentially due
to the lack of variety in the recodes, we decided we may need
to increase the dimensionality of our analysis in order to draw
interesting conclusions. To this end, we added the Manner of Death
attribute to our cluster analysis:
As before, we see little to no correlation between any of the three
attributes and little distinction between clusters. Although, scatter
plot analysis brought to light an interesting lack in correlation
between our attributes, making R-squared analysis a worthwhile
research topic.
</p>

___
**R-squared analysis:**
<p>Due to the lack of correlation seen in scatter plots, it led to the
assumption that the attributes in our dataset are poorly correlated.
To verify this assumption, we generated a table showing the R-
squared values between what we believed to be our most interesting
attributes:
From the above, it is obvious that the majority of our attributes
are only loosely correlated. Even in the case of our strongest corre-
lation, that of manner of death and age, only 8.5% of the variance
can be explained by the model.
The clustered scatter plot between the two most highly correlated
attributes can be seen below:
</p>

___
**Results:**
<p>ROC AUC Discussion: 
	In general, our binary classifiers managed to score fairly well and
produce good ROC curves, the two being suicide, scoring (0.88)
and homicide, with scores ranging from (0.93) to (0.94). We were
surprised to learn that according to the Caspian Journal of Internal
Medicine, that it is generally accepted in the field of medicine in
order to be considered medically plausible, a test must achieve an
ROC score of (0.95) or higher. This helped to put the precision of
our results into better perspective, informing us that our results
appear to be of high quality. [2]</p>
<p>
Verifying challenges with classification: 
One of the most notable, all be it less interesting, pieces of informa-
tion gathered from our results are general validation of previous
finding. many of our results corroborated previously stated chal-
lenges in using classification to find correlation between to the
day-of-death and historical features such as race, sex, date, age, edu-
cation, and circumstance of death. Additionally, we found that due
to common best practices in pre-processing the data for usability
also negatively effected unsupervised clustering attempts at finding
meaningful correlation between these features.
</p>
<p>Feature importance and ROC score in
Binary Classification:
While we have may have not been able to offer meaningful in-
sight into multi-dimensional correlation, results from our binary
classifier did yield potentially interesting data. When binary classi-
fication was used to classify cause of death against a wide variety
of other attributes, at least two broad patterns emerged. Firstly,
upon examining feature importance with suicide as the cause of
death (in our findings, the number 3 reported cause of death after
Accident and Natural), we observed that the age of the individual,
(appx. 0.7275) scored more than seven times as high as the next
highest feature, education (appx. 0.0965). When scoring ROC for Suicide, the binary classifier achieved reasonable results reaching a
max score of (0.879).
Similarly, when we drilled down and isolated homicide as the
cause of death, just after suicide in terms of total number of reported
deaths, we again observed that age scored highest (appx. 0.4677) and
binary_black second (appx. 0.2143) in terms of feature importance.
While we were not able to directly correlate these features in terms
of heavily weighted predictors for cause of homicide deaths. When
scoring ROC, homicide scored very well, achieving a max score of
(0.94).
</p>
<p>Feature importance and ROC score in
Multi-Class Classification:
Decision Tree Multi-Class. In an effort to cross validate
the Binary classification findings of our Decision tree, our next
models incorporated a multi-class classification approach to the
data using, again, Decision tree classifiers and Random Forests. As
with the binary classification using decisions trees, we scored our
results using ROC curves for the same reasons already mentioned.
We found with our milti-class Decision tree classifier surprisingly
also found detail_age the feature of highest scoring importance in
general across all causes of death(0.88). It is of interest to note that
this score exceeds any feature importance score from our binary
classifier. Additionally, the multi-class Decision tree ROC score
for suicide scored slightly better (0.88) then the ROC score for the
single tree (0.879) though the scores are so close as to be negligible.
For scoring homicide as the cause of death, the multi-class decision
tree performed substantially better then other features scoring a
peak ROC score of (0.94). Not only is this score 6 percentage points
higher then the next best scoring feature, suicide at (0.88). Another
observation of interest from the multi-class decision tree’s ROC
score is that homicide starts out as far and away the best scoring
feature, peaks the soonest and has a very shallow plateau-decline,
remaining better scoring the other features nearly across the board.


Random Forests Multi-Class. In an effort to optimize our
results from our successful multi-class Decision Tree classifier,
we next tested our data against a GridsearchCV optimized Ran-
dom_Forest classifier with a max depth of 10. We were surprised
to find that nearly across the board, ROC scores either fell or re-
mained constant. Many of the features remained in the same order
when organized by highest ROC score compared with the Deci-
sion_tree classifier, with Homicide and Suicide receiving the top
scores (0.91) and (0.87) respectively. The Pending_investigation
feature fluctuated most drastically, falling (0.09) points in the Ran-
dom_forest classifier (0.77) compared to the Decision_tree clas-
sifier (0.86). Additionally, the Pending_investigation feature was
the only feature in the multi-class model to suffer a sharp sud-
den decline in ROC score, as seen in Figure 6, (specifically in the
False-positive range of 0.4 to appx. 0.75) before rising sharply to
rejoin the other features at the end of the ROC curve. Given our
limited time, we were unable to come to any firm conclusions as
to why the Random_forest multi-class classifier reacted to dras-
tically different with this particular feature over other classifier
models, although it may warrant further in-depth analysis. In terms of feature importance, our Random_forest multi-class classifier cor-
roborated previous classifiers valuation of detail_age as the most
highly scored feature of the dataset, scoring this feature in the mid
to high (0.80’s). While precise feature importance score was not
plausible for Random_forests, when graphing the feature impor-
tance, we provided error bars based on the Gaussian distribution
over the various individual trees inside the forest. We can, therefore,
offer an accurate range and likely median value for the score of
the feature importance of our Random_forest multi-class classifier.
Based on the overall worse performance of the Random_forest in
addition to the lack of precision in scoring the feature importance,
we concluded that Random_forest classifiers would not provide any
benefit over Decision_trees for a usable multi-class classifier.
</p>
<p>
K-means Clustering:
While K-Means clustering failed to produce easy to analyze clusters,
we were able to analyze why this method may have been ineffective
for us and offer some potential next steps if this method were to be
attempted again on this dataset. As indicated by our unacceptably
high variance within the clusters, the lack of distinctness between
clusters, as well as our difficult to interpret plots, our method and
dataset (post pre-processing) were unsuitable. Future work in re-
gards to clustering on this dataset will more than likely require
a different preprocessing process than the one that was able to
produce intersting results in classification. Binary attributes will
not be suitable for cluster analysis. Furthermore, the rest of the
attributes as a whole will require a higher degree of variety in order
to produce interesting clusters.
Another potential avenue for improving cluster analysis may be
to utilize sampling. The high number of objects resulted in plots
loaded with datapoints. This made it difficult to draw meaningful
conclusions. Effective sampling as well as increasing the variety
in our attributes could very well be the next step in producing
interesting results.	
</p>
<p>Comparing findings:
Suicide. After discovering the apparent importance of
distinctive features in both suicide and homicide, we wanted to see if
other researchers had observed similar results. Research conducted
by the Suicide Prevention Resource Center over a very similar time
period and geography to our own study (Suicide rates with respect
to age in the USA from 2000 to 2016) seem to come to verify the
feature importance of age in respect to suicide as the cause of
death. In figures 15 and 16, we see both the reported suicide rates of
Americans per 100,000 in various age groups from 2000 to 2016 and
the ranking of suicide, in respect to the top 10 leading cause of death
in the same age groups over the same time period. As illustrated
particularly clearly in figure 16,the ranking of suicide as a top 10
leading cause of death, age appears to be of high importance for a
majority of the age ranges. [4]

Homicide. Looking into work done surrounding the im-
portance of age and homicide as cause of death, a 28 year longitudi-
nal study by the USA Bureau of Justice looking at homicide trends
in the USA from 1980 to 2008 offered similar results to our study. As
seen in figure 17, both age and race were prominent features with
respect to the victims of homicide also supporting our finding that race coded as black_binary presented itself as the highest scoring
race identifier with respect to victims of homicide.
</p>
___
**Application of Leanred Knolwedge:**
While we have been unable to provide strong evidence or mean-
ingful correlation between the features we explored and cause of
death, our finding do suggest strong feature importance of age in
both suicide and homicide, with the addition of race scoring high
as an important feature with respect to homicide. To further qual-
ify and support our results, and given that our findings seem to
agree with independent studies conducted on similar trends, we
can firstly conclude that these are well documented trends and
are generally widely accepted prior to our work. Therefore, in lieu
of specific actionable steps, we offer broader application of these
findings. Since there are clear and persistent findings of age being
of high importance with respect to suicide and both age and race
exhibiting high feature importance when homicide is the cause
of death, we believe that greater research must be done to drill into both these areas in an attempt to explore deeper correlations
and trends potentially within these areas. In terms of broad ac-
tionable steps, the fact that age seems to be the highest weighted
feature in suicide deaths, and suicide is a high cause of death in the
United States, this information should be more widely publicized
throughout general media. Secondly, individuals in positions of
trust, parents, teachers, caretakers and legal guardians, should be
made aware of the seeming importance age plays with respect to
suicide related deaths.[7]

___
**Refrences:**
[1] [n. d.]. ROC Curve Example Scikit-learn. ([n. d.]). Retrieved April 8, 2018
from http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#
sphx-glr-auto-examples-model-selection-plot-roc-py
[2] 2013. Receiver Operating Characteristic (ROC) Curve Analysis for Medical
Diagnostic Test Evaluation. (2013). Retrieved March 27, 2018 from https:
//www.ncbi.nlm.nih.gov/pmc/articles/PMC3755824/
[3] 2015. NVSS - Mortality Data. (2015). Retrieved March 2, 2018 from https:
//www.cdc.gov/nchs/nvss/deaths.htm
[4] 2016. Suicide Rates by age, USA 2000 to 2016. (2016). Retrieved March 22, 2018
from https://www.sprc.org/scope/age/
[5] 2017. Mortality Trends in the United States, 1900-2015. (2017). Retrieved March
5, 2018 from https://www.cdc.gov/nchs/data-visualization/mortality-trends/
[6] 2018. Death in the United States. (2018). Retrieved March 5, 2018 from https:
//www.kaggle.com/cdc/mortality/kernels
[7] Bureau of Justice Statistics 2008. Homicide Trends in the United States, 1980-2008.
(2008). Retrieved March 22, 2018 from https://www.bjs.gov/content/pub/pdf/
htus8008/
[8] W. Paoin. 2011. Lessons Learned from Data Mining of WHO Mortality Database.
Methods of Information in Medicine 50, 4 (jun 2011), 380–385. https://doi.org/10.
3414/me10-02-0019
[9] M. H. Saraee, Z. Ehghaghi, H. Meamarzadeh, and B. Zibanezhad. 2008. Applying
data mining in medical data with focus on mortality related to accident in children.
In 2008 IEEE International Multitopic Conference. 160–164. https://doi.org/10.1109/
INMIC.2008.4777728

###### This project used the following dataset provided by the CDC: https://www.kaggle.com/cdc/mortality/data

