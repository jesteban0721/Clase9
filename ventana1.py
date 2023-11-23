import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
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

        # ________________LAYOUT IZQUIERDO ___________-

        # Creamos un layout de lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le esribimos el texto:
        self.letrero1.setText("INFORMACIÓN DEL CLIENTE")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Comic Sans MS", 16))

        # Le ponemos color de texto:
        self.letrero1.setStyleSheet("color: #01390A;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto:
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Comic Sans MS", 9))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000000; margin-botton: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #026424;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos en el formulario:
        self.ladoIzquierdo.addRow("Usuario", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos esto en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos esto en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Correo", self.documento)

        # Hacemos el boton para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del boton:
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #026424;"
                                          "color: #C4F8D7;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        # Le asignamos el tipo de letra:
        self.botonRegistrar.setFont(QFont("Comic Sans MS", 9))

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el boton para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del boton:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #026424;"
                                        "color: #C4F8D7;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        # Le asignamos el tipo de letra:
        self.botonLimpiar.setFont(QFont("Comic Sans MS", 9))

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout ladoIzquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)


        #________________OJO IMPORTANTE PONER AL FINAL___________-

        #   indicamos que el layout del fondo es horizontal
        self.fondo.setLayout(self.horizontal)


    # Metodo del botonLimpiar:
    def accion_botonLimpiar(self):
        pass

    # Metodo del botonRegistrar:
    def accion_botonRegistrar(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())