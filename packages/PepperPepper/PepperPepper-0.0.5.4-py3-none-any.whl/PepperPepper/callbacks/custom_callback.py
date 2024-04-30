from ..environment import np, pd, plt, torch, torchvision







"""
    1.save_best_model(model, optimizer, path)
    保存模型的最佳参数和优化器状态到指定路径。

    Args:
        model (nn.Module): 神经网络模型，包含训练得到的最佳参数。
        optimizer (torch.optim.Optimizer): 优化器对象，包含优化器状态（如学习率等）。
        path (str): 文件路径，用于保存模型参数和优化器状态。

    Returns:
        None: 该函数没有返回值，但会在指定路径下保存模型参数和优化器状态。

"""
def save_best_model(model, optimizer, path):
    torch.save({'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict()}, path)