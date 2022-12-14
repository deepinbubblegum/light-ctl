from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from interfaces.UiPageTabs import UiPageTabs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # setting title
        self.setWindowTitle("Light Controls")
        
        # setting geometry
        self.setGeometry(0, 0, 1280, 800)
        
        # # call method components
        self.UiComponents()
        # setting show ui on screen
        # self.show()
        
        # self.showMaximized()
        self.showFullScreen()
        
    def UiComponents(self):
        self.pageTabs = UiPageTabs()
        self.setCentralWidget(self.pageTabs)
