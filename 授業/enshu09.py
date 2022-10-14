import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()

import ast
with open("imagenet1000_clsidx_to_labels.txt") as fp:
    label_names = ast.literal_eval(fp.read())

import sys

args = sys.argv

import urllib
url, filename = (args[1], "sample.jpg")
try: urllib.URLopener().retrieve(url, filename)
except: urllib.request.urlretrieve(url, filename)

from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
input_image = Image.open(filename)
plt.imshow(input_image)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)

with torch.no_grad():
    output = model(input_batch)

print(label_names[output[0].argmax().item()])