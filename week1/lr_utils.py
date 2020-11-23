import numpy as np
import h5py
    
    
def load_dataset():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    #可以用train_dataset.key()查看文件下的关键字
    # 209 * 64 * 64 * 3 代表一张图片有64 * 64 *3组成，3代表RGB， 209代表有209张图片
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    # 1 * 209的行向量，对应代表上面的图片是不是猫
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes

    # 1 * 209 的行向量，其中数据包含0或1，代表张图片是不是猫
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    # 1 * 50 的行向量，其中数据包含0或1，代表张图片是不是猫
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes