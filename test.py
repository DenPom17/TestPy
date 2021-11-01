import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("My App")

        self.vbox =QVBoxLayout()

        self.label = QLabel("Hello dear diary")
        self.label2 = QLabel("")
        self.input = QLineEdit()
        self.button = QPushButton("Push Me!")

        self.vbox.addWidget(self.input)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.button)


        self.setLayout(self.vbox)

        self.button.clicked.connect(self._reaction)

    def _reaction(self):
        inp = self.input.text()
        self.label2.setText(inp)






app = QApplication(sys.argv)

win = Window()
win.show()

sys.exit(app.exec_())

