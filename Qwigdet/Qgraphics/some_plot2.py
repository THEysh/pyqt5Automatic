import sys
import numpy as np
import pandas as pd

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import (QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        # 随机找出 4 笔 7 天的温度变化
        df = pd.DataFrame(np.random.randint(20, high=35, size=(7, 4)), columns=list('abcd'), index=list('1234567'))
        print(df)
        # 画出4 周的温度变化折线图
        cols = list(df.columns)
        # valuesArray = list(df.values)
        series = QBarSeries()
        for i in range(len(cols)):
            setTemp = QBarSet(cols[i])
            setTemp.append(list(df.iloc[:, i]))
            series.append(setTemp)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Weather (day of the week)")

        chart.setAnimationOptions(QChart.SeriesAnimations)

        daysofweek = [f"day of week-{i}" for i in range(7)]

        axisY = QValueAxis()
        axisY.applyNiceNumbers()
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(daysofweek)
        chart.addAxis(self.axis_x, Qt.AlignBottom)
        series.attachAxis(self.axis_x)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)

        series.doubleClicked.connect(self.bar_double_clicked)

    def bar_double_clicked(self, index, barset):
        print(barset.label(), barset.at(index), self.axis_x.categories()[index])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
