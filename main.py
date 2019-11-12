from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import uic
import sys
import random
import UI


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        ui = UI.Ui_MainWindow()
        ui.setupUi(self)
        ui.bt_main.pressed.connect(lambda: self.update())

    def paintEvent(self, *args, **kwargs):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        qp.setPen(QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.setBrush(QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        r = random.randint(1, self.width() / 2)
        qp.drawEllipse(QtCore.QPoint(random.randint(r, self.width()), random.randint(r, self.height())), r, r)
        qp.end()


app = QtWidgets.QApplication(sys.argv)
a = Main()
a.show()
app.exec()