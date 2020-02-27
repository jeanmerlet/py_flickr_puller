import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Standard_CNN(nn.Module):

  def __init__(self):
    super(Net, self).__init__()

    # 3x3 kernels for each convolution
    # 3 input channels(r, g, b) for first convolution, 64 output channels
    self.conv1 = nn.Conv2d(3, 64, 3)
    # 64 input channels, 128 output channels
    self.conv2 = nn.Conv2d(64, 128 , 3)
    # 128 input channels, 256 output channels
    self.conv3 = nn.Conv2d(128, 256 , 3)
    # 256 input channels, 512 output channels
    self.conv4 = nn.Conv2d(256, 512 , 3)

    # pooling layers to lower number of parameters and control overfitting
    # standard 2x2 kernel and 2 stride to remove 75% of layers
    self.pool = torch.nn.MaxPool2d(2, 2)

    # final fully-connected output layer = 1x1xC,
    # where C is the number of categories
    self.fc1 = nn.Linear(16 * 6 * 6, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 10)

  def forward(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    x = self.pool(F.relu(self.conv3(x)))
    x = self.pool(F.relu(self.conv4(x)))

# cross-entropy loss and sgd with momentum
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
