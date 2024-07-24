from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app = QApplication([])
main_win = QWidget()
main_win.show()

main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(500, 200)

text = QLabel("У якому році канал отримав золоту кнопку від YouTube?")

btn = QRadioButton("2005")
btn1 = QRadioButton("2010")
btn2 = QRadioButton("2015")
btn3 = QRadioButton("2020")


main_l =QVBoxLayout()
main_l.addWidget(text)

r1 = QHBoxLayout()
r2 = QHBoxLayout()

r1.addWidget(btn)
r1.addWidget(btn1)
r2.addWidget(btn2)
r2.addWidget(btn3)

def show_right():
    w_right = QMessageBox(main_win)
    w_right.setWindowTitle("Результат")
    w_right.setText("Ти виграв гіроскутер")
    w_right.show()
def show_wrong():
    w_right = QMessageBox(main_win)
    w_right.setWindowTitle("Результат")
    w_right.setText("Неправильно")
    w_right.show()
btn.clicked.connect(show_wrong)
btn1.clicked.connect(show_wrong)
btn2.clicked.connect(show_right)
btn3.clicked.connect(show_wrong)

main_l.addLayout(r1)
main_l.addLayout(r2)
main_win.setLayout(main_l)
main_win.show()
app.exec_()