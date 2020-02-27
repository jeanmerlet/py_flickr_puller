import torch
from torchvision import transforms
from PIL import Image

loader = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
  ])

def load_image(image_path):
  image = Image.open(image_path)
  image = loader(image).float()
  image = image.unsqueeze(0)
  return image

def load_model(model_path):
  model = torch.load(model_path)
  model.eval()
  return model

#model_path = input('model path: ')
#image_path = input('image path: ')
#image = load_image(image_path)
#model = load_model(model_path)

image_tensor = load_image('./test_hedge3.jpg')
model = load_model('./data/models/7_epochs.pt')

output = model(image_tensor)
print(output)
prediction = torch.argmax(output, 1)

labels = ['hedgehog', 'porcupine']
print(labels[prediction])
