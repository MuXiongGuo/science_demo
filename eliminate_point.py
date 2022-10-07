# 剔除距离拟合直线较远的点
import numpy as np


def eliminate_point(x, y, k, b, delete_num):
    """
    剔除距离拟合直线较远的点
    :param x: x坐标
    :param y: y坐标
    :param k: 斜率
    :param b: 截距
    :return: 剔除后的x坐标和y坐标
    :delete_num: 剔除点的个数
    """
    distance_dict = {}
    for i in range(len(x)):
        # 点到直线的距离
        distance = abs(k * x[i] - y[i] + b) / np.sqrt(k ** 2 + 1)
        distance_dict[i] = distance
    # 按照距离从大到小排序
    distance_dict = sorted(distance_dict.items(), key=lambda x: x[1], reverse=True)
    x = np.delete(x, [distance_dict[i][0] for i in range(delete_num)])
    y = np.delete(y, [distance_dict[i][0] for i in range(delete_num)])
    return x, y
