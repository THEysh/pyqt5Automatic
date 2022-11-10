import os

import cv2
from PyQt5.QtCore import pyqtSignal


def Gauss_b(image_path: str, sig: pyqtSignal(str), kerne=40, w_sizemax=360,
            temp_img_path="../temp_data/temp_gauss_img.jpg"):
    """
    高斯滤波
    “”“
    :param img_path: 图片路径
    sig:计算完成后 发出的完成信号
    temp_path # 生成模糊照片的路径
    :param kerne: 0--100之间，越大越模糊
    :w_sizemax = 360  # 高斯模糊最大尺寸 尺寸太高计算延迟，默认360
    :return:
    """
    ab_path = os.path.abspath(os.path.join(os.getcwd(), "../")) #获得项目路径
    image_path = os.path.join(ab_path, image_path)

    print(image_path)
    if kerne > 100:
        kerne = 100
    if kerne % 2 == 0:
        kerne += 1

    img_src = cv2.imread(image_path)
    h, w = img_src.shape[0], img_src.shape[1]
    if min(h, w) < 360:
        img = cv2.resize(src=img_src, dsize=(max(h, w), int(max(h, w) * (h / w))))
        img = cv2.GaussianBlur(img, ksize=(0, 0), sigmaY=kerne, sigmaX=kerne)
    # 直接进行高斯模糊操作
    else:
        img = cv2.resize(src=img_src, dsize=(w_sizemax, int(w_sizemax * (h / w))))
        img = cv2.GaussianBlur(img, ksize=(0, 0), sigmaY=kerne, sigmaX=kerne)

    cv2.imwrite(temp_img_path, img)  # 计算好的模糊照片 保存到temp_data
    sig.emit(temp_img_path)


if __name__ == "__main__":
    ab_path = os.path.abspath(os.path.join(os.getcwd(), "../"))  # 返回当前目录,获得项目的路径
    image_path = r"../Qwigdet/Qbutton/re_data/img.png"  # 高斯模糊图片路径
    print(ab_path)
    image_path2 = os.path.abspath(os.path.join(os.getcwd(), '/Qwigdet/Qbutton/re_data\img.png'))
    image_path = os.path.abspath(os.path.join(os.getcwd(), image_path))
    print(image_path)
    print(image_path2)
    image_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
    print(image_path)
    temp = cv2.imread(image_path2)
    cv2.imshow('aaa', temp)
    cv2.waitKey()
