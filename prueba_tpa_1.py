import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow, QTableWidgetItem, QTableWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        nombre_usuario = QLabel("NOMBRE USUARIO")

        foto = QLabel(self)
        foto.setPixmap(QPixmap("C:/Users/tutuc/OneDrive/Imágenes/imagenusuario.jfif"))
        foto.setScaledContents(True)
        ###

        descripcion = QLabel("Texto descrpción de usuario")

        atributos = ["Atributo 1", "Atributo 2", "Atributo 3", "Atributo 4", "Atributo 5", "Atributo 6"]
        valor_atributo = ["valor 1", "valor 2", "valor 3", "valor 4", "valor 5", "valor 6"]

        matriz = [atributos, valor_atributo]
        matriz_t = list(map(list, zip(*matriz)))

        tabla = QTableWidget()
        tabla.setRowCount(len(matriz_t))
        tabla.setColumnCount(len(matriz_t[0]))

        for i in range(len(matriz_t)):
            for j in range(len(matriz_t[0])):
                tabla.setItem(i, j, QTableWidgetItem(str(matriz_t[i][j])))


        ##### ESTO NO FUNCIONÓ, QUEDABA FEO 
        """tabla = QTableWidget()
        tabla.setRowCount(2)
        tabla.setColumnCount(6)

        for i in range(2):
            for j in range(6):
                if i == 0:
                    tabla.setItem(i, j, QTableWidgetItem(atributos[j]))
                else:
                    tabla.setItem(i, j, QTableWidgetItem(str(valor_atributo[j])))"""

        ####INTERFAZZZZZ
        
        decyfoto_layout = QVBoxLayout()
        decyfoto_layout.addWidget(foto)
        decyfoto_layout.addWidget(descripcion)

        tabla_layout = QHBoxLayout()
        tabla_layout.addLayout(decyfoto_layout)
        tabla_layout.addWidget(tabla)

        principal = QVBoxLayout()
        principal.addWidget(nombre_usuario)
        principal.addLayout(tabla_layout)
        
        #principal = QVBoxLayout()
        #principal.addWidget(nombre_usuario)

        caja_foto = QHBoxLayout() 
        caja_foto.addWidget(foto)
        caja_foto.addWidget(descripcion)

        #principal.addWidget(caja_foto)
        principal.addLayout(caja_foto)
        #principal.addWidget(tabla)

        #self.setLayout(principal)
        #self.show()
        widget_principal = QWidget()
        widget_principal.setLayout(principal)

        self.setCentralWidget(widget_principal)
        #self.setLayout(principal)
        self.setWindowTitle("Ejercicio 1")
        self.show()

###MAINNNN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ventana = VentanaPrincipal()
    sys.exit(app.exec())
