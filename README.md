<img width="1903" height="472" alt="Ảnh chụp màn hình 2025-08-31 123537" src="https://github.com/user-attachments/assets/74bf9eaf-0a16-459f-a99a-c8f3877fec05" /># Customer Segmentation App

## Usage 
This project provides an interactive Dash web application for performing customer segmentation on retail purchase data. It leverages KMeans clustering on three key features: Recency, Frequency, and Monetary, to help analyze customer behavior. The app enables users to explore the data, adjust clustering parameters, and dynamically visualize segmentation results.

## Features
1. Data Inspection
   - Explore the distribution of Recency, Frequency, and Monetary features for a selected country.
   <img width="1903" height="653" alt="Ảnh chụp màn hình 2025-08-31 120106" src="https://github.com/user-attachments/assets/abb65418-ea87-4e2b-a1ca-a48b053ef638" />
   - Visualizations include histograms, scatter plots, and box plots.
   <img width="1901" height="480" alt="Ảnh chụp màn hình 2025-08-31 120149" src="https://github.com/user-attachments/assets/218e7133-e182-4260-be52-1fec9aa5a3ee" />
   <img width="1903" height="472" alt="Ảnh chụp màn hình 2025-08-31 123537" src="https://github.com/user-attachments/assets/99eb1db6-51f2-4d56-8322-d834b309a5e5" />
   <img width="1901" height="474" alt="Ảnh chụp màn hình 2025-08-31 120211" src="https://github.com/user-attachments/assets/1a3a7a62-1ea0-4280-af73-54231570d29d" />
2. Cluster Evaluation
   - Compute Inertia Errors and Silhouette Scores for different numbers of clusters. The users can choose the range of the cluster themselves.
   - Help select the most suitable number of clusters for the KMeans model.
   <img width="1906" height="917" alt="Ảnh chụp màn hình 2025-08-31 115916" src="https://github.com/user-attachments/assets/e4309525-019a-440f-b7af-71dd12939541" />
3. Segmentation Visualization-
   - Visualize the final customer segments using:
       2D Scatter Plot (after PCA reduction)
     <img width="1904" height="919" alt="Ảnh chụp màn hình 2025-08-31 120007" src="https://github.com/user-attachments/assets/486c2772-79df-424a-8fb7-e95245ab9972" />
       3D Scatter Plot
     <img width="1909" height="920" alt="Ảnh chụp màn hình 2025-08-31 120032" src="https://github.com/user-attachments/assets/0bd4dbaf-0f4f-4211-a5d9-1b3b5d97428b" />

## Dataset
- Online Retail.csv contains transactional data used for segmentation.
- Key features used for clustering:
  Recency: Days since last purchase
  Frequency: Number of purchases
  Monetary: Total spent
