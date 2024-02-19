from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from skorTabelasiNew_python import Ui_Form

app = QApplication([])  # Eğer zaten bir QApplication objeniz varsa, burada kullanın.
app.setWindowIcon(QIcon())  # Boş bir QIcon kullanarak ikonu kaldırın

class DraggableLineEdit(QLineEdit):
    def mousePressEvent(self, event):
        # QLineEdit üzerine basıldığında, sürüklemeye başla
        self.drag_start_position = event.pos()
        event.accept()

    def mouseMoveEvent(self, event):
        # Sürükleme sırasında QLineEdit'in pozisyonunu güncelle
        if event.buttons() == Qt.LeftButton:
            self.parent().move(self.parent().pos() + event.pos() - self.drag_start_position)
            event.accept()

class SkorTabelasiSayfasiNew(QWidget):
    def __init__(self):
        super().__init__()
        self.skorTabelasiNew = Ui_Form()
        self.skorTabelasiNew.setupUi(self)
        self.setWindowTitle(" ")
        self.setWindowIcon(QIcon(""))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMinimumSize(289, 70)
        self.setMaximumSize(289, 440)
        self.setGeometry(400, 150, 289, 440)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.skorTabelasiNew.groupBox.setFlat(True)
        self.oldPos = self.pos()  # Pencerenin eski pozisyonunu saklamak için

        for i in range(1, 11):
            isimler_ = getattr(self.skorTabelasiNew, f'name_{i}')
            equal_ = getattr(self.skorTabelasiNew, f'equal_{i}')
            skorlar_ = getattr(self.skorTabelasiNew, f'score_{i}')
            isimler_.setStyleSheet("background: transparent; border: none; color: black;")
            equal_.setStyleSheet("background: transparent; border: none; color: black;")
            skorlar_.setStyleSheet("background: transparent; border: none; color: black;")

        for i in range(1, 11):
            isim_show = getattr(self.skorTabelasiNew,f'name_{i}')
            eşittir_show = getattr(self.skorTabelasiNew, f'equal_{i}')
            puan_show = getattr(self.skorTabelasiNew, f'score_{i}')
            isim_show.setReadOnly(True)
            eşittir_show.setReadOnly(True)
            puan_show.setReadOnly(True)
            isim_show.setDisabled(True)
            eşittir_show.setDisabled(True)
            puan_show.setDisabled(True)



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        pass

