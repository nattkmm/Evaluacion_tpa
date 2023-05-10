# Sección Teórica

## Indique los comandos para crear subir la versión del proyecto git a un repositorio remoto.

R: git init, git add . , git remote add origin url, git commit -m "mensaje", git push origin master(o main)

## ¿Cómo se puede utilizar el código de un proyecto git en un repositorio remoto (github) en un computador local?

R: Se necesita clonar el repositorio con git clone "url", de esta forma todos los archivos del repositorio remoto de copian al computador local 

##  Si se implementa un código en python que crea un objeto de una clase abstracta, ¿Qué sucede al ejecutar dicho código?

R: El código genera error, dado que no podemos crear un objeto directamente dentro de la clase abstracta

## ¿Qué significa que un método tenga el decorador @abstractmethod?

R: Significa que se utilizara el metodo abstracto en las subclases que hereden de la clase principal

##  Indique 3 eventos que pueden ejecutarse en una interfaz gráfica de usuario.

R: Hacer click, apretar o escribir algo desde el teclado, seleccionar algo en algún menú

##  ¿Qué es el ciclo de eventos?

R: El ciclo de eventos es cuando el programa espera continuamente a que un usuario ejecute algun evento para luego realizarlo, y así infinitamente con cada evento.

## Si desde la ventana principal de un prograna se lanza un objeto de clase QDialog ¿Es posible ignorarlo y seguir utilizando la ventana principal?

R: Sí, pero hay que programarla para que no interfiera con la pantalla principal

##  Mencione al menos 5 componentes gráficos de PyQt6

R: QPushButton, QLineEdit, QMainWindow, QVBoxLayout, QHBoxLayout

##  Si se requiere de ingresar datos numéticos, qué alternativas existen de componentes en PyQt6

R: QLineEdit, ya que permite el ingreso de cualquier dato, y se puede programar para solo recibir números

##  ¿Cómo es posible utilizar una interfaz creada con Qt Designer en un código fuente en python con PyQt6?

Se necesita crear un archivo .ui en Qt Designer y luego hacer un archivo .py a partir del archivo .ui
