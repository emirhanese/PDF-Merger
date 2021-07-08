from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QFileDialog, QMessageBox, QLineEdit
from PySide2.QtWidgets import QListWidget
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep
from PyQt5.QtGui import QCursor, QMovie
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os
from PyQt5.QtCore import QUrl
from pathlib import Path

ICON = os.path.abspath("icons/icon.png")
CROSSICON = os.path.abspath("icons/crossicon.png")
CHECKMARK = os.path.abspath("icons/checkmark.jpg")
PDF = os.path.abspath("icons/pdf.gif")

# Loading icons' path to the constant variables.
ICON = ICON.replace("\\", '/')
CROSSICON = CROSSICON.replace("\\", '/')
CHECKMARK = CHECKMARK.replace("\\", '/')
PDF = PDF.replace('\\', '/')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon(
            ICON))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "background-color: rgb(155, 155, 155);")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(15, 0, 800, 600))
        self.label2.setObjectName("label2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 7, 650, 61))
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
                                 "font: 50 15pt \"MS Sans Serif\";\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-style:outlet;\n"
                                 "border-width:2px;\n"
                                 "border-radius:10px;\n"
                                 "border-color: rgb(128, 128, 128);")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 17, 116, 41))
        self.pushButton_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "background-color: rgb(64, 64, 64);\n"
                                        "border-style:outlet;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 530, 121, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "background-color: rgb(64, 64, 64);\n"
                                      "border-style:outlet;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(250, 170, 311, 211))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 530, 121, 41))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "background-color: rgb(64, 64, 64);\n"
                                        "border-style:outlet;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 530, 121, 41))
        self.pushButton_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "background-color: rgb(64, 64, 64);\n"
                                        "border-style:outlet;\n"
                                        "border-width:2px;\n"
                                        "border-radius:10px;\n"
                                        "border-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.msg = QMessageBox()
        self.listWidget.setStyleSheet(""" QListWidget {
            
            background-color:transparent;
            font: 75 14pt \"MS Shell Dlg 2\";
            border-width:5px;
            }


            QListView::item:selected:!active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #ABAFE5, stop: 1 #8588B2);
}

            QListView::item:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);
}

            QListView::item:selected:active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #6a6ea9, stop: 1 #888dd9);
}
            """)

        self.movie = QMovie(
            PDF)
        self.label2.setMovie(self.movie)
        self.movie.start()
        self.paths = []
        self.player = QMediaPlayer()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ESE PDF MERGER"))
        self.label.setText(_translate(
            "MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Dosya Ekle"))
        self.pushButton_2.setText(_translate("MainWindow", "Birleştir"))
        self.pushButton_3.setText(_translate("MainWindow", "Dosya Çıkar"))
        self.pushButton_4.setText(_translate("MainWindow", "Dosya Yolu"))
        self.pushButton.clicked.connect(self.create_dialog_box)
        self.pushButton_3.clicked.connect(self.remove_item)
        self.pushButton_2.clicked.connect(self.merge)
        self.pushButton_4.clicked.connect(self.saveTo)
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonState()
        self.buttonState2()

    def buttonState(self):

        if len(self.paths) == 0:
            self.pushButton_3.setEnabled(False)
            self.pushButton_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                            "color:rgb(255, 255, 255);\n"
                                            "background-color: rgb(224, 224, 224);\n"
                                            "border-style:outlet;\n"
                                            "border-width:2px;\n"
                                            "border-radius:10px;\n"
                                            "border-color: rgb(0, 0, 0);")
            self.pushButton_3.setCursor(QCursor(QtCore.Qt.ArrowCursor))

        else:
            self.pushButton_3.setEnabled(True)
            self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def buttonState2(self):
        if len(self.paths) > 1 and self.label.text() != "..." and self.label.text() != "":
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
            self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        else:
            self.pushButton_2.setEnabled(False)
            self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                            "color:rgb(255, 255, 255);\n"
                                            "background-color: rgb(224, 224, 224);\n"
                                            "border-style:outlet;\n"
                                            "border-width:2px;\n"
                                            "border-radius:10px;\n"
                                            "border-color: rgb(0, 0, 0);")
            self.pushButton_2.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    def saveTo(self):
        path = QFileDialog.getSaveFileName(MainWindow, 'Save file to ...', os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
                                           'PDF Files (*.pdf)', options=QFileDialog.DontUseNativeDialog)
        
        if path[0] != "":
            self.label.setText(path[0])
            self.buttonState2()

    def create_dialog_box(self):
        path = QFileDialog.getOpenFileName()[0]
        filename = path.split("/")[-1]

        if filename != "":
            if filename.endswith(".pdf"):
                self.listWidget.addItem(filename)
                self.paths.append([filename, path])
                if len(self.paths) == 1:
                    self.pushButton_3.setEnabled(True)
                    self.pushButton_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
                    self.pushButton_3.setCursor(
                        QCursor(QtCore.Qt.PointingHandCursor))

                elif len(self.paths) == 2 and self.label.text() != "..." and self.label.text() != "":
                    self.pushButton_2.setEnabled(True)
                    self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
                    self.pushButton_2.setCursor(
                        QCursor(QtCore.Qt.PointingHandCursor))

            else:
                self.error()

    def remove_item(self):
        file = self.listWidget.takeItem(
            self.listWidget.row(self.listWidget.currentItem()))

        try:
            filename = file.text()
            for i in self.paths:
                if i[0] == filename:
                    self.paths.remove(i)

            sleep(0.1)
            self.buttonState()
            self.buttonState2()

        except AttributeError:
            pass

    def merge(self):

        merger = PdfFileMerger()
        path = self.label.text()

        for item in self.paths:
            merger.append(item[1])

        if path.endswith(".pdf"):
            merger.write(path)

        else:
            merger.write(path + ".pdf")
            
        self.completedMessage()
        self.listWidget.clear()
        self.paths.clear()
        self.buttonState()
        self.buttonState2()

    def error(self):
        self.msg.setWindowIcon(QtGui.QIcon(
            CROSSICON))
        self.msg.setWindowTitle("Error !")
        self.msg.setText("You can only add PDF files.")
        self.msg.exec_()
        
    def completedMessage(self):
        self.msg.setWindowIcon(QtGui.QIcon(
            CHECKMARK))
        self.msg.setWindowTitle("Completed !")
        self.msg.setText("PDFs merged successfully.")
        self.msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
