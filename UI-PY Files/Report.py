# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Report_Generation.ui'
#
# Created by: Suraj Giri
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from fpdf import FPDF
from datetime import date

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 90, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.date_show = QtWidgets.QLabel(self.centralwidget)
        self.date_show.setGeometry(QtCore.QRect(270, 30, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_show.setFont(font)
        self.date_show.setObjectName("date_show")
        self.tourRegister = QtWidgets.QPushButton(self.centralwidget)
        self.tourRegister.setGeometry(QtCore.QRect(120, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tourRegister.setFont(font)
        self.tourRegister.setObjectName("tourRegister")
        self.hotelBook = QtWidgets.QPushButton(self.centralwidget)
        self.hotelBook.setGeometry(QtCore.QRect(120, 220, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.hotelBook.setFont(font)
        self.hotelBook.setObjectName("hotelBook")
        self.vehicleRegister = QtWidgets.QPushButton(self.centralwidget)
        self.vehicleRegister.setGeometry(QtCore.QRect(120, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.vehicleRegister.setFont(font)
        self.vehicleRegister.setObjectName("vehicleRegister")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        d=date.today()
        d="Date: "+str(d.strftime('%d/%m/%Y'))
        self.date_show.setText(d)
            

        self.tourRegister.clicked.connect(self.TourPDF)
        self.hotelBook.clicked.connect(self.HotelPDF)
        self.vehicleRegister.clicked.connect(self.VehiclePDF)
        
    def connection(self):
        import mysql.connector
        cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
        return cn

    def TourPDF(self):
        try:
            cn=self.connection()
            mycursor=cn.cursor()
            mycursor.execute("SELECT `customer_name`,`customer_email`,`customer_phone`,`customer_selected_package`,`customer_payment`,`trip_status` FROM `tour_registration`")
            r=mycursor.fetchall()
            d=date.today()
            d="Date: "+str(d.strftime('%d/%m/%Y'))
            pdf=FPDF()
            pdf.add_page()
            epw = pdf.w - 2*pdf.l_margin
            pdf.set_font("Times","B",size=11)
            pdf.cell(epw,0.0,str(d),align="R")
            pdf.ln(10)
            pdf.set_font("Times","B",size=14)
            pdf.cell(epw,0.0,"Tour Registration Data",align="C")
            pdf.set_font("Times","B",size=10)
            pdf.ln(10)
            th = pdf.font_size
            col_width = pdf.epw /6
            pdf.cell(col_width, th, "Customer Name", border=1)
            pdf.cell(col_width, th, "Customer E-Mail", border=1)
            pdf.cell(col_width, th, "Customer Phone", border=1)
            pdf.cell(col_width, th, "Selected Package", border=1)
            pdf.cell(col_width, th, "Customer Payment", border=1)
            pdf.cell(col_width, th, "Trip Status", border=1)
            pdf.ln(th)

            pdf.set_font("Times",size=10)

            for row in r:
                pdf.cell(col_width, 2*th, row[0], border=1)
                pdf.cell(col_width, 2*th, row[1], border=1)
                pdf.cell(col_width, 2*th, row[2], border=1)
                pdf.cell(col_width, 2*th, row[3], border=1)
                pdf.cell(col_width, 2*th, str(row[4]), border=1)
                pdf.cell(col_width, 2*th, row[5], border=1)
                pdf.ln(2*th)
            p="C:\\Tour_Registered.pdf"
            pdf.output(p)
            mycursor.close()
            cn.close()
            self.Message("Report", 'Tour Report Generated on C Drive')
        except ValueError as v:
            print(v)
            
    def HotelPDF(self):
        try:
            cn=self.connection()
            mycursor=cn.cursor()
            mycursor.execute("SELECT `customer_name`, `customer_number`, `room_booked`, `no_of_people`, `hotel_checkin`, `hotel_checkout`, `date_booked` FROM `hotel_booking` ")
            r=mycursor.fetchall()
            d=date.today()
            d="Date: "+str(d.strftime('%d/%m/%Y'))
            pdf=FPDF()
            pdf.add_page()
            epw = pdf.w - 2*pdf.l_margin
            pdf.set_font("Times","B",size=11)
            pdf.cell(epw,0.0,str(d),align="R")
            pdf.ln(10)
            pdf.set_font("Times","B",size=14)
            pdf.cell(epw,0.0,"Hotel Booking Data",align="C")
            pdf.set_font("Times","B",size=10)
            pdf.ln(10)
            th = pdf.font_size
            col_width = pdf.epw /7
            pdf.cell(col_width, th, "Customer Name", border=1)
            pdf.cell(col_width, th, "Customer Phone", border=1)
            pdf.cell(col_width, th, "Room Booked", border=1)
            pdf.cell(col_width, th, "NO. Of People", border=1)
            pdf.cell(col_width, th, "Check-In", border=1)
            pdf.cell(col_width, th, "Check-Out", border=1)
            pdf.cell(col_width, th, "Date Booked", border=1)
            pdf.ln(th)

            pdf.set_font("Times",size=10)

            for row in r:
                pdf.cell(col_width, 2*th, row[0], border=1)
                pdf.cell(col_width, 2*th, row[1], border=1)
                pdf.cell(col_width, 2*th, row[2], border=1)
                pdf.cell(col_width, 2*th, row[3], border=1)
                pdf.cell(col_width, 2*th, str(row[4]), border=1)
                pdf.cell(col_width, 2*th, str(row[5]), border=1)
                pdf.cell(col_width, 2*th, str(row[6]), border=1)
                pdf.ln(2*th)
            p="C:\\Hotel_Booked.pdf"
            pdf.output(p)
            mycursor.close()
            cn.close()
            self.Message("Report", 'Hotel Booking Report Generated on C Drive')
        except ValueError as v:
            print(v)


    def VehiclePDF(self):
        try:
            cn=self.connection()
            mycursor=cn.cursor()
            mycursor.execute("SELECT `customer_name`, `customer_license`, `customer_phone`,`customer_drop`, `vehicle_type`, `amount` FROM `vehicle_registration`")
            r=mycursor.fetchall()
            d=date.today()
            d="Date: "+str(d.strftime('%d/%m/%Y'))
            pdf=FPDF()
            pdf.add_page()
            epw = pdf.w - 2*pdf.l_margin
            pdf.set_font("Times","B",size=11)
            pdf.cell(epw,0.0,str(d),align="R")
            pdf.ln(10)
            pdf.set_font("Times","B",size=14)
            pdf.cell(epw,0.0,"Vehicle Registration Data",align="C")
            pdf.set_font("Times","B",size=10)
            pdf.ln(10)
            th = pdf.font_size
            col_width = pdf.epw /6
            pdf.cell(col_width, th, "Customer Name", border=1)
            pdf.cell(col_width, th, "Customer License", border=1)
            pdf.cell(col_width, th, "Customer Phone", border=1)
            pdf.cell(col_width, th, "Drop Date", border=1)
            pdf.cell(col_width, th, "Vehicle Type", border=1)
            pdf.cell(col_width, th, "Amount", border=1)
            pdf.ln(th)

            pdf.set_font("Times",size=10)

            for row in r:
                pdf.cell(col_width, 2*th, row[0], border=1)
                pdf.cell(col_width, 2*th, row[1], border=1)
                pdf.cell(col_width, 2*th, row[2], border=1)
                pdf.cell(col_width, 2*th, str(row[3]), border=1)
                pdf.cell(col_width, 2*th, row[4], border=1)
                pdf.cell(col_width, 2*th, str(row[5]), border=1)
                pdf.ln(2*th)
            p="C:\\Vehicle_Registered.pdf"
            pdf.output(p)
            mycursor.close()
            cn.close()
            self.Message("Report", 'Vehicle Report Generated on C Drive')
        except ValueError as v:
            print(v)

    def Message(self,h,mssg):
            msg = QMessageBox()
            msg.setWindowTitle(h)
            msg.setText(mssg)
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Generation"))
        self.label.setText(_translate("MainWindow", "Report Generation"))
        self.date_show.setText(_translate("MainWindow", "Date:-"))
        self.tourRegister.setText(_translate("MainWindow", "Tour Registration"))
        self.hotelBook.setText(_translate("MainWindow", "Hotel Booking"))
        self.vehicleRegister.setText(_translate("MainWindow", "Vehicle Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
