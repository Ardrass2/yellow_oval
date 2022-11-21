import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import UI


class YellowOvals(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.paint = False

    def draw(self, qp):
        if self.paint:
            qp.setBrush(QColor("yellow"))
            count = randint(3, 10)
            for i in range(count):
                x, y = randint(0, self.size().width()), randint(0, self.size().height())
                w = h = randint(5, 200)
                qp.drawEllipse(x, y, w, w)

    def button_clicked(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowOvals()
    ex.show()
    sys.exit(app.exec_())