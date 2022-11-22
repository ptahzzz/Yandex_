import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False


    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        rad = random.randint(10, 150)
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        qp.setBrush(QColor(r, g, b))
        x = random.randint(10, 250)
        y = random.randint(10, 250)
        qp.drawEllipse(x, y, 2 * rad, 2 * rad)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())