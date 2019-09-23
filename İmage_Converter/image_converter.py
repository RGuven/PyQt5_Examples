# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QProgressBar
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("dog.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 0, 300, 300))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 80, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 120, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 0, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 200, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 160, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 240, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Converted_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Converted_Image.setObjectName("actionSave_Converted_Image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Converted_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        
        

        self.actionOpen.triggered.connect(self.file_open)
        self.pushButton_4.clicked.connect(self.img2gray)
        self.pushButton.clicked.connect(self.img2blur)
        
        self.actionExit.triggered.connect(self.close_application) #for close application
        self.actionExit.setShortcut("q")
        self.pushButton_2.clicked.connect(self.img2hsv)
        self.pushButton_3.clicked.connect(self.convert_90)
        self.pushButton_6.clicked.connect(self.img2laplacian)
        self.pushButton_5.clicked.connect(self.sobel_x)
        self.pushButton_7.clicked.connect(self.sobel_y)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def file_open(self):
    
        print("opening")
        
        #imagePath = name[0]
        #pixmap = QPixmap(imagePath)
        #self.label_2.setPixmap(QtGui.QPixmap(pixmap))
        #img=cv2.imread(name)
        #self.label_2.setPixmap(QtGui.QPixmap(img))
    
    def img2gray(self):
        img=cv2.imread("dog.jpg")
        #images = 0.299*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
        images=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgS=cv2.resize(img,(300,300))
        imagesS=cv2.resize(images,(300,300))
        cv2.imshow("Resim",imgS)
        cv2.imshow("Gri Resim",imagesS)
        cv2.moveWindow("Resim",0,0)
        cv2.moveWindow("Gri Resim",303,0)
        
        
        if cv2.waitKey(0) & 0xFF==ord("q"):
            cv2.destroyAllWindows()
         
    def img2blur(self):
        img=cv2.imread("dog.jpg")
        self.label_2.setPixmap(QtGui.QPixmap("gaussian.png"))
        imgS=cv2.resize(img,(300,300))
        dst = cv2.GaussianBlur(imgS,(7,7),cv2.BORDER_DEFAULT)
        dst1=cv2.resize(dst,(300,300))
        #plt.hist(img.ravel(),256,[0,256])
        #plt.show()
        cv2.imshow("Gaussian Blur",dst1)
        cv2.moveWindow("Gaussian Blur",606,0)
        cv2.waitKey(0)
    



    def img2hsv(self):
        img=cv2.imread("dog.jpg")
        self.label_2.setPixmap(QtGui.QPixmap("hsv_color.jpg"))
        images=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        imagesS=cv2.resize(images,(300,300))
        cv2.imshow("HSV Format",imagesS)
        cv2.moveWindow("HSV Format",909,0)
        cv2.waitKey(0)
    
    def convert_90(self):
        img=cv2.imread("dog.jpg")
        #images=cv2.rotate(img,rotateCode=ROTATE_90)
        #images = np.rot90(img)
        #imagesS=cv2.resize(images,(300,300))
        #cv2.imshow("ROTATE 90 DEGREE",imagesS)
        #cv2.moveWindow("ROTATE 90 DEGREE",909,0)
        #cv2.waitKey(0)
        
        # get image height, width
        (h, w) = img.shape[:2]
        # calculate the center of the image
        center = (w / 2, h / 2)
        angle_90 = 90
        M = cv2.getRotationMatrix2D(center, angle_90, 1.0)
        rotated90 = cv2.warpAffine(img, M, (h, w))
        imagesS=cv2.resize(rotated90,(300,300))
        cv2.imshow("ROTATE 90 DEGREE",imagesS)
        cv2.moveWindow("ROTATE 90 DEGREE",1212,0)
        cv2.waitKey(0)   


    def img2laplacian(self):
        img=cv2.imread("dog.jpg",0)
        self.label_2.setPixmap(QtGui.QPixmap("Laplacian_Formul.png"))
        laplacian = cv2.Laplacian(img,cv2.CV_64FC4)
        laplacianS=cv2.resize(laplacian,(300,300))
        cv2.imshow("Laplacian",laplacianS)
        cv2.moveWindow("Laplacian",1515,0)
        cv2.waitKey(0)
        
    
    def sobel_x(self):
        img=cv2.imread("dog.jpg",0)
        self.label_2.setPixmap(QtGui.QPixmap("sobel.png"))
        sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        sobelx=cv2.resize(sobel_x,(300,300))
        cv2.imshow("Sobel X",sobelx)
        cv2.moveWindow("Sobel X",1515,350)
        cv2.waitKey(0)

    def sobel_y(self):
        img=cv2.imread("dog.jpg",0)
        self.label_2.setPixmap(QtGui.QPixmap("sobel.png"))
        sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        sobely=cv2.resize(sobel_y,(300,300))
        cv2.imshow("Sobel Y",sobely)
        cv2.moveWindow("Sobel Y",1515,700)
        cv2.waitKey(0)




    #TO DO close_application !!!!!!!!!!!
    def close_application(self):
        choice=QMessageBox.question(self,'Message',
        "Cikmak Istediğinizden Emin Misiniz",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Uygulamadan Çıkıyorsunuz....")
            sys.exit()
        else:
            pass
        


    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Gaussian Blur"))
        self.label_2.setText(_translate("MainWindow", "Converted Image"))
        self.pushButton_2.setText(_translate("MainWindow", "HSV"))
        self.pushButton_3.setText(_translate("MainWindow", "Rotation Convert( 90° )"))
        self.pushButton_4.setText(_translate("MainWindow", "Gray"))
        self.pushButton_5.setText(_translate("MainWindow", "Sobel X"))
        self.pushButton_6.setText(_translate("MainWindow", "Laplacian"))
        self.pushButton_7.setText(_translate("MainWindow", "Sobel Y"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_Converted_Image.setText(_translate("MainWindow", "Save Converted Image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
