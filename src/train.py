from pathlib import Path

import pandas as pd

from src.data.dataset import DataLoader, TabularDataset

DATA_DIR = Path().resolve().parent / "data"
train_csv = DATA_DIR / "raw" / "ml_ozon_сounterfeit_train.csv"
test_csv = DATA_DIR / "raw" / "ml_ozon_сounterfeit_test.csv"

df_train = pd.read_csv(train_csv, index_col=0)
df_test = pd.read_csv(test_csv, index_col=0)

FEATURE_COLUMNS = []

dataset = TabularDataset(df_train, FEATURE_COLUMNS, target_col="resolution")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
