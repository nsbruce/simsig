from torchsig.utils.dataset import SignalDataset
import torchsig.transforms as ST
import random
import numpy as np

class SigCLRDataset(SignalDataset):
    def __init__(self, dataset,transforms=None):
        self.dataset = dataset
        self.CLRTs=transforms
        self.n_views=2
        if self.CLRTs is None:
            self.CLRTs=[ST.Identity(),ST.Identity()]
        super().__init__(dataset)

    def __getitem__(self, idx):
        x, y = self.dataset[idx]
        smpld_tfs = random.sample(self.CLRTs, self.n_views)
        x1=ST.Compose([smpld_tfs[0],ST.ComplexTo2D()])(x)
        x2=ST.Compose([smpld_tfs[1],ST.ComplexTo2D()])(x)
        #return (x1["data"]["samples"].astype(np.float32), x2["data"]["samples"].astype(np.float32)),y
        return (x1.astype(np.float32), x2.astype(np.float32)),y

    def __len__(self) -> int:
        return len(self.dataset)
