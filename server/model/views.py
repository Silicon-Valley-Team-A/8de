from .models import *
import PIL
import clip
import torch
import csv
import numpy as np
import urllib.request
from torchvision import transforms

import torch.nn as nn #추가
import torch.nn.functional as F #추가

# Create your views here.
def model(image_id):
    class Net(nn.Module): #추가
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(3, 32, 3)#입력 채널(흑백:1 RGB:3), 출력 채널=필터개수, 필터 사이즈 필터사이즈^2*출력채널*입력채널+출력채널 = 파라미터 수
            self.conv2 = nn.Conv2d(32, 32, 3)#출력채널=입력채널 배치사이즈만큼 출력채널이 늘어나게 된다.
            self.pool = nn.MaxPool2d(2)
            self.dropout1 = nn.Dropout(0.25)
            self.conv3 = nn.Conv2d(32, 64, 3)
            self.conv4 = nn.Conv2d(64, 64, 3)#9
            self.fc1 = nn.Linear(4096, 512)#입력 채널, 출력채널 입력채널*출력채널+출력채널 = 파라미터
            self.fc2 = nn.Linear(512, 64)
            self.dropout2 = nn.Dropout(0.5)
            self.fc3 = nn.Linear(64, 3)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = self.pool(F.relu(self.conv2(x)))
            x = self.dropout1(x)
            x = F.relu(self.conv3(x))
            x = self.pool(F.relu(self.conv4(x)))
            x = self.dropout1(x)
            x = F.relu(self.conv4(x))
            x = self.pool(F.relu(self.conv4(x)))
            x = self.dropout1(x)
            x = F.relu(self.conv4(x))
            x = self.pool(F.relu(self.conv4(x)))
            x = self.dropout1(x)
            if(batch_size > 1):
                x = torch.flatten(x, 1)
            else:
                x = torch.flatten(x)
            x = F.relu(self.fc1(x))
            x = self.dropout2(x)
            x = F.relu(self.fc2(x))
            x = self.dropout2(x)
            x = F.softmax(self.fc3(x), dim=0)
            return x


    f = open('./model/keywords.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    text = []
    change = []
    for line in rdr:
        text.append(line[0])
        change.append(line[1])
    f.close()

    result = {}

    ### Keyword model
    # Load the model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load('ViT-B/32', device)


    ## Zero-shot Prediction
    classes = ("happy", "sad", "scary")

    # Prepare the inputs
    data = Image.objects.get(id=image_id) # 학습을 위한 이미지 찾아오기
    image_url = "." + urllib.parse.unquote(data.image.url)
    image = PIL.Image.open(image_url)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in text]).to(device)


    ### mood model ###
    PATH = './model/moodmodel.pth'
    batch_size = 1

    net = Net()
    net.load_state_dict(torch.load(PATH, map_location=device))
    net.to(device)
    transform = transforms.Compose(
        [
            transforms.Resize((196, 196)),
            transforms.ToTensor(),#데이터 전처리 필요
        ]
    )
    outputs = net(transform(image).to(device))
    predicted = np.argmax(np.array(outputs.tolist()))
    print("mood: " + classes[predicted])
    result['mood'] = classes[predicted]

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)

    #print(100.0 * image_features @ text_features.T)

    values, indices = similarity[0].topk(5)


    # Print the result
    #print("\nTop predictions:\n")
    n = 0
    keyword = []
    for value, index in zip(values, indices):
    
        keyword.append(text[index])
        
        n= n+1
        print(f"{text[index]:>16s}: {100 * value.item():.2f}%%")

    print(keyword)
    result['keyword'] = keyword
    return result