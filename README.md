7006SCN – Machine Learning and Big Data
Predicting Arrest Outcomes Using Scalable Distributed ML on Chicago Crime Data

Project Overview:

This project implements a scalable distributed machine learning pipeline using PySpark to predict arrest outcomes from the Chicago Crime dataset (2001–Present), which exceeds 1GB in size.

Due to the dataset scale, a distributed Spark-based approach was used for data ingestion, preprocessing, feature engineering, model training, evaluation, and scalability analysis.

The project demonstrates both machine learning performance and distributed systems optimisation.

objectives:

Implement distributed data engineering using PySpark

Train multiple MLlib classification models

Compare distributed models with a Scikit-learn baseline

Conduct strong and weak scaling experiments

Optimise joins using broadcast strategy

Tune shuffle partitions for performance

Develop Tableau dashboards for business insights

Dataset

Source: City of Chicago Data Portal
Dataset: Crimes – 2001 to Present
Size: >1GB
Target Variable: Arrest

Features include temporal, spatial, and categorical crime attributes.

Technologies Used

Apache Spark (PySpark)

Databricks

MLlib

Scikit-learn

Pandas

Tableau

Python 3


Models Implemented

Logistic Regression (Spark MLlib)

Decision Tree (Spark MLlib)

Random Forest (Spark MLlib)

Gradient Boosting (Scikit-learn baseline)

Primary evaluation metric: AUC (Area Under ROC Curve)


Scalability Analysis

Strong Scaling (200, 400, 800 partitions)

Weak Scaling (Small, Medium, Large datasets)

Broadcast vs Normal Join comparison

Physical execution plan analysis


Tableau Dashboards

Interactive dashboards available here:

https://public.tableau.com/app/profile/siddesh.gangadharappa/vizzes

GitHub Repository

https://github.com/Siddesh2508/7006SCN_coursework_siddesh

Ethical Consideration

Crime prediction systems may reflect historical bias. Future work should incorporate fairness-aware machine learning and bias evaluation techniques.

Author

Siddesh Gangadharappa
7006SCN – Machine Learning and Big Data



























