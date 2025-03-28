import torch
from torch import nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, input_channel, num_class):
        super(Net, self).__init__()
        self.classes = num_class

        self.conv1 = nn.Conv2d(input_channel, 8, 3, 1)
        self.conv2 = nn.Conv2d(8, 16, 3, 1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(3, 3)
        self.dropout = nn.Dropout(0.3)

        self.fc1 = nn.Linear(64, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, self.classes)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)

        return x
    
class MLTNet(nn.Module):
    def __init__(self, input_channel, num_class):
        super(MLTNet, self).__init__()
        self.classes = num_class

        self.conv1 = nn.Conv2d(input_channel, 8, 3, 1)
        self.conv2 = nn.Conv2d(8, 16, 3, 1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(3, 3)
        self.dropout = nn.Dropout(0.3)

        self.fc1 = nn.Linear(64, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, self.classes[0])
        self.fc4 = nn.Linear(128, self.classes[1])

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x1 = self.fc3(x)
        x2 = self.fc4(x)

        return x1, x2