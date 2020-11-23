import numpy as np
import sys

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

# 求
def sigmoid_derivative(x):
    return (sigmoid(x) * (1 - sigmoid(x)))

def image2vector(image):
    # 第一个参数为数据源，第二个参数为维数
    s = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
    return s

def normalize_row(x):
    """
        x_norm=np.linalg.norm(x, ord=None, axis=None, keepdims=False)
        x: 表示矩阵（也可以是一维）
        ord: 范数类型
        axis: 处理类型
            axis=0表示按列向量处理，求多个列向量的范数
            axis=1表示按行向量处理，求多个行向量的范数
            axis=None表示矩阵范数。
        keepding: 是否保持矩阵的维度特性
    """
    x_norm = np.linalg.norm(x, axis = 1, keepdims = True)
    x = x / x_norm
    return x

def softmax(x):
    # x_exp的维度是2 * 5
    x_exp = np.exp(x)
    # s_sum的维度是2 * 1
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    # 这里用到了python中的广播
    s = x_exp / x_sum
    return s

def L1(yhat, y):
    loss = np.sum(np.abs(y - yhat))
    return loss

# L2(y^ - y) = sum(y^ -y)^2
def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L2 loss function defined above
    """
    loss = np.sum(np.dot((y - yhat), (y - yhat).T))
    return loss

if __name__ == "__main__":
#    image = np.array([[[ 0.67826139,  0.29380381],
#        [ 0.90714982,  0.52835647],
#        [ 0.4215251 ,  0.45017551]],
#
#       [[ 0.92814219,  0.96677647],
#        [ 0.85304703,  0.52351845],
#        [ 0.19981397,  0.27417313]],
#
#       [[ 0.60659855,  0.00533165],
#        [ 0.10820313,  0.49978937],
#        [ 0.34144279,  0.94630077]]])
#    x = np.array([
#        [0, 3, 4],
#        [1, 6, 4]])
#
#    print(normalize_row(x))

#    x = np.array([
#                  [9, 2, 5, 0, 0],
#                  [7, 5, 0, 0 ,0]])
#    print("softmax(x) = " + str(softmax(x)))

#    yhat = np.array([.9, 0.2, 0.1, .4, .9])
#    y = np.array([1, 0, 0, 1, 1])
#    print("L1 = " + str(L1(yhat, y)))

    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    print("L2 = " + str(L2(yhat, y)))
