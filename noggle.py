import sys
import settings
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

homepage = 'https://noggle-tech.github.io/noggle/browser/welcome.html'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = None
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(homepage))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # NAVIGATION BAR
        navbar = QToolBar()
        self.addToolBar(navbar)

        backbtn = QAction('<--', self)
        backbtn.setToolTip('<em>Back</em>')
        backbtn.triggered.connect(self.browser.back)
        navbar.addAction(backbtn)
        fwdbtn = QAction('-->', self)
        fwdbtn.setToolTip('<em>Forward</em>')
        fwdbtn.triggered.connect(self.browser.forward)
        navbar.addAction(fwdbtn)
        rwdbtn = QAction('🔄', self)
        rwdbtn.setToolTip('<em>Reload</em>')
        rwdbtn.triggered.connect(self.browser.reload)
        navbar.addAction(rwdbtn)
        hombtn = QAction('🏠', self)
        hombtn.setToolTip('<em>Home</em>')
        hombtn.triggered.connect(self.navigatehome)
        navbar.addAction(hombtn)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigatetourl)
        navbar.addWidget(self.urlbar)

        stnbtn = QAction('⚙️', self)
        stnbtn.setToolTip('<em>Settings and About</em>')
        stnbtn.triggered.connect(self.opensettings)
        navbar.addAction(stnbtn)

        self.browser.urlChanged.connect(self.updateurl)

    def navigatehome(self):
        self.browser.setUrl(QUrl(homepage))
    
    def navigatetourl(self):
        url = self.urlbar.text()
        self.browser.setUrl(QUrl(url))
    
    def updateurl(self, url):
        self.urlbar.setText(url.toString())
    
    def opensettings(self, checked):
        if self.w is None:
            self.w = settings.SettingsWindow()
            self.w.show()

        else:
            self.w.close()
            self.w = None

app = QApplication(sys.argv)
QApplication.setApplicationName("Noggle Browser")
window = MainWindow()
app.exec_()