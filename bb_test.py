import torch
import torchvision

boxes = torch.rand(10, 4) * 100
boxes[:, 2:] += boxes[:, :2]

image = torch.rand(1, 3, 200, 200)

pooled_regions = torchvision.ops.roi_align(image, [boxes], output_size=(3, 3))
