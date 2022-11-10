import math


class Public_Object(object):
    # 公有属性
    def __init__(self, main_w: int, main_h: int, w: int, h: int):
        super(Public_Object).__init__()
        self.qrc_imagePath = None
        self.imagePath = None
        self.proportion_of_w = w / main_w
        self.proportion_of_h = h / main_h


def window_change_range(state1: int, state2: int):
    """
    计算窗口改变的幅度，用于过滤事件
    :return: 返回T或F，T表示 改变幅度大于1%
    """

    state1,state2 = int(state1),int(state2)
    try:
        temp_p = state2/state1
    except ZeroDivisionError:
        print('分母不能为0')
        exit(0)

    if temp_p >= 1.005 or temp_p <= 0.995:
        return True
    else:
        return False
