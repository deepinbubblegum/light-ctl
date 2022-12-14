from PySide2.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLabel
from interfaces.pages.General import General
from interfaces.pages.Settings import Settings

class UiPageTabs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        # self.tabs.setTabPosition(QTabWidget.South)
        self.tabs.setUsesScrollButtons(False)
        
        # create tabs
        self.General = QWidget()
        self.Settings = QWidget()
        
        # add tabs
        self.tabs.addTab(self.General, "GENERAL")
        self.tabs.addTab(self.Settings, "SETTINGS")

        self.tabWidth = int(self.geometry().width()) - 12
        self.tabs.setStyleSheet("QTabBar::tab { width: " + str(self.tabWidth) + "px; min-height: 8ex;}")
        
        # load pages
        General(self.General)
        Settings(self.Settings)
        
        # add tabs to layout
        self.layout.addWidget(self.tabs)