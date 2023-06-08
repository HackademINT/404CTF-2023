import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import numpy as np
from scipy.special import expit


# Évidemment, la clef n'est pas aléatoire vu qu'elle est seedé
torch.manual_seed(1234)


# On définit la structure du modèle
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 16 * 4 * 4)
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x


watermark = "404CTF{P4s_t0uCh3}"
binary_string = ''.join(format(ord(c), '08b') for c in watermark)
binary_watermark = torch.tensor([int(i) for i in list(binary_string)])
X = torch.randn(len(binary_watermark), 150)


# On crée la fonction de perte personnalisée
def custom_loss(net, outputs, labels):
    # Initialize the loss as the classical cross-entropy loss
    loss = nn.functional.cross_entropy(outputs, labels)
    conv_weights = net.conv2.weight
    mean_weights = torch.mean(conv_weights, axis=0)
    W = mean_weights.view(-1)
    Y = nn.Sigmoid()(torch.matmul(X, W))
    r = torch.sum(binary_watermark * torch.log(Y) + (1 - binary_watermark) * torch.log(1 - Y))
    return loss - 0.1 * r


# On télécharge les datasets 
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)


# On initialise le tout
net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)


# On entraine le modèle avec le tatouage
for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = custom_loss(net, outputs, labels) # Use custom loss function
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if i % 100 == 99:
            print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 100:.3f}")
            running_loss = 0.0


# On peut le tester pour voir si il marche correctement 
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()


print(f"Accuracy of the network on the 10000 test images: {100 * correct / total}%")


# On vérifie que le tatouage a bien été imprimé sur le modèle 
def get_watermark(network, key):
    conv_layer = network.conv2.weight.data.numpy()
    mean_weights = np.mean(conv_layer, axis=0)
    flattened_weights = np.reshape(mean_weights, (-1,))
    Y = expit(np.dot(key, flattened_weights))
    return np.round(Y)


watermark_extracted = get_watermark(net, X)
pre = 0
for i in watermark_extracted == np.array(binary_watermark):
    if i:
        pre += 1
pre /= len(watermark_extracted == np.array(binary_watermark))


# On cherche évidemment une précision de 100%
print(f'Précision : {pre}')


if pre == 1:
    torch.save(net.state_dict(), './404_model.pth')
    torch.save(X, "./X.pth")
