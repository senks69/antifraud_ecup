from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
train_csv = DATA_DIR / "raw" / "ml_ozon_сounterfeit_train.csv"
processed_csv = DATA_DIR / "processed" / "train.csv"


df_train = pd.read_csv(train_csv)
df = pd.DataFrame()


df["id"] = df_train["ItemID"]
df["percent_fake_returns"] = (
    df_train["item_count_fake_returns90"] / df_train["item_count_sales90"]
)
df["percent_fake_returns"] = df["percent_fake_returns"].fillna(0)
df["has_sales"] = (df_train["item_count_sales90"] > 0).astype(int)

df.to_csv(processed_csv)
