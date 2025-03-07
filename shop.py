from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from file_helper17 import *




def open_shop():
    window = QDialog()
    catalog = [
        {
            "name": "skin 1",
            "kartinka": "Знімок_екрана_2025-01-26_142901-removebg-preview.png",
            'gun':1,
            "price": 200
        },
        {
            "name": "skin 2",
            "kartinka": "Знімок_екрана_2025-02-19_202812-removebg-preview.png",
            'gun': 0.4,
            "price": 250
        },
        {
            "name": "skin 2",
            "kartinka": "Знімок_екрана_2025-02-19_202925-removebg-preview.png",
            'gun': 1.5,
            "price": 500
        },
        {
            "name": "skin 2",
            "kartinka": "Знімок_екрана_2025-02-19_202951-removebg-preview.png",
            'gun': 0.2,
            "price": 500
        },
    ]



    data = read_from_file()
    score_lbl = QLabel("Score: " + str(data['score']))
    main_line = QVBoxLayout()
    main_line.addWidget(score_lbl)

    h1 = QHBoxLayout()
    def buy_func(p, skin,gun):
        data = read_from_file()
        print(p)
        if data["score"] >= p:
            data["score"] -= p
            data["skin"] = skin
            data['gun'] = gun
            write_in_file(data)

    for element in catalog:
        v1 = QVBoxLayout()
        name = QLabel(element['name'])
        katinka = QLabel("kartinka")
        pixmap = QPixmap(element['kartinka'])
        pixmap = pixmap.scaledToWidth(100)
        katinka.setPixmap(pixmap)
        price = QLabel(str(element['price']))
        buy_btn = QPushButton("BUY")
        buy_btn.clicked.connect(lambda _,
                                        my_price=element['price'],
                                        skin=element['kartinka'],
                                        gun=element['gun']:
                                buy_func(my_price,skin,gun))
        v1.addWidget(name)
        v1.addWidget(katinka)
        v1.addWidget(price)
        v1.addWidget(buy_btn)
        h1.addLayout(v1)
    main_line.addLayout(h1)
    window.setLayout(main_line)
    window.exec()