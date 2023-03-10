# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employee_Management.ui'
#
# Created by: Suraj Giri
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from audioop import add
from dataclasses import dataclass
from email.headerregistry import Address
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QWidget,QApplication

class Ui_Employee_Management(object):
    def setupUi(self, Employee_Management):
        Employee_Management.setObjectName("Employee_Management")
        Employee_Management.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(Employee_Management)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 120, 651, 421))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.groupBox.setObjectName("groupBox")
        self.newEmp = QtWidgets.QPushButton(self.groupBox)
        self.newEmp.setGeometry(QtCore.QRect(110, 360, 131, 41))
        self.newEmp.setObjectName("newEmp")
        self.updateEmp = QtWidgets.QPushButton(self.groupBox)
        self.updateEmp.setGeometry(QtCore.QRect(250, 360, 141, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/updated.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateEmp.setIcon(icon)
        self.updateEmp.setObjectName("updateEmp")
        self.delEmp = QtWidgets.QPushButton(self.groupBox)
        self.delEmp.setGeometry(QtCore.QRect(400, 360, 141, 41))
        self.delEmp.setAutoFillBackground(False)
        self.delEmp.setAutoDefault(False)
        self.delEmp.setDefault(False)
        self.delEmp.setFlat(False)
        self.delEmp.setObjectName("delEmp")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.fname = QtWidgets.QLineEdit(self.groupBox)
        self.fname.setGeometry(QtCore.QRect(110, 40, 181, 20))
        self.fname.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLineEdit(self.groupBox)
        self.lname.setGeometry(QtCore.QRect(110, 80, 181, 20))
        self.lname.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.lname.setObjectName("lname")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 81, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.baseSalary = QtWidgets.QLineEdit(self.groupBox)
        self.baseSalary.setGeometry(QtCore.QRect(430, 40, 181, 20))
        self.baseSalary.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.baseSalary.setObjectName("baseSalary")
        self.tax = QtWidgets.QLineEdit(self.groupBox)
        self.tax.setGeometry(QtCore.QRect(430, 70, 181, 20))
        self.tax.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.tax.setObjectName("tax")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(340, 70, 81, 16))
        self.label_4.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(340, 100, 81, 16))
        self.label_9.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.netSalary = QtWidgets.QLineEdit(self.groupBox)
        self.netSalary.setGeometry(QtCore.QRect(430, 100, 181, 20))
        self.netSalary.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.netSalary.setObjectName("netSalary")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_10.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.address = QtWidgets.QPlainTextEdit(self.groupBox)
        self.address.setGeometry(QtCore.QRect(110, 120, 211, 101))
        self.address.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.address.setObjectName("address")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 240, 81, 16))
        self.label_11.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_11.setObjectName("label_11")
        self.dob = QtWidgets.QDateEdit(self.groupBox)
        self.dob.setGeometry(QtCore.QRect(110, 240, 110, 22))
        self.dob.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.dob.setObjectName("dob")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(20, 290, 81, 16))
        self.label_12.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_12.setObjectName("label_12")
        self.mobileno = QtWidgets.QLineEdit(self.groupBox)
        self.mobileno.setGeometry(QtCore.QRect(110, 290, 181, 20))
        self.mobileno.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.mobileno.setObjectName("mobileno")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(340, 130, 101, 21))
        self.label_14.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(460, 130, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.findEmp = QtWidgets.QPushButton(self.centralwidget)
        self.findEmp.setGeometry(QtCore.QRect(570, 90, 151, 31))
        self.findEmp.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.findEmp.setObjectName("findEmp")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(300, 30, 201, 31))
        self.label_13.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.label_13.setObjectName("label_13")
        Employee_Management.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Employee_Management)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Employee_Management.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Employee_Management)
        self.statusbar.setObjectName("statusbar")
        Employee_Management.setStatusBar(self.statusbar)

        self.retranslateUi(Employee_Management)
        QtCore.QMetaObject.connectSlotsByName(Employee_Management)
         #Button Actions
        self.newEmp.clicked.connect(self.newEmployee)
        self.updateEmp.clicked.connect(self.updateEmployee)
        self.delEmp.clicked.connect(self.deleteEmployee)
        self.findEmp.clicked.connect(self.findEmployee)

    def retranslateUi(self, Employee_Management):
        _translate = QtCore.QCoreApplication.translate
        Employee_Management.setWindowTitle(_translate("Employee_Management", "Employee Management"))
        self.groupBox.setTitle(_translate("Employee_Management", "Profile"))
        self.newEmp.setToolTip(_translate("Employee_Management", "Add New Employee"))
        self.newEmp.setText(_translate("Employee_Management", "New Employee"))
        self.updateEmp.setToolTip(_translate("Employee_Management", "Update Employee Profile"))
        self.updateEmp.setText(_translate("Employee_Management", "Update Employee"))
        self.delEmp.setToolTip(_translate("Employee_Management", "Delete Employee Profile"))
        self.delEmp.setText(_translate("Employee_Management", "Delete Employee"))
        self.label.setText(_translate("Employee_Management", "First Name:"))
        self.label_2.setText(_translate("Employee_Management", "Last Name:"))
        self.label_3.setText(_translate("Employee_Management", "Basic Salary:"))
        self.label_4.setText(_translate("Employee_Management", "Tax:"))
        self.label_9.setText(_translate("Employee_Management", "Net Salary:"))
        self.label_10.setText(_translate("Employee_Management", "Address:"))
        self.label_11.setText(_translate("Employee_Management", "DOB:"))
        self.label_12.setText(_translate("Employee_Management", "Mobile No:"))
        self.label_14.setText(_translate("Employee_Management", "Employee Type:"))
        self.comboBox.setItemText(0, _translate("Employee_Management", "Select Type"))
        self.comboBox.setItemText(1, _translate("Employee_Management", "Administrator"))
        self.comboBox.setItemText(2, _translate("Employee_Management", "Employee"))
        self.findEmp.setToolTip(_translate("Employee_Management", "Find Employee"))
        self.findEmp.setText(_translate("Employee_Management", "Find Employee"))
        self.label_13.setText(_translate("Employee_Management", "Employee Management"))

    def Connection(self):
        pass
        
    def findEmployee(self):
        no, ok=QInputDialog.getText(QWidget(self.centralwidget),"Employee","Employee ID")
        if no!='':
            import mysql.connector
            cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
            mycursor=cn.cursor()
            mycursor.execute("select * from trs_employee where emp_id like '"+no+"';")
            r=mycursor.fetchone()
            if r==None:
                Message("Employee","Not Found")
            else:
                Message("Employee","Found")
                self.fname.setText(r[1])
                self.address.setPlainText(r[2])
                self.dob.setDate(r[3])
                self.mobileno.setText(str(r[4]))
                self.baseSalary.setText(str(r[5]))
                self.tax.setText(str(r[6]))
                self.netSalary.setText(str(r[7]))
                self.netSalary.setEnabled(False)
                self.tax.setEnabled(False)
                self.fname.setEnabled(False)
                self.baseSalary.setEnabled(False)
                self.lname.setEnabled(False)
                
        else:
            Message("Employee","Empty")  
              
    def idcreate(self):
            import random
            empid="SSRTRS"+str(random.randint(1,99999))
            return empid

    def idGenerator(self):
            empid=self.idcreate()
            import mysql.connector
            cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
            c=cn.cursor()
            c.execute("SELECT `emp_id` FROM `trs_employee` WHERE emp_id like '"+empid+"' ")
            r=c.fetchone()
            if r!=None:
                self.newEmployee(empid)
            else:
                self.idcreate()
            return empid
            

    def clear(self):
        self.fname.clear()
        self.lname.clear()
        self.address.clear()
        self.dob.date().currentDate()
        self.mobileno.clear()
        self.baseSalary.clear()
        self.tax.clear()
        self.netSalary.clear()
        self.comboBox.setCurrentIndex(0)



    def newEmployee(self,id):
            try:
                name=str(self.fname.text())+" "+str(self.lname.text())
                id=self.idGenerator()
                address=self.address.toPlainText()  
                dob=str(self.dob.date().toPyDate())
                mobno=self.mobileno.text()
                bsal=float(self.baseSalary.text())
                tax=float(self.tax.text())
                etype=self.comboBox.currentText()
                netsal=bsal*18-tax
                self.netSalary.setEnabled(False)
                self.netSalary.setText(str(netsal))
                import mysql.connector
                cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
                c1=cn.cursor()
                c1.execute("SELECT `emp_mobno` FROM `trs_employee` where `emp_mobno` like '"+mobno+"'; ")
                r=c1.fetchone()
                if r==None:
                    print(id,name,address,dob,mobno,bsal,tax,netsal,etype)
                    if len(mobno)!=10:
                        Message("Employee","Invalid Number")
                    elif len(name)<3 and len(address)<4 and len(bsal<2) and len(tax)<2 and etype=="Select Type":
                        Message("Employee","Invalid Form Entry")
                    else:
                        q=("INSERT INTO `trs_employee`(`emp_id`, `emp_name`, `emp_address`, `emp_dob`, `emp_mobno`, `emp_sal`, `emp_saltax`, `emp_netsal`, `emp_type`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
                        v=(id,name,address,dob,mobno,bsal,tax,netsal,etype)
                        c=cn.cursor()
                        c.execute(q,v)
                        cn.commit()
                        if cn.commit:
                                s="Welcome Aboard Your Employee ID: -"+id
                                Message("Employee",s)
                        else:
                            Message("Employee","Went Wrong")
                else:
                    Message("Employee","Employee Already Exist!!")
                    self.clear()

            except TypeError as t:
                #cn.rollback()
                print(t)
                Message("Employee","Something went wrong")
                self.clear()
            
    def updateEmployee(self):
           try:
                name=self.fname.text()
                address=self.address.toPlainText()  
                dob=str(self.dob.date().toPyDate())
                mobno=self.mobileno.text()
                etype=self.comboBox.currentText()
                self.netSalary.setEnabled(False)
                import mysql.connector
                cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
                print(name,address,dob,mobno,etype)
                if len(mobno)!=10:
                    Message("Employee","Invalid Number")
                elif len(name)<3 and len(address)<4 and etype=="Select Type":
                    Message("Employee","Invalid Form Entry")
                else:
                    no, ok=QInputDialog.getText(QWidget(self.centralwidget),"Employee","Enter Employee ID")
                    q=("UPDATE `trs_employee` SET `emp_address`=%s,`emp_dob`=%s,`emp_mobno`=%s WHERE emp_id like '"+no+"' ")
                    v=(address,dob,mobno)
                    c=cn.cursor()
                    c.execute(q,v)
                    cn.commit()
                    if cn.commit:
                        s="Data Updated: "+str(no)
                        Message("Employee",s)
                    else:
                        Message("Employee","Went Wrong")
           except TypeError as t:
                #cn.rollback()
                print(t)
                Message("Employee","Something went wrong")
                self.clear()

    def deleteEmployee(self):
        try:
            import mysql.connector
            cn=mysql.connector.connect(host="localhost",user="root",password="",database="trs")
            no, ok=QInputDialog.getText(QWidget(self.centralwidget),"Employee","Enter Employee ID")
            
            if no!='':
                q="DELETE FROM `trs_employee` where emp_id = %s "
                v=(no,)
                c=cn.cursor()
                c.execute(q,v)
                cn.commit()
                if cn.commit:
                    s="Employee Deleted: "+str(no)
                    Message("Employee",s)
                else:
                    Message("Employee","Went Wrong")
        except TypeError as t:
                print(t)
                Message("Employee","Something went wrong")
                self.clear()

           


def Message(h,mssg):
        msg = QMessageBox()
        msg.setWindowTitle(h)
        msg.setText(mssg)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Employee_Management = QtWidgets.QMainWindow()
    ui = Ui_Employee_Management()
    ui.setupUi(Employee_Management)
    Employee_Management.show()
    sys.exit(app.exec_())
