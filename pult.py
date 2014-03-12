# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pult.ui'
#
# Created: Sun Feb 16 11:31:45 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import subprocess
import sys
import socket
import time


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
      
#HOST= "10.65.9.213"
class Pult(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(Pult, self).__init__(parent)
        self.prevCmd = ''
        self.counter = 0
        self.muted = False
        self.conns = []
        self.setWindowTitle(u"Pult Remote")
        self.ui = Ui_Pult()
        self.ui.setupUi(self)
        gry = self.geometry()
        gry.moveCenter(QtCore.QCoreApplication.instance().desktop().availableGeometry().center())
        self.setGeometry(gry)
        QtCore.QObject.connect(self.ui.connect,QtCore.SIGNAL(u"clicked()"), self.Connect)
        QtCore.QObject.connect(self.ui.update,QtCore.SIGNAL(u"clicked()"), self.Update)
        QtCore.QObject.connect(self.ui.play,QtCore.SIGNAL(u"clicked()"), self.sendPause)
        QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL(u"clicked()"), self.sendStop)
        QtCore.QObject.connect(self.ui.up,QtCore.SIGNAL(u"clicked()"), self.sendUp)
        QtCore.QObject.connect(self.ui.down,QtCore.SIGNAL(u"clicked()"), self.sendDown)
        QtCore.QObject.connect(self.ui.left,QtCore.SIGNAL(u"clicked()"), self.sendLeft)
        QtCore.QObject.connect(self.ui.right,QtCore.SIGNAL(u"clicked()"), self.sendRight)
        QtCore.QObject.connect(self.ui.ok,QtCore.SIGNAL(u"clicked()"), self.sendOk)
        QtCore.QObject.connect(self.ui.home,QtCore.SIGNAL(u"clicked()"), self.sendHome)
        QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL(u"clicked()"), self.sendBack)
        QtCore.QObject.connect(self.ui.chup,QtCore.SIGNAL(u"clicked()"), self.sendChup)
        QtCore.QObject.connect(self.ui.chdw,QtCore.SIGNAL(u"clicked()"), self.sendChdw)
        QtCore.QObject.connect(self.ui.one,QtCore.SIGNAL(u"clicked()"), self.sendOne)
        QtCore.QObject.connect(self.ui.three,QtCore.SIGNAL(u"clicked()"), self.sendThree)
        QtCore.QObject.connect(self.ui.four,QtCore.SIGNAL(u"clicked()"), self.sendFour)
        QtCore.QObject.connect(self.ui.five,QtCore.SIGNAL(u"clicked()"), self.sendFive)
        QtCore.QObject.connect(self.ui.six,QtCore.SIGNAL(u"clicked()"), self.sendSix)
        QtCore.QObject.connect(self.ui.seven,QtCore.SIGNAL(u"clicked()"), self.sendSeven)
        QtCore.QObject.connect(self.ui.eight,QtCore.SIGNAL(u"clicked()"), self.sendEight)
        QtCore.QObject.connect(self.ui.nine,QtCore.SIGNAL(u"clicked()"), self.sendNine)
        QtCore.QObject.connect(self.ui.zero,QtCore.SIGNAL(u"clicked()"), self.sendZero)

      
        
        
        
        # TextEdit Create
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(30, 10, 161, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
	self.textEdit.append(_fromUtf8("10.65.9.213"))


	# Image
	self.screen = QtGui.QLabel(self)
        self.screen.setGeometry(QtCore.QRect(10, 50, 900, 504))
        self.screen.setObjectName(_fromUtf8("screen"))
        self.screen.setScaledContents(True)
        self.show()
   
    def Connect(self):
        global HOST
        HOST = self.textEdit.toPlainText()
        self.Update()
        #print(HOST)

   
    def Update(self):
	#subprocess.call("nc "+str(HOST)+" 1234 > s.png", shell=True)
	#subprocess.call("expect \"screenshot\"",shell=True)
	#filename= "./s.png"
	#image = QtGui.QImage(filename)
	#pp = QtGui.QPixmap.fromImage(image)
	#lbl = QtGui.QLabel(self.screen)
        #lbl.setPixmap(pp)
        #lbl.show()
        sock = socket.socket()
	sock.connect((str(HOST), 1234))
	sock.send('screenshot\n')
	data = b""
	tmp = sock.recv(1024)
	while tmp: 
	  data += tmp
	  tmp = sock.recv(1024)
	sock.close()
	f = open("s.png", "w")
	f.write(data)
	f.close()  
	self.screen.setPixmap(QtGui.QPixmap(_fromUtf8("s.png")))
	self.screen.setScaledContents(True)
	
    def SendS(self,cmd):
	ock = socket.socket()
	ock.connect((str(HOST), 1234))
	ock.send(cmd+"\n")
	ock.close()
	#time.sleep(1)
	#self.Update()
        
        
    def sendPause(self):
       self.SendS("key pause")
       QtCore.QObject.connect(self.ui.play,QtCore.SIGNAL(u"clicked()"), self.sendPlay)
    def sendPlay(self):
	self.SendS("key play")
	QtCore.QObject.connect(self.ui.play,QtCore.SIGNAL(u"clicked()"), self.sendPause)
    def sendStop(self):
        self.SendS("key stop")
    def sendUp(self):
        self.SendS("key up")
    def sendDown(self):
        self.SendS("key down")
    def sendLeft(self):
        self.SendS("key left")
    def sendRight(self):
        self.SendS("key right")
    def sendOk(self):
        self.SendS("key ok")
    def sendHome(self):
      self.SendS("key home")
    def sendBack(self):
      self.SendS("key back")
    def sendChup(self):
      self.SendS("key ChannelNext")
    def sendChdw(self):
      self.SendS("key ChannelPrev")
    def sendOne(self):
      self.SendS("key 1")
    def sendTwo(self):
      self.SendS("key 2")
    def sendThree(self):
      self.SendS("key 3")
    def sendFour(self):
      self.SendS("key 4")
    def sendFive(self):
      self.SendS("key 5")
    def sendSix(self):
      self.SendS("key 6")
    def sendSeven(self):
      self.SendS("key 7")
    def sendEight(self):
      self.SendS("key 8")
    def sendNine(self):
      self.SendS("key 9")
    def sendZero(self):
      self.SendS("key 0")

      
      
class Ui_Pult(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1092, 580)
        self.up = QtGui.QPushButton(Dialog)
        self.up.setGeometry(QtCore.QRect(980, 230, 41, 41))
        self.up.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-up"))
        self.up.setIcon(icon)
        self.up.setObjectName(_fromUtf8("up"))
        self.right = QtGui.QPushButton(Dialog)
        self.right.setGeometry(QtCore.QRect(1020, 270, 41, 41))
        self.right.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-right"))
        self.right.setIcon(icon)
        self.right.setObjectName(_fromUtf8("right"))
        self.down = QtGui.QPushButton(Dialog)
        self.down.setGeometry(QtCore.QRect(980, 310, 41, 41))
        self.down.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-down"))
        self.down.setIcon(icon)
        self.down.setObjectName(_fromUtf8("down"))
        self.left = QtGui.QPushButton(Dialog)
        self.left.setGeometry(QtCore.QRect(940, 270, 41, 41))
        self.left.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("arrow-left"))
        self.left.setIcon(icon)
        self.left.setObjectName(_fromUtf8("left"))
        self.ok = QtGui.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(980, 270, 41, 41))
        self.ok.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("user-online"))
        self.ok.setIcon(icon)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.home = QtGui.QPushButton(Dialog)
        self.home.setGeometry(QtCore.QRect(940, 230, 41, 41))
        self.home.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-home"))
        self.home.setIcon(icon)
        self.home.setObjectName(_fromUtf8("home"))
        self.menu = QtGui.QPushButton(Dialog)
        self.menu.setGeometry(QtCore.QRect(1020, 230, 41, 41))
        self.menu.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("show-menu"))
        self.menu.setIcon(icon)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.next = QtGui.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(1040, 30, 41, 41))
        self.next.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-seek-forward"))
        self.next.setIcon(icon)
        self.next.setObjectName(_fromUtf8("next"))
        self.stop = QtGui.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(960, 30, 41, 41))
        self.stop.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-stop"))
        self.stop.setIcon(icon)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.play = QtGui.QPushButton(Dialog)
        self.play.setGeometry(QtCore.QRect(1000, 30, 41, 41))
        self.play.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-start"))
        self.play.setIcon(icon)
        self.play.setObjectName(_fromUtf8("play"))
        self.back = QtGui.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(920, 30, 41, 41))
        self.back.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-seek-backward"))
        self.back.setIcon(icon)
        self.back.setObjectName(_fromUtf8("back"))
        self.nine = QtGui.QPushButton(Dialog)
        self.nine.setGeometry(QtCore.QRect(1020, 150, 41, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nine.setIcon(icon)
        self.nine.setObjectName(_fromUtf8("nine"))
        self.seven = QtGui.QPushButton(Dialog)
        self.seven.setGeometry(QtCore.QRect(940, 150, 41, 41))
        self.seven.setIcon(icon)
        self.seven.setObjectName(_fromUtf8("seven"))
        self.eight = QtGui.QPushButton(Dialog)
        self.eight.setGeometry(QtCore.QRect(980, 150, 41, 41))
        self.eight.setIcon(icon)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.six = QtGui.QPushButton(Dialog)
        self.six.setGeometry(QtCore.QRect(1020, 110, 41, 41))
        self.six.setIcon(icon)
        self.six.setObjectName(_fromUtf8("six"))
        self.five = QtGui.QPushButton(Dialog)
        self.five.setGeometry(QtCore.QRect(980, 110, 41, 41))
        self.five.setIcon(icon)
        self.five.setObjectName(_fromUtf8("five"))
        self.four = QtGui.QPushButton(Dialog)
        self.four.setGeometry(QtCore.QRect(940, 110, 41, 41))
        self.four.setIcon(icon)
        self.four.setObjectName(_fromUtf8("four"))
        self.three = QtGui.QPushButton(Dialog)
        self.three.setGeometry(QtCore.QRect(1020, 70, 41, 41))
        self.three.setIcon(icon)
        self.three.setObjectName(_fromUtf8("three"))
        self.two = QtGui.QPushButton(Dialog)
        self.two.setGeometry(QtCore.QRect(980, 70, 41, 41))
        self.two.setIcon(icon)
        self.two.setObjectName(_fromUtf8("two"))
        self.one = QtGui.QPushButton(Dialog)
        self.one.setGeometry(QtCore.QRect(940, 70, 41, 41))
        self.one.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.one.setIcon(icon)
        self.one.setObjectName(_fromUtf8("one"))
        self.zero = QtGui.QPushButton(Dialog)
        self.zero.setGeometry(QtCore.QRect(980, 190, 41, 41))
        self.zero.setIcon(icon)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.volup = QtGui.QPushButton(Dialog)
        self.volup.setGeometry(QtCore.QRect(940, 330, 41, 41))
        self.volup.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("audio-volume-high"))
        self.volup.setIcon(icon)
        self.volup.setObjectName(_fromUtf8("volup"))
        self.voldown = QtGui.QPushButton(Dialog)
        self.voldown.setGeometry(QtCore.QRect(940, 370, 41, 41))
        self.voldown.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("audio-volume-low"))
        self.voldown.setIcon(icon)
        self.voldown.setObjectName(_fromUtf8("voldown"))
        self.chup = QtGui.QPushButton(Dialog)
        self.chup.setGeometry(QtCore.QRect(1020, 330, 41, 41))
        self.chup.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-up"))
        self.chup.setIcon(icon)
        self.chup.setObjectName(_fromUtf8("chup"))
        self.chdw = QtGui.QPushButton(Dialog)
        self.chdw.setGeometry(QtCore.QRect(1020, 370, 41, 41))
        self.chdw.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-down"))
        self.chdw.setIcon(icon)
        self.chdw.setObjectName(_fromUtf8("chdw"))
        self.connect = QtGui.QPushButton(Dialog)
        self.connect.setGeometry(QtCore.QRect(200, 10, 40, 31))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("network-connect"))
        self.connect.setIcon(icon)
        self.connect.setObjectName(_fromUtf8("connect"))
        self.update = QtGui.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(250, 10, 40, 31))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("view-refresh"))
        self.update.setIcon(icon)
        self.update.setObjectName(_fromUtf8("update"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.nine.setText(_translate("Dialog", "9", None))
        self.seven.setText(_translate("Dialog", "7", None))
        self.eight.setText(_translate("Dialog", "8", None))
        self.six.setText(_translate("Dialog", "6", None))
        self.five.setText(_translate("Dialog", "5", None))
        self.four.setText(_translate("Dialog", "4", None))
        self.three.setText(_translate("Dialog", "3", None))
        self.two.setText(_translate("Dialog", "2", None))
        self.one.setText(_translate("Dialog", "1", None))
        self.zero.setText(_translate("Dialog", "0", None))
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(["Pult Remote"])
    app.setStyle(u"Cleanlooks")
    wem = Pult()
    res = app.exec_()
    sys.exit(res)

