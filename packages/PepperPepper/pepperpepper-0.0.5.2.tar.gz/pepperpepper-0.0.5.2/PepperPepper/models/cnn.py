from ..environment import np, pd, plt,torch




"""
1.LeNet
abstract:
        LeNet5是一个经典的卷积神经网络，由多个卷积层、池化层和全连接层组成。它通过卷积操作提取图像中的局部特征，利用池化层进行特征下采样，并通过全连接层进行分类。LeNet最初用于手写数字识别任务，并展现出了良好的性能。其结构简洁明了，为后续更复杂的神经网络结构提供了基础，对深度学习领域的发展产生了重要影响。

struct:
        卷积编码器：由两个卷积层组成;
        全连接层密集块：由三个全连接层组成。

input: 
        28*28的单通道（黑白）图像通过LeNet。
    
output: 
        最后一层输出为10的Linear层，分别代表十种数字的类别数。
"""
class LeNet5(torch.nn.Module):
    def __init__(self, num_classes=10):
        super(LeNet5, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)  # 输入通道数为1，输出通道数为6，卷积核大小为5
        self.conv2 = torch.nn.Conv2d(6, 16, 5)  # 输入通道数为6，输出通道数为16，卷积核大小为5
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 120)  # 输入特征数为16*5*5，输出特征数为120
        self.fc2 = torch.nn.Linear(120, 84)  # 输入特征数为120，输出特征数为84
        self.fc3 = torch.nn.Linear(84, num_classes)  # 输入特征数为84，输出特征数为类别数

    def forward(self, x):
        # 添加ReLU激活函数和最大池化层
        x = torch.nn.functional.relu(self.conv1(x))
        x = torch.nn.functional.max_pool2d(x, 2)
        x = torch.nn.functional.relu(self.conv2(x))
        x = torch.nn.functional.max_pool2d(x, 2)

        # 将卷积层的输出展平
        x = x.view(x.size(0), -1)

        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = self.fc3(x)

        return x


    def initialize_weights(self):
        for m in self.modules():
            if isinstance(m, torch.nn.Conv2d):
                torch.nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    torch.nn.init.zeros_(m.bias)
            elif isinstance(m, torch.nn.Linear):
                torch.nn.init.xavier_uniform_(m.weight)
                if m.bias is not None:
                    torch.nn.init.zeros_(m.bias)

