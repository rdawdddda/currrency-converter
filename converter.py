from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)
from PyQt5 import QtGui
import pywinstyles

def rubles_to_dollars(input_rubles, result_container):
    ru_count = float(input_rubles.text())
    result = str(ru_count/80.0) +"$"
    result_container.setText(result)
def dollars_to_rubles(input_rubles, result_container):
    dol_count = float(input_rubles.text())
    result = str(dol_count*80.0) + "₽"
    result_container.setText(result)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

result_container = QLabel("Тут будет результат")

input_rub = QLineEdit()
input_rub.setPlaceholderText("Введите ₽")
input_dollars = QLineEdit()
input_dollars.setPlaceholderText("Введите $")

btn_rubles = QPushButton("перевести\nрубли в доллары")
btn_rubles.clicked.connect(
    lambda: rubles_to_dollars(input_rub, result_container)
)

btn_dollars = QPushButton("перевести\nдоллары в рубли")
btn_dollars.clicked.connect(
    lambda: dollars_to_rubles(input_dollars , result_container)
)



layout_h1 = QHBoxLayout()
layout_h1.addWidget(input_dollars)
layout_h1.addWidget(btn_dollars)

layout_h2 = QHBoxLayout()
layout_h2.addWidget(input_rub)
layout_h2.addWidget(btn_rubles)

layout.addLayout(layout_h1)
layout.addLayout(layout_h2)





window.setWindowIcon(QtGui.QIcon('convert.png'))

pywinstyles.apply_style(window, "dark")

window.setStyleSheet("background:white;")
window.setWindowTitle("Конвертация валют")

layout.addWidget(result_container)

window.setLayout(layout)
window.resize(350, 0)
window.show()
app.exec_()