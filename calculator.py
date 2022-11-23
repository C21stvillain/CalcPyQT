from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 20, 330, 40))
        font = QFont()
        font.setFamily(u"SWRomnt")
        self.display.setFont(font)
        self.display.setLayoutDirection(Qt.RightToLeft)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.display.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 392, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_sol = QPushButton(self.gridLayoutWidget)
        self.Btn_sol.setObjectName(u"Btn_sol")
        self.Btn_sol.setSizeIncrement(QSize(1, 1))
        font1 = QFont()
        font1.setFamily(u"8514oem")
        font1.setBold(True)
        font1.setWeight(75)
        self.Btn_sol.setFont(font1)

        self.gridLayout.addWidget(self.Btn_sol, 0, 0, 1, 1)

        self.Btn_7 = QPushButton(self.gridLayoutWidget)
        self.Btn_7.setObjectName(u"Btn_7")
        self.Btn_7.setSizeIncrement(QSize(1, 1))
        self.Btn_7.setFont(font1)

        self.gridLayout.addWidget(self.Btn_7, 1, 0, 1, 1)

        self.Btn_8 = QPushButton(self.gridLayoutWidget)
        self.Btn_8.setObjectName(u"Btn_8")
        self.Btn_8.setSizeIncrement(QSize(1, 1))
        self.Btn_8.setFont(font1)

        self.gridLayout.addWidget(self.Btn_8, 1, 1, 1, 1)

        self.Btn_1 = QPushButton(self.gridLayoutWidget)
        self.Btn_1.setObjectName(u"Btn_1")
        self.Btn_1.setSizeIncrement(QSize(1, 1))
        self.Btn_1.setFont(font1)

        self.gridLayout.addWidget(self.Btn_1, 3, 0, 1, 1)

        self.Btn_bolme = QPushButton(self.gridLayoutWidget)
        self.Btn_bolme.setObjectName(u"Btn_bolme")
        self.Btn_bolme.setSizeIncrement(QSize(1, 1))
        self.Btn_bolme.setFont(font1)

        self.gridLayout.addWidget(self.Btn_bolme, 0, 3, 1, 1)

        self.Btn_carpma = QPushButton(self.gridLayoutWidget)
        self.Btn_carpma.setObjectName(u"Btn_carpma")
        self.Btn_carpma.setSizeIncrement(QSize(1, 1))
        self.Btn_carpma.setFont(font1)

        self.gridLayout.addWidget(self.Btn_carpma, 1, 3, 1, 1)

        self.Btn_yuzde = QPushButton(self.gridLayoutWidget)
        self.Btn_yuzde.setObjectName(u"Btn_yuzde")
        self.Btn_yuzde.setSizeIncrement(QSize(1, 1))
        self.Btn_yuzde.setFont(font1)

        self.gridLayout.addWidget(self.Btn_yuzde, 0, 2, 1, 1)

        self.Btn_sag = QPushButton(self.gridLayoutWidget)
        self.Btn_sag.setObjectName(u"Btn_sag")
        self.Btn_sag.setSizeIncrement(QSize(1, 1))
        self.Btn_sag.setFont(font1)

        self.gridLayout.addWidget(self.Btn_sag, 0, 1, 1, 1)

        self.Btn_4 = QPushButton(self.gridLayoutWidget)
        self.Btn_4.setObjectName(u"Btn_4")
        self.Btn_4.setSizeIncrement(QSize(1, 1))
        self.Btn_4.setFont(font1)

        self.gridLayout.addWidget(self.Btn_4, 2, 0, 1, 1)

        self.Btn_9 = QPushButton(self.gridLayoutWidget)
        self.Btn_9.setObjectName(u"Btn_9")
        self.Btn_9.setSizeIncrement(QSize(1, 1))
        self.Btn_9.setFont(font1)

        self.gridLayout.addWidget(self.Btn_9, 1, 2, 1, 1)

        self.Btn_c = QPushButton(self.gridLayoutWidget)
        self.Btn_c.setObjectName(u"Btn_c")
        self.Btn_c.setSizeIncrement(QSize(1, 1))
        self.Btn_c.setFont(font1)

        self.gridLayout.addWidget(self.Btn_c, 4, 0, 1, 1)

        self.Btn_5 = QPushButton(self.gridLayoutWidget)
        self.Btn_5.setObjectName(u"Btn_5")
        self.Btn_5.setSizeIncrement(QSize(1, 1))
        self.Btn_5.setFont(font1)

        self.gridLayout.addWidget(self.Btn_5, 2, 1, 1, 1)

        self.Btn_2 = QPushButton(self.gridLayoutWidget)
        self.Btn_2.setObjectName(u"Btn_2")
        self.Btn_2.setSizeIncrement(QSize(1, 1))
        self.Btn_2.setFont(font1)

        self.gridLayout.addWidget(self.Btn_2, 3, 1, 1, 1)

        self.Btn_0 = QPushButton(self.gridLayoutWidget)
        self.Btn_0.setObjectName(u"Btn_0")
        self.Btn_0.setSizeIncrement(QSize(1, 1))
        self.Btn_0.setFont(font1)

        self.gridLayout.addWidget(self.Btn_0, 4, 1, 1, 1)

        self.Btn_6 = QPushButton(self.gridLayoutWidget)
        self.Btn_6.setObjectName(u"Btn_6")
        self.Btn_6.setSizeIncrement(QSize(1, 1))
        self.Btn_6.setFont(font1)

        self.gridLayout.addWidget(self.Btn_6, 2, 2, 1, 1)

        self.Btn_toplama = QPushButton(self.gridLayoutWidget)
        self.Btn_toplama.setObjectName(u"Btn_toplama")
        self.Btn_toplama.setSizeIncrement(QSize(1, 1))
        self.Btn_toplama.setFont(font1)

        self.gridLayout.addWidget(self.Btn_toplama, 2, 3, 1, 1)

        self.Btn_cikarma = QPushButton(self.gridLayoutWidget)
        self.Btn_cikarma.setObjectName(u"Btn_cikarma")
        self.Btn_cikarma.setSizeIncrement(QSize(1, 1))
        self.Btn_cikarma.setFont(font1)

        self.gridLayout.addWidget(self.Btn_cikarma, 3, 3, 1, 1)

        self.Btn_esittir = QPushButton(self.gridLayoutWidget)
        self.Btn_esittir.setObjectName(u"Btn_esittir")
        self.Btn_esittir.setSizeIncrement(QSize(1, 1))
        self.Btn_esittir.setFont(font1)

        self.gridLayout.addWidget(self.Btn_esittir, 4, 3, 1, 1)

        self.Btn_3 = QPushButton(self.gridLayoutWidget)
        self.Btn_3.setObjectName(u"Btn_3")
        self.Btn_3.setSizeIncrement(QSize(1, 1))
        self.Btn_3.setFont(font1)

        self.gridLayout.addWidget(self.Btn_3, 3, 2, 1, 1)

        self.Btn_00 = QPushButton(self.gridLayoutWidget)
        self.Btn_00.setObjectName(u"Btn_00")
        self.Btn_00.setSizeIncrement(QSize(1, 1))
        self.Btn_00.setFont(font1)

        self.gridLayout.addWidget(self.Btn_00, 4, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 380, 121, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HesapMakinesi", None))
        self.Btn_sol.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.Btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Btn_bolme.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Btn_carpma.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Btn_yuzde.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.Btn_sag.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Btn_toplama.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Btn_cikarma.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Btn_esittir.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Btn_00.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Made by C21stVillain", None))