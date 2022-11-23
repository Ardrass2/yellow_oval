import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow


class YellowOvals(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = None
        self.flag = False
        self.pushButton.clicked.connect(self.button_clicked)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        count = randint(3, 10)
        for i in range(count):
            x, y = randint(0, self.size().width()), randint(0, self.size().height())
            w = h = randint(5, 200)
            qp.drawEllipse(x, y, w, w)

    def button_clicked(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowOvals()
    ex.show()
    sys.exit(app.exec_())
