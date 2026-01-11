import pandas as pd
from datetime import datetime

#sku_id is the specific product id.
# transaction_id represents a single business event (order, cancel, return)
# and may appear in multiple systems (website, warehouse).
transactions = [
    {
        "transaction_id": "T001",
        "sku_id": "SKU003",
        "event_type": "order",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 9,10),
        "system": "website"
    },
    {
        "transaction_id": "T002",
        "sku_id": "SKU001",
        "event_type": "order",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 10, 15),
        "system": "website"
    },
    {
    "transaction_id": "T002",
    "sku_id": "SKU001",
    "event_type": "order",
    "quantity": 1,
    "timestamp": datetime(2026, 1, 1, 23, 10),
    "system": "warehouse"
},
    {
        "transaction_id": "T002",
        "sku_id": "SKU001",
        "event_type": "cancel",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 10, 45),
        "system": "website"
    },
     {
    "transaction_id": "T005",
    "sku_id": "SKU002",
    "event_type": "order",
    "quantity": 2,
    "timestamp": datetime(2026, 1, 1, 18, 10),
    "system": "website"
},
    {
        "transaction_id": "T001",
        "sku_id": "SKU003",
        "event_type": "order",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 13,45),
        "system": "warehouse"
    },
    {
        "transaction_id": "T003",
        "sku_id": "SKU004",
        "event_type": "order",
        "quantity": 2,
        "timestamp": datetime(2026, 1, 1, 15,35),
        "system": "website"
    },
    {
        "transaction_id": "T003",
        "sku_id": "SKU004",
        "event_type": "order",
        "quantity": 2,
        "timestamp": datetime(2026, 1, 1, 15,45),
        "system": "warehouse"
    },
    {
        "transaction_id": "T004",
        "sku_id": "SKU005",
        "event_type": "return",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 16,00),
        "system": "warehouse"
    },
    {
        "transaction_id": "T004",
        "sku_id": "SKU005",
        "event_type": "return",
        "quantity": 1,
        "timestamp": datetime(2026, 1, 1, 16,20),
        "system": "website"
    },
    {
    "transaction_id": "T006",
    "sku_id": "SKU006",
    "event_type": "adjustment",
    "quantity": 1,
    "timestamp": datetime(2026, 1, 1, 19, 30),
    "system": "warehouse"
},


]

df = pd.DataFrame(transactions)
print(df)
df.to_csv("data/raw/transactions_20260101.csv", index=False)


