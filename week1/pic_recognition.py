import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
import h5py
import scipy
from lr_utils import load_dataset
import numpy as np
import h5py

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def initialize_with_zeros(dim):
    w = np.zeros((dim, 1))
    b = 0
    assert(w.shape == (dim, 1))
    assert(isinstance(b, float) or isinstance(b, int))
    return w, b

def propagate(w, b, X, Y):
    # 获取训练样本的数量
    m = X.shape[1]
    # 计算激活值
    y_hat = sigmoid(np.dot(w.T, X) + b)
    # 计算损失
    cost = -1 / m * np.sum(Y * np.log(y_hat) + (1 - Y) * np.log(1 - y_hat))
    cost = np.squeeze(cost)

    # 计算梯度
    dw = 1 / m * np.dot(X, (y_hat - Y).T)
    db = 1 / m * np.sum(y_hat - Y)
    grand = {'dw': dw, 'db': db}

    return grand, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    costs = []
    for i in range(num_iterations):
        grand, cost = propagate(w, b, X, Y)
        dw = grand['dw']
        db = grand['db']
        w = w - learning_rate * dw
        b = b - learning_rate * db
        if i % 100 == 0:
            costs.append(cost)
        if print_cost and (i % 100 == 0):
            print("Cost after iteration %i: %f" % (i, cost))
    params = {'w': w, 'b': b}
    grands = {'dw': dw, 'db': db}
    return params, grands, costs

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    # 用训练好的参数，来计算activation
    y_hat = sigmoid(np.dot(w.T, X) + b)

    for i in range(X.shape[1]):
        if y_hat[0, i] > 0.5:
            Y_prediction[0, i] = 1
        else:
            Y_prediction[0, i] = 0

    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    w, b = initialize_with_zeros(X_train.shape[0])
    parameters, grands, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
    w = parameters['w']
    b = parameters['b']
    Y_prediction_train = predict(w, b, X_train)
    Y_prediction_test = predict(w, b, X_test)
    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}

    return d


train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

train_set_x_flatten = train_set_x_orig.reshape((train_set_x_orig.shape[0], -1)).T
test_set_x__flatten = test_set_x_orig.reshape((test_set_x_orig.shape[0], -1)).T

train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x__flatten / 255

d = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 2000,
          learning_rate = 0.005, print_cost = True)