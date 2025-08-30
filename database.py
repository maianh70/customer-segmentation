import pandas as pd


# Tasks 7.4.5, 7.4.6, 7.4.9, 7.4.10
class load_data:
    """For connecting and interacting with MongoDB."""

    def __init__(
        self,
        database = r"C:\Users\Admin\cus_seg\Online Retail.csv"
    ):
    
        self.database = database
        

    def wrangle_data(self):
        df = pd.read_csv(self.database)

        #Drop na
        df.dropna(inplace=True)

        #M: total spent on each product
        df["Total Spent"] = df["Quantity"] * df["UnitPrice"]

        # Sum of spent of each customer
        df["Total_Spent_Summed"] = df.groupby(["InvoiceNo", "InvoiceDate", "CustomerID"])["Total Spent"].transform("sum")
        df["Total_Spent_Summed"] = df["Total_Spent_Summed"].round(2)

        #F: Frequency
        df["Frequency"] = df.groupby("CustomerID")["InvoiceNo"].transform("nunique")

        #R: Recency
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
        closest_date = df["InvoiceDate"].max()
        df["Recency [days since last purchases]"] = df.groupby("CustomerID")["InvoiceDate"].transform(lambda x: (closest_date - x.max()).days)

        # Drop unnecessaries
        df.drop(columns=["Description", "Quantity", "Total Spent", "UnitPrice","StockCode"], inplace=True)

        # Rename columns
        df.rename(columns={
            "CustomerID": "Customer ID", 
            "InvoiceNo": "Invoice No", 
            "InvoiceDate": "Invoice Date", 
            "Total_Spent_Summed": "Total Spent",
            "Frequency": "Frequency [times purchased]",
            }, 
            inplace=True)
        
        #Convert Customer ID
        df["Customer ID"] = df["Customer ID"].astype(str).str.split(".").str[0]

        #Drop duplicates
        df.drop_duplicates(inplace=True)

        df.reset_index(drop=True, inplace=True)

        return df
    

    def sample_data(self):
        df = self.wrangle_data().drop(columns=["Country"])
        df = df.sample(random_state=1, n=10)
        return df.to_dict('records')

    def country(self):
        df = self.wrangle_data()["Country"].sort_values().unique()        
        cols = df.tolist()
        return cols
    

    def get_country(self, country):
        df = self.wrangle_data()
        df = df[df["Country"] == country]
        return df
    
    def train_data(self):
        df = self.wrangle_data()
        df = df[["Recency [days since last purchases]", "Frequency [times purchased]", "Total Spent"]]
        return df
                    