import torch.nn as nn
import torch.nn.functional as F


class FCModel(nn.Module):

    def __init__(self, input_size, output_cnt, device):
        super(FCModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, output_cnt)
        self.device = device

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
