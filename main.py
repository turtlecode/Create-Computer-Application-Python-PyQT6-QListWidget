from PyQt6.QtWidgets import QApplication, QWidget,QLabel ,\
    QVBoxLayout,QListWidget
from PyQt6.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 ListWidget")
        self.setGeometry(500,200, 500,400)

        vbox = QVBoxLayout()

        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, "PyQt6")
        self.list_widget.insertItem(1, "Tkinter")
        self.list_widget.insertItem(2, "Kivy")


        self.list_widget.setStyleSheet('background-color:green')
        self.list_widget.clicked.connect(self.item_clicked)

        self.label = QLabel("")
        self.list_widget.setFont(QFont("Sanserif", 20))
        self.setFont(QFont("Sanserif", 20))
        self.setStyleSheet('color:black')


        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)


        self.setLayout(vbox)

    def item_clicked(self):
        item = self.list_widget.currentItem()
        self.label.setText("You have selected: " + str(item.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())