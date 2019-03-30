# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QInputDialog
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox
from PyQt5.QtGui import QPalette, QPixmap

class OnStepCTF(QWidget):
# class OnStepCTF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #初始外形
        self.setWindowTitle('CTF沙雕工具 v1.0 by Mki603')
        self.setGeometry(100,100,900,400)

        #  一键按钮
        self.Btn_1 = QPushButton('一键暴打出题人', self)
        self.Btn_1.clicked[bool].connect(self.OnstepAction)

        self.Btn_2 = QPushButton('一键获取flag', self)
        self.Btn_2.clicked[bool].connect(self.OnstepAction)

        self.Btn_3 = QPushButton('一键打断复读', self)
        self.Btn_3.clicked[bool].connect(self.OnstepAction)

        self.Btn_4 = QPushButton('一键开启复读', self)
        self.Btn_4.clicked[bool].connect(self.OnstepAction)

        self.Btn_5 = QPushButton('一键膜dalao', self)
        self.Btn_5.clicked[bool].connect(self.OnstepAction)

        # 加急名单
        self.Label_1 = QLabel(self)
        text = "出题人A\n出题人B\n出题人C\n出题人D\n"
        self.Label_1.setText(text)
        self.Btn_Add = QPushButton('添加名单', self)
        self.Btn_Add.clicked[bool].connect(self.ShowPerson)

        # 找点乐子
        self.Bilibili = QLabel(self)
        self.Bilibili.setText('<a href="www.bilibili.com">bilibili ( ゜ -゜)つロ 乾杯~</a>')
        self.Bilibili.setOpenExternalLinks(True)

        self.BilibiliTV = QLabel(self)
        self.BilibiliTV.setPixmap(QPixmap('C:\\Users\\Mki_6\\Desktop\\Code\\Pic\\bilibili.png'))
        self.BilibiliTV.setScaledContents(True)

        self.Chess = QLabel(self)
        self.Chess.setText('<a href="#">内网五子棋！启动！</a>')

        self.ChessPic = QLabel(self)
        self.ChessPic.setPixmap(QPixmap('C:\\Users\\Mki_6\\Desktop\\Code\\Pic\\five.png'))
        self.ChessPic.resize(100,100)
        self.ChessPic.setScaledContents(True)

        # 弹性布局
        self.CreateGridLayout()
        self.setLayout(self.windowLayout)
        self.show()

    def CreateGridLayout(self):
        self.BtnBox = QGroupBox("快捷按钮")
        layout = QGridLayout()
        layout.addWidget(self.Btn_1,1,1)
        layout.addWidget(self.Btn_2,2,1)
        layout.addWidget(self.Btn_3,3,1)
        layout.addWidget(self.Btn_4,4,1)
        layout.addWidget(self.Btn_5,5,1)
        self.BtnBox.setLayout(layout)

        self.ListBox = QGroupBox("枪毙名单")
        layout = QGridLayout()
        layout.addWidget(self.Label_1,1,2)
        layout.addWidget(self.Btn_Add,2,2)
        self.ListBox.setLayout(layout)

        self.GameBox = QGroupBox("摸鱼入口")
        layout = QGridLayout()
        layout.addWidget(self.Bilibili,1,1)
        layout.addWidget(self.BilibiliTV,1,2)
        layout.addWidget(self.Chess,2,2)
        layout.addWidget(self.ChessPic,2,1)
        self.GameBox.setLayout(layout)

        # self.boxlayout = QGroupBox()
        # layout = QGridLayout()
        # layout.addWidget(self.BtnBox,1,1)
        # layout.addWidget(self.ListBox,1,2)
        # layout.addWidget(self.GameBox,1,3)
        # self.boxlayout.setLayout(layout)


        
        self.windowLayout = QHBoxLayout()
        self.windowLayout.addWidget(self.BtnBox)
        self.windowLayout.addWidget(self.ListBox)
        self.windowLayout.addWidget(self.GameBox)

    def ShowPerson(self):
        text, ok = QInputDialog.getText(self,"本月加急","name: ")
        if ok:
            newtext = self.Label_1.text() + str(text) + "\n"
            self.Label_1.setText(newtext)

    def OnstepAction(self):
        sender = self.sender()
        action = sender.text()
        if action == '一键暴打出题人':
            reply = '出题人已被击毙'
        elif action == '一键获取flag':
            reply = 'flag is flag{b4608f992f32586e17c334c6633c8925}'
        elif action == '一键打断复读':
            reply = '一位群友及时打断了复读'
        else:
            reply = '功能还在开发中....'
        message = QMessageBox.question(self,'一个消息',reply)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tool = OnStepCTF()
    sys.exit(app.exec_())