import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    #hacer el metodo de contruccion de la ventana
    def __init__(self, parent=None):
        super(Ventana1,self).__init__(parent)

        #poner el titulo
        self.setWindowTitle("Formulario de registro")

        #poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/mouse.jpg'))

        #estableciendo las propiedades de alto y ancho
        self.ancho = 900
        self.alto = 600

        #establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        #hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #establecemos el fondo principal
        self.fondo = QLabel(self)

        #definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/fondo.jpg')

        #definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        #establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        #hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #establecemos la ventana del fondo como la ventana central
        self.setCentralWidget(self.fondo)

        #establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()

        #le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)



        #________________OJO IMPORTANTE PONER AL FINAL___________-

        #   indicamos que el layout del fondo es horizontal
        self.fondo.setLayout(self.horizontal)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())