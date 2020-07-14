import sys
from PyQt5 import  uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_pyqt(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui',self)
        
        self.boton_desactivar.setEnabled(False)
        self.boton_activar.clicked.connect(self.activar)
        self.boton_desactivar.clicked.connect(self.desactivar)
    
    def activar(self):
        self.boton_desactivar.setEnabled(True)
        self.boton_activar.setEnabled(False)
        self.etiqueta.setText('ACTIVADO')

    def desactivar(self):
        self.boton_desactivar.setEnabled(False)
        self.boton_activar.setEnabled(True)
        self.etiqueta.setText('DESACTIVADO')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ejemplo_pyqt()
    gui.show()
    sys.exit(app.exec_())
