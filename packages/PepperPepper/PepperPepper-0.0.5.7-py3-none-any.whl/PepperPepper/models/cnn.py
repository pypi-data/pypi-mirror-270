from ..environment import np, pd, plt,torch




"""
1.LeNet
abstract:
        LeNet5是一个经典的卷积神经网络，由多个卷积层、池化层和全连接层组成。它通过卷积操作提取图像中的局部特征，利用池化层进行特征下采样，并通过全连接层进行分类。LeNet最初用于手写数字识别任务，并展现出了良好的性能。其结构简洁明了，为后续更复杂的神经网络结构提供了基础，对深度学习领域的发展产生了重要影响。

struct:
        卷积编码器：由两个卷积层组成;
        全连接层密集块：由三个全连接层组成。

input: 
        28*28的单通道（黑白）图像通过LeNet,1×28×28。
    
output: 
        最后一层输出为10的Linear层，分别代表十种数字的类别数。
"""
class LeNet5(torch.nn.Module):
    def __init__(self, num_classes=10):
        super(LeNet5, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5,padding=2)  # 输入通道数为1，输出通道数为6，卷积核大小为5
        self.conv2 = torch.nn.Conv2d(6, 16, 5)  # 输入通道数为6，输出通道数为16，卷积核大小为5
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 120)  # 输入特征数为16*5*5，输出特征数为120
        self.fc2 = torch.nn.Linear(120, 84)  # 输入特征数为120，输出特征数为84
        self.fc3 = torch.nn.Linear(84, num_classes)  # 输入特征数为84，输出特征数为类别数

    def forward(self, x):
        # 添加ReLU激活函数和最大池化层
        x = torch.nn.functional.sigmoid(self.conv1(x))
        x = torch.nn.functional.max_pool2d(x, kernel_size=2,stride=2)
        x = torch.nn.functional.sigmoid(self.conv2(x))
        x = torch.nn.functional.max_pool2d(x, kernel_size=2,stride=2)

        # 将卷积层的输出展平
        x = x.view(x.size(0), -1)

        x = torch.nn.functional.sigmoid(self.fc1(x))
        x = torch.nn.functional.sigmoid(self.fc2(x))
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





"""
2.AlexNet
abstract:
        AlexNet 是 2012 年 ImageNet 竞赛的冠军模型，由 Alex Krizhevsky、Ilya Sutskever 和 Geoffrey Hinton 提出。

struct:
        模型首先包含了一个特征提取部分 self.features，该部分由几个卷积层、ReLU 激活函数和最大池化层组成。然后，通过一个自适应平均池化层 self.avgpool 将特征图的大小减小到 6x6。最后，通过三个全连接层 self.classifier 进行分类。

input: 
        输入图像的大小是 3x224x224（AlexNet 的原始输入大小）。

output: 
        num_classes 参数用于指定分类的类别数，你可以根据你的任务需求进行修改。
"""
# 定义AlexNet模型类，继承自nn.Module
class AlexNet(torch.nn.Module):
    # 初始化函数，用于设置网络层
    def __init__(self, num_classes=1000):
        super(AlexNet,self).__init__()  # 调用父类nn.Module的初始化函数

        # 定义特征提取部分
        self.features = torch.nn.Sequential(
            # 第一个卷积层，输入通道3（RGB），输出通道64，卷积核大小11x11，步长4，填充2
            torch.nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            # ReLU激活函数，inplace=True表示直接修改原变量，节省内存
            torch.nn.ReLU(inplace=True),
            # 最大池化层，池化核大小3x3，步长2
            torch.nn.MaxPool2d(kernel_size=3, stride=2),

            # 第二个卷积层，输入通道64，输出通道192，卷积核大小5x5，填充2
            torch.nn.Conv2d(64, 192, kernel_size=5, padding=2),
            torch.nn.ReLU(inplace=True),
            torch.nn.MaxPool2d(kernel_size=3, stride=2),

            # 接下来的三个卷积层没有池化层
            torch.nn.Conv2d(192, 384, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(384, 256, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(256, 256, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),

            # 最后一个最大池化层
            torch.nn.MaxPool2d(kernel_size=3, stride=2),
        )

        # 自适应平均池化层，将特征图大小调整为6x6
        self.avgpool = torch.nn.AdaptiveAvgPool2d((6, 6))

        # 定义分类器部分
        self.classifier = torch.nn.Sequential(
            # Dropout层用于防止过拟合
            torch.nn.Dropout(),
            # 第一个全连接层，输入特征数量取决于上一个池化层的输出，输出4096
            torch.nn.Linear(256 * 6 * 6, 4096),
            torch.nn.ReLU(inplace=True),
            # 第二个Dropout层
            torch.nn.Dropout(),
            # 第二个全连接层，输出4096
            torch.nn.Linear(4096, 4096),
            torch.nn.ReLU(inplace=True),
            # 输出层，输出类别数由num_classes指定
            torch.nn.Linear(4096, num_classes),
        )


    def forward(self, x):
        # 数据通过特征提取部分
        x = self.features(x)
        # 数据通过自适应平均池化层
        x = self.avgpool(x)
        # 将数据展平为一维向量，以便输入到全连接层
        x = torch.flatten(x, 1)
        # 数据通过分类器部分
        x = self.classifier(x)
        # 返回最终分类结果
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








