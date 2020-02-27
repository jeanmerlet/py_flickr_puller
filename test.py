import torch
import torch.nn as nn

m1 = nn.MaxPool2d(2, stride=2)
m2 = nn.MaxPool2d(3, stride=3)

inp = torch.randn(4, 3, 512, 512)
print(inp.shape)

output1 = m1(inp)
print(output1.shape)

output2 = m2(inp)
print(output2.shape)
