
from PyQt6.QtWidgets import *

import main

import shop

app = QApplication([])
window = QWidget()

play = QPushButton("Грати")
magazine = QPushButton("Магазин скінів")

v1 = QVBoxLayout()
v1.addWidget(play)
v1.addWidget(magazine)




play.clicked.connect(main.game)
magazine.clicked.connect(shop.open_shop)

window.setLayout(v1)
window.show()
app.exec()


