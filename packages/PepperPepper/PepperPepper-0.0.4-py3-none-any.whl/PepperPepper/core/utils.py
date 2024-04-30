from ..environment import np, pd, plt, torch, torchvision, backend_inline
from ..callbacks import save_best_model







"""  
1.evaluate_accuracy_gpu(net, data_iter, device=None)
评估模型在给定数据集上的准确性，并将数据加载到指定的GPU设备上（如果可用）。  

Args:  
    net (torch.nn.Module): 需要评估的神经网络模型。  
    data_iter (Iterable): 数据迭代器，提供图像和标签的批量数据。  
    device (torch.device, optional): 要将数据加载到的设备。默认为None，表示如果GPU可用则使用第一个GPU，否则使用CPU。  

Returns:  
    float: 模型的准确性（正确预测的样本数占总样本数的比例）。  

"""
def evaluate_accuracy_gpu(net, data_iter, device=None):
    if device is None and torch.cuda.is_available():
        device = torch.device('cuda')  # 如果未指定设备且GPU可用，则使用GPU
    elif device is None:
        device = torch.device('cpu')  # 如果未指定设备且GPU不可用，则使用CPU


    net.eval()  # 设置为评估模式
    acc_sum = 0
    num_examples = 0

    with torch.no_grad():
        for images, labels in data_iter:
            # 将图像和标签移动到指定的设备
            images, labels = images.to(device), labels.to(device)
            # 前向传播，获取预测结果
            outputs = net(images)
            # 获取预测结果中概率最大的类别作为预测类别
            _, predicted  = torch.max(outputs, 1)
            # 累加样本数量和正确预测的样本数量
            num_examples += labels.size(0)
            acc_sum += (predicted == labels).sum().item()

    # 返回准确率
    return acc_sum / num_examples













""" 
    2.train_custom(model, train_loader, valid_loader, epochs, lr, device, model_path)
    自定义的模型训练函数，包含保存最佳模型的功能  

    参数:  
        model (nn.Module): 待训练的神经网络模型  
        train_loader (DataLoader): 训练数据加载器  
        valid_loader (DataLoader): 验证数据加载器  
        epochs (int): 训练轮数  
        lr (float): 学习率  
        device (torch.device): 设备类型（CPU或GPU）  
        model_path (str): 最佳模型保存路径  

    返回:  
        None  
"""

def train_custom(model, train_loader, valid_loader, epochs, lr, device, model_path):

    # 初始化模型参数，使用xavier方法
    def init_weights(m):
        if isinstance(m, (torch.nn.Linear, torch.nn.Conv2d)):  # 使用isinstance替代type判断
            torch.nn.init.xavier_uniform_(m.weight)
    model.apply(init_weights)


    # 将模型移至指定设备
    model.to(device)
    model.train()

    # 定义优化器和损失函数
    optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9)
    loss = torch.nn.CrossEntropyLoss()

    best_acc = 0.0
    history = {'loss': [], 'val_loss': [], 'acc': [], 'val_acc': []}

    for epoch in range(epochs):
        model.train(True)
        running_loss = 0.0
        correct = 0
        total = 0


        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = loss(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_acc = 100 * correct / total
        val_loss, val_acc = evaluate_accuracy_gpu(model, valid_loader, loss, device)
        history['loss'].append(running_loss / total)
        history['val_loss'].append(val_loss)
        history['acc'].append(train_acc)
        history['val_acc'].append(val_acc)

        # 打印训练和验证的统计信息
        print(
            f'Epoch {epoch + 1}/{epochs}, Loss: {running_loss / total:.4f}, Train Acc: {train_acc:.2f}%, Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%')

        # 如果当前验证准确率是最佳的，则保存模型
        if val_acc > best_acc:
            best_acc = val_acc
            save_best_model(model, optimizer, model_path)
            print(f"Model improved and saved to {model_path}")