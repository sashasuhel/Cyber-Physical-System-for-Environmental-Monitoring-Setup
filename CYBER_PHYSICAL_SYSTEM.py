
from PyQt5 import QtCore, QtGui, QtWidgets
from Sensor_Node import dhtTopics
from Data_Schema_Node import Schema_Topics
from Prediction_Node import Prediction_Topics



class CRGS(object):
    def crgs(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/CRGS.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(400, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 91, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 221, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 40, 221, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 70, 221, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 81, 16))
        self.label_4.setObjectName("label_4")

        self.pushButton.clicked.connect(self.fetchTemp_Humid)
        self.pushButton_2.clicked.connect(self.save_current_hundred_Readings)
        self.pushButton_3.clicked.connect(self.get_Predition)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cyber Physical System for Environmental Monitoring and Prediction"))
        self.label_2.setText(_translate("Dialog", "Temperature"))
        self.label_3.setText(_translate("Dialog", "Humidity"))
        self.pushButton.setText(_translate("Dialog", "Display Curent Reading"))
        self.pushButton_2.setText(_translate("Dialog", "Save Current 100 readings"))
        self.pushButton_3.setText(_translate("Dialog", "Generate Prediction Map"))
        self.label_4.setText(_translate("Dialog", "12:02:00"))
        #System Time Fetcher
        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

    def displayTime(self):
        self.label_4.setText(QtCore.QDateTime.currentDateTime().time().toString())
        if(str(self.label_4.text())=="06:00:00"):
            print('[autoFetch]')
            self.save_current_hundred_Readings()

        elif(str(self.label_4.text())=="12:00:00"):
            print('[autoFetch]')
            self.save_current_hundred_Readings()

        elif(str(self.label_4.text())=="16:00:00"):
            print('[autoFetch]')
            self.save_current_hundred_Readings()

        elif(str(self.label_4.text())=="21:00:00"):
            print('[autoFetch]')
            self.save_current_hundred_Readings()


    def fetchTemp_Humid(self):
        dataFetched=dhtTopics.dhtMessages()
        self.lineEdit.setText(str(dataFetched[0]))
        self.lineEdit_2.setText(str(dataFetched[1]))

    def save_current_hundred_Readings(self):
        location='Cybernetics_Rpi\Data_Schema_Node\SensorData.csv'
        ACK=Schema_Topics.recordDATA(location)
        if(ACK==True):
            print('[DATA SAVED]')

    def get_Predition(self):
        Prediction_Topics.Prediction()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CRGS()
    ui.crgs(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
