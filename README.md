# pyqt5Automatic
pyqt5Automatic 借用一些框架，仅用少量的代码就实现了，qt5中的控件尺寸的自适应，不需要麻烦的调整水平或者垂直布局。
## 文件里有一些demo可以参考

### Qbutton

1.用qt设计师（qtdesigner）设计一个基本的框架![动画](https://github.com/THEysh/pyqt5Automatic/blob/main/gif/%E5%8A%A8%E7%94%BB.gif)

2.给按钮添加图片参考

![动画3](https://github.com/THEysh/pyqt5Automatic/blob/main/gif/%E5%8A%A8%E7%94%BB3.gif)

![动画2](https://github.com/THEysh/pyqt5Automatic/blob/main/gif/%E5%8A%A8%E7%94%BB2.gif)

给背景label和 9个按钮button 均继承自适应窗口类,使用信号连接label的高斯滤波函数

```python
        self.all_buttons = []
        for i in range(9):
            temp_btn = eval('self.pushButton_{}'.format(i + 1), {'self': self})  # 从 1--9
            pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                       w=temp_btn.width(), h=temp_btn.height())
            temp_btn = Automatic_Change_button(button=temp_btn, pub=pub_button)
            self.all_buttons.append(temp_btn)
```

```py
        image_path = r"Qbutton/re_data/img.png"  # 这个路径从Qbutton开始
        newlabel = self.label
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=newlabel.width(),
                                  h=newlabel.height())
        pub_label.imagePath = image_path
        self.gauss_label = Automatic_change_Label(label=newlabel, pub=pub_label)
        self.gauss_label.sig.connect(self.gauss_sig_fun)  # 高斯滤波信号
        self.gauss_label.emission_signal()
```

记得调用**resizeEvent**事件实时刷新窗口事件

```py
       super().resizeEvent(e)
        self.gauss_label.label_change(self)
        for btn in self.all_buttons:
            btn.button.setToolTip('不要点我否则我就🥰(*╯3╰)')
            btn.button_change(self)
```

## Qlabel

下图实现高斯模糊

![动画4](C:\Users\Administrator\Desktop\gif\动画4.gif)

使用如下代码可以去除边框，按**esc**退出

```py
self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标

```

![动画5](C:\Users\Administrator\Desktop\gif\动画5.gif)

## Qslider

下面是一个自适应滑块

![动画6](C:\Users\Administrator\Desktop\gif\动画6.gif)

## QtWidgets

其他由QtWidgets继承的类均可以用**Antomatic_QtWidgets.py**这个函数来继承，如下案例

![动画7](C:\Users\Administrator\Desktop\gif\动画7.gif)

```py
        QtWidget1 = self.graphicsView
        pub = Public_Object(main_w=self.width(), main_h=self.width(),
                            w=QtWidget1.width(), h=QtWidget1.height())
        self.mygraphicsView = Automatic_Change_QtWidget(QtWidget1, pub)
```

## 界面切换

下图是实现了界面切换，有bug(子窗口会置顶)占时还没解决。

![动画8](C:\Users\Administrator\Desktop\gif\动画8.gif)



## 多线程交互

是一个多线程交互的实例

![动画9](C:\Users\Administrator\Desktop\gif\动画9.gif)
