# Customer Segmentation App

## Usage 
This project provides an interactive Dash web application for performing customer segmentation on retail purchase data. It leverages KMeans clustering on three key features: Recency, Frequency, and Monetary, to help analyze customer behavior. The app enables users to explore the data, adjust clustering parameters, and dynamically visualize segmentation results.

## Features
1. Data Inspection
   - Explore the distribution of Recency, Frequency, and Monetary features for a selected country.
   - Visualizations include histograms, scatter plots, and box plots.
2. Cluster Evaluation
   - Compute Inertia Errors and Silhouette Scores for different numbers of clusters.
   - Help select the most suitable number of clusters for the KMeans model.
3. Segmentation Visualization-
   - Visualize the final customer segments using:
       2D Scatter Plot (after PCA reduction)
       3D Scatter Plot

## Dataset
- Online Retail.csv contains transactional data used for segmentation.
- Key features used for clustering:
  Recency: Days since last purchase
  Frequency: Number of purchases
  Monetary: Total spent
