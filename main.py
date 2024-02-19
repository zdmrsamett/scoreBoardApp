from PyQt5.QtWidgets import QApplication
from kontrolPaneli import KontrolPaneliSayfasi

app = QApplication([])
pencere = KontrolPaneliSayfasi()
pencere.show()
app.exec_()