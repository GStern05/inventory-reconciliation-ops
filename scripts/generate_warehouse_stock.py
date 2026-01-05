import pandas as pd
data = {
  "sku_id": ["SKU001", "SKU002", "SKU003","SKU004","SKU005"],
  "warehouse_quantity": [10, 10, 10,10,10]
}

df0 = pd.DataFrame(data)
df1 = pd.read_csv("data/raw/transactions_20260101.csv")
print(df1)
n = df1.shape[0]
for i in range (0,n):
    if df1.loc[i, "system"] == 'warehouse':
        if df1.loc[i,"event_type"] == 'order': #orders
            sku = df1.loc[i, "sku_id"]
            qty = df1.loc[i, "quantity"]
            df0.loc[df0["sku_id"] == sku, "warehouse_quantity"] -= qty   
        elif df1.loc[i,"event_type"] == "return": 
            sku = df1.loc[i, "sku_id"]
            qty = df1.loc[i, "quantity"]
            df0.loc[df0["sku_id"] == sku, "warehouse_quantity"] += qty  


df0.to_csv("data/raw/warehouse_stock_20260101.csv", index= False)


