import torch
from torch.utils.data import Dataset


class PlantDiseaseDataset(Dataset):

    def __init__(self, hf_dataset, transform=None):
        self.dataset = hf_dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]

        image = item["image"]
        label = item["class_idx"]

        if self.transform:
            image = self.transform(image)

        label = torch.tensor(
            label,
            dtype=torch.long
        )

        return image, label