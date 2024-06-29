from PyQt5.QtWidgets import*
import random
app = QApplication([])

window = QWidget()

winner_lbl = QWidget()

winner_lbl = QLabel("Переможець")
generate_winer_btn = QPushButton("Отримати переможця")

main_line = QVBoxLayout()
main_line.addWidget(winner_lbl)
main_line.addWidget(generate_winer_btn)

def winner_func():
    num = random.randint(1,4)
    winner_lbl.setText("Перемржець" + str(num))

generate_winer_btn.clicked.connect(winner_func)




window.setLayout(main_line)
window.show()
app.exec()