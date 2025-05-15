from PyQt5.QtWidgets import (
    QWidget, QPushButton, QPlainTextEdit,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QIcon

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 텍스트 창
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        # 버튼 생성
        self.btn1 = QPushButton('Message', self)
        self.btn2 = QPushButton('Clear', self)

        # 버튼 수평 배치
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        # 전체 수직 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))  # 아이콘은 실제 파일이 있어야 적용됨
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()
