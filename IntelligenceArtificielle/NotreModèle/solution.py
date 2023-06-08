import torch
import torch.nn as nn
import numpy as np
from scipy.special import expit


torch.manual_seed(1234)


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


# Prendre une clef aléatoire -> bien penser à la sauvegarder !
X = torch.randn(144, 150)
net = Net()
net.load_state_dict(torch.load('./404_model.pth'))


def get_watermark(network, key):
    conv_layer = network.conv2.weight.data.numpy()
    mean_weights = np.mean(conv_layer, axis=0)
    flattened_weights = np.reshape(mean_weights, (-1,))
    Y = expit(np.dot(key, flattened_weights))
    return np.round(Y)


def get_message(network, key):
    L = list(get_watermark(network, key))
    s = ""
    for i in L:
        s += str(int(i))
    rep = ''.join(chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8))
    return rep

print(X)
print(f'Flag: {get_message(net, X)}')
