import torch
from torch.utils.data import DataLoader, Dataset


class TabularDataset(Dataset):
    def __init__(self, df, feature_cols, target_col):
        self.features = df[feature_cols].values
        self.labels = df[target_col].values

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        x = torch.tensor(self.features[idx], dtype=torch.float32)
        y = torch.tensor(self.labels[idx], dtype=torch.float32)
        return x, y
