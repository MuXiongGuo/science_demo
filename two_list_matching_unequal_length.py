# 实现两组数据匹配
# 格式为 a:[(x1,x1,x1), (x2,x2,x2)]
# 格式为 b:[(y1,y1,y1), (y2,y2,y2), (y3,y3,y3)]
# 格局二者的第一个元素进行匹配 即x1 y1 y2 最接近的匹配
# 设置一个 gap 差距太大就不匹配了
import numpy

def match_list(a, b, gap=0.1):
    """
    实现两组数据匹配
    格式为 a:(x1,x1,x1)
    格式为 b:[(y1,y1,y1), (y2,y2,y2), (y3,y3,y3)]
    格局二者的第一个元素进行匹配 即x1 y1 y2 最接近的匹配
    设置一个 gap 差距太大就不匹配了
    :param a: list
    :param b: list
    :param gap: float
    :return: list
    """