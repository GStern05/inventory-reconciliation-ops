import pandas as pd
import numpy as np

#load the website and warehouse data
warehouse_stock = pd.read_csv("data/raw/warehouse_stock_20260101.csv")
website_stock = pd.read_csv("data/raw/website_stock_20260101.csv")

#merge the datasets on sku_id
joined = warehouse_stock.merge(
    website_stock,
    on="sku_id",
    how="left",
    validate="many_to_one"
)
#create a difference column
joined["difference"] = joined["warehouse_quantity"] - joined["website_quantity"]

#flag oversell and undersell risk
conditions = [
    joined["difference"] > 0,
    joined["difference"] < 0
]

choices = [
    "WAREHOUSE_HIGH",
    "WEBSITE_HIGH"
]

joined["flag"] = np.select(conditions, choices, default="OK")

print(joined)

joined.to_csv("data/processed/reconciliation_20260101.csv", index = False)
