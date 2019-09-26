# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



""" Author : Ramazan GÜVEN 
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit,QMessageBox,QCheckBox
import sys
import qimage2ndarray
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
 
 

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(920, 920)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(920, 920))
        Form.setMaximumSize(QtCore.QSize(920, 920))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 40, 702, 820))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_10.setMaximumSize(QtCore.QSize(5000, 40))
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMaximumSize(QtCore.QSize(720, 480))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("background-color: rgb(129, 184, 255);\n"
                                    "color: rgb(255, 7, 60);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(720, 480))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setStyleSheet("color: rgb(7, 19, 255);\n"
                                    "background-color: rgb(6, 255, 14);\n"
                                    "font: 75 12pt \"Rockwell\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()



        self.pushButton_1.clicked.connect(self.getImage)
        self.pushButton_4.clicked.connect(self.img2gray)
        self.pushButton_6.clicked.connect(self.img2gaussian)
        self.pushButton_5.clicked.connect(self.img2canny)
        self.pushButton_7.clicked.connect(self.img_mask)
        self.pushButton_8.clicked.connect(self.hough_line)
        self.pushButton_9.clicked.connect(self.hough_line_combo)
        self.pushButton_10.clicked.connect(self.save_converted_image)
       
       
        self.native = QCheckBox()
        self.native.setText("Use native file dialog.")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()
       
       
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Open Image"))
        self.pushButton_4.setText(_translate("Form", "Gray"))
        self.pushButton_6.setText(_translate("Form", "Gaussian"))
        self.pushButton_5.setText(_translate("Form", "Canny Edge Detection"))
        self.pushButton_7.setText(_translate("Form", "Mask Edges"))
        self.pushButton_8.setText(_translate("Form", "Hough Lines"))
        self.pushButton_9.setText(_translate("Form", "Combine Line Original Image"))
        self.pushButton_10.setText(_translate("Form", "Save Converted Image"))
        self.label_4.setText(_translate("Form", "Understanding Self Driving With Images"))
        self.label_5.setText(_translate("Form", "ORIGINAL IMAGE"))

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.gif *.jpeg *.png)")                                  
        self.imagePath = fname[0]
        pixmap = QPixmap(self.imagePath)
        pixmap5 = pixmap.scaled(720,420)
        self.label_1.setPixmap(QPixmap(pixmap5))
        print(pixmap.width())
        print(pixmap.height())
        #self.resize(pixmap.width(),pixmap.height())
        #self.label_1.setText("Orijinal Image")
        #for test #self.label_3.setPixmap(QPixmap(pixmap5))
        
    
    def img2gray(self):
        img=QtGui.QImage(self.imagePath)
        #image=QPixmap(self.imagePath)
        convert=qimage2ndarray.rgb_view(img)
        print(type(convert)) #numpy
        print(convert.shape) 
        converter=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
        converter=cv2.resize(converter,(720,420))
        #pixmap5 = converter.scaled(720,420)

        last =qimage2ndarray.array2qimage(converter)
        self.label_3.setPixmap(QPixmap(last))
        self.label_5.setText("GRAY IMAGE")
    def img2gaussian(self):
        img=QtGui.QImage(self.imagePath)
        convert=qimage2ndarray.rgb_view(img)
        gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(9,9),0)
        resized=cv2.resize(blur,(720,420))
        last=qimage2ndarray.array2qimage(resized)
        self.label_3.setPixmap(QPixmap(last))
        self.label_5.setText("Gaussian Blur Image ksize_for_this_image=(9,9)")


    def img2canny(self):
        img=QtGui.QImage(self.imagePath)
        convert=qimage2ndarray.rgb_view(img)
        gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        canny=cv2.Canny(blur,50,150)
        resized=cv2.resize(canny,(720,420))
        last=qimage2ndarray.array2qimage(resized)
        self.label_3.setPixmap(QPixmap(last))
        self.label_5.setText("Canny Edge Detection")
    
    def img_mask(self):
        
        
        buttonReply = QMessageBox.question(self, 'Edge Question', "Do you want see only triangle over the image?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            img=QtGui.QImage(self.imagePath)
            convert=qimage2ndarray.rgb_view(img)
            gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
            blur=cv2.GaussianBlur(gray,(5,5),0)
            canny=cv2.Canny(blur,50,150)
            resized1=cv2.resize(canny,(720,420))
            height=canny.shape[0]
            polygons=np.array([[(100,height),(680,height),(370,150)]
                              ])
            mask=np.zeros_like(resized1)
            cv2.fillPoly(mask,polygons,255)
            #masked_image=cv2.bitwise_and(canny,mask)
            plt.imshow(resized1)
            plt.show()
            resized=cv2.resize(mask,(720,420))
            #last=qimage2ndarray.array2qimage(resized)
            masked=qimage2ndarray.array2qimage(resized)
            self.label_3.setPixmap(QPixmap(masked))
            self.label_5.setText("Canny Edge Detection Mask Triangle")
        else:
            print('No clicked.')
            img=QtGui.QImage(self.imagePath)
            convert=qimage2ndarray.rgb_view(img)
            gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
            blur=cv2.GaussianBlur(gray,(5,5),0)
            canny=cv2.Canny(blur,50,150)
            resized1=cv2.resize(canny,(720,420))
            height=canny.shape[0]
            polygons=np.array([[(100,height),(680,height),(360,150)]
                              ])
            mask=np.zeros_like(resized1)
            cv2.fillPoly(mask,polygons,255)
            masked_image=cv2.bitwise_and(resized1,mask)
            resized=cv2.resize(masked_image,(720,420))
            #last=qimage2ndarray.array2qimage(resized)
            masked=qimage2ndarray.array2qimage(resized)
            self.label_3.setPixmap(QPixmap(masked))
            self.label_5.setText("Cropped image")
  
        
    def hough_line(self):
            img=QtGui.QImage(self.imagePath)
            convert=qimage2ndarray.rgb_view(img)
            gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
            blur=cv2.GaussianBlur(gray,(5,5),0)
            canny=cv2.Canny(blur,50,150)
            resized1=cv2.resize(canny,(720,420))
            height=canny.shape[0]
            polygons=np.array([[(100,height),(680,height),(360,150)]
                              ])
            mask=np.zeros_like(resized1)
            cv2.fillPoly(mask,polygons,255)
            masked_image=cv2.bitwise_and(resized1,mask)
            resized=cv2.resize(masked_image,(720,420))
            
            lines=cv2.HoughLinesP(resized,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
            original_image=np.zeros_like(convert)
            if lines is not None:
                for line in lines:
                    print(line)
                    x1,y1,x2,y2=line.reshape(4)    
                    cv2.line(original_image,(x1,y1),(x2,y2),(255,0,0),10)
   
       
            masked=qimage2ndarray.array2qimage(original_image) 
            self.label_3.setPixmap(QPixmap(masked))
            self.label_5.setText("Hough Line")
    
        
    def hough_line_combo(self):
            img=QtGui.QImage(self.imagePath)
            convert=qimage2ndarray.rgb_view(img)
            convert_resize=cv2.resize(convert,(720,420))
            
            gray=cv2.cvtColor(convert,cv2.COLOR_BGR2GRAY)
            blur=cv2.GaussianBlur(gray,(5,5),0)
            canny=cv2.Canny(blur,50,150)
            resized1=cv2.resize(canny,(720,420))
            height=canny.shape[0]
            polygons=np.array([[(100,height),(680,height),(360,150)]
                              ])
            mask=np.zeros_like(resized1)
            cv2.fillPoly(mask,polygons,255)
            masked_image=cv2.bitwise_and(resized1,mask)
            resized=cv2.resize(masked_image,(720,420))
            
            lines=cv2.HoughLinesP(resized,2,np.pi/180,100,np.array([]),minLineLength=30,maxLineGap=10)
            original_image=np.zeros_like(convert_resize)
            if lines is not None:
                for line in lines:
                    print(line)
                    x1,y1,x2,y2=line.reshape(4)    
                    cv2.line(original_image,(x1,y1),(x2,y2),(255,0,0),8)
   
            two_image=cv2.addWeighted(convert_resize,0.8,original_image,1,1)
            masked=qimage2ndarray.array2qimage(two_image)
            self.masked1=masked #for save image 
            self.label_3.setPixmap(QPixmap(masked))
            self.label_5.setText("Hough Line Combine with Original Image")
    
    def save_converted_image(self):
        img=QtGui.QImage(self.masked1)
        convert=qimage2ndarray.rgb_view(img)
        array2img=qimage2ndarray.array2qimage(convert)
        options = QFileDialog.Options()
        
        if not self.native.isChecked():
            options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File","untitled_","Save Images (*.jpeg *.jpg *.png)",options=options)
        if fileName:
            self.label_1.setPixmap(QPixmap(array2img))
            print("22222")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
