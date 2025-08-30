import math
import io
import base64

import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline


from database import load_data

data = load_data()

class GraphBuilder:

    def __init__(
        self,
        data = data
    ):
        self.data = data

    def build_graph(self, country, graph_type):

        coun_data = self.data.get_country(country)
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))

        if graph_type == "Histogram":
            ax[0].hist(coun_data["Recency [days since last purchases]"], bins=10, color='skyblue')
            ax[0].set_title(f"Recency [days since last purchases] in {country}")

            ax[1].hist(coun_data["Frequency [times purchased]"], bins=10, color='orange')
            ax[1].set_title(f"Frequency [times purchased] in {country}")

            ax[2].hist(coun_data["Total Spent"], bins=10, color='green')
            ax[2].set_title(f"Total Spent in {country}")

            plt.suptitle(f'Histogram of Feature Distribution in {country}')
            plt.tight_layout()

        elif graph_type == "Scatter Plot":
            ax[0].scatter(coun_data["Recency [days since last purchases]"], coun_data["Frequency [times purchased]"], color='skyblue')
            ax[0].set_title(f"Recency vs Frequency in {country}")
            ax[0].set_xlabel("Recency [days since last purchases]")
            ax[0].set_ylabel("Frequency [times purchased]")

            ax[1].scatter(coun_data["Recency [days since last purchases]"], coun_data["Total Spent"], color='orange')
            ax[1].set_title(f"Recency vs Total Spent in {country}")
            ax[1].set_xlabel("Recency [days since last purchases]")
            ax[1].set_ylabel("Total Spent")

            ax[2].scatter(coun_data["Frequency [times purchased]"], coun_data["Total Spent"], color='green')
            ax[2].set_title(f"Frequency vs Total Spent in {country}")
            ax[2].set_xlabel("Frequency [times purchased]")
            ax[2].set_ylabel("Total Spent")

            plt.suptitle(f'Scatter Plots of Features Distribution in {country}')
            plt.tight_layout()
        
        else:
            sns.boxplot(y=coun_data["Recency [days since last purchases]"], ax=ax[0], color='skyblue')
            ax[0].set_title(f"Recency [days since last purchases] in {country}")

            sns.boxplot(y=coun_data["Frequency [times purchased]"], ax=ax[1], color='orange')
            ax[1].set_title(f"Frequency [times purchased] in {country}")

            sns.boxplot(y=coun_data["Total Spent"], ax=ax[2], color='green')
            ax[2].set_title(f"Total Spent in {country}")

            plt.suptitle(f'Box plot of Feature Distribution in {country}')
            plt.tight_layout()
        

        # save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        # encode to base64
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        
        # Return Figure
        return img_base64
    
    def scoring(self, n_clusters):
        X = self.data.train_data()

        inertia_errors = []
        silhouette_scores = []

        for n in n_clusters:
            model = make_pipeline(
                StandardScaler(),
                KMeans(n_clusters=n, random_state=42)
            )
            model.fit(X)
            inertia_errors.append(model.named_steps["kmeans"].inertia_)
            silhouette_scores.append(silhouette_score(X, model.named_steps["kmeans"].labels_))
    
        return inertia_errors, silhouette_scores
    
    def line_plot(self, range):
        inertia_errors, silhouette_scores = self.scoring(n_clusters=range)

        fig, ax = plt.subplots(1, 2, figsize=(8, 4))

        ax[0].plot(
            range, 
            inertia_errors, 
            marker='o'
            )
        ax[0].set_title("Inertia Error vs Number of clusters")
        ax[0].set_xlabel("Number of clusters")
        ax[0].set_ylabel("Sum of squared distances to cluster centroids")
        ax[0].grid(True)

        ax[1].plot(
            range, 
            silhouette_scores, 
            marker='o', 
            color='orange'
            )
        ax[1].set_title("Silhouette Score vs Number of clusters")
        ax[1].set_xlabel("Number of clusters")
        ax[1].set_ylabel("How well points fit in their clusters")
        ax[1].set_ylim(-1, 1)
        ax[1].grid(True)


        # save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        # encode to base64
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        return img_base64


    def labels(self, cluster_number):
        X = self.data.train_data()

        model = make_pipeline(
            StandardScaler(),
            KMeans(n_clusters=cluster_number, random_state=42)
        )
        model.fit(X)
        return model.named_steps["kmeans"].labels_
    
    def result(self, cluster_number, plot_type):
        X = self.data.train_data()
        labels = self.labels(cluster_number)
        if plot_type == "3D Scatter Plot":
            fig = px.scatter_3d(
                X, 
                x="Recency [days since last purchases]", 
                y="Frequency [times purchased]", 
                z="Total Spent", 
                color=labels.astype(str), 
                title="3D Scatter Plot of Clusters"
                )
            return fig
        else:
            pca = PCA(n_components=2)
            X_2 = pca.fit_transform(X)
            df_plot = pd.DataFrame(X_2, columns=["PCA1", "PCA2"])
            df_plot["Cluster"] = labels.astype(str)

            fig = px.scatter(
                df_plot, 
                x="PCA1", 
                y="PCA2", 
                color="Cluster", 
                title="2D Scatter Plot of Clusters after PCA"
                )
            return fig



        
        