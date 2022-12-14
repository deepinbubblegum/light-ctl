from PySide2.QtWidgets import QGridLayout, QLabel

class General:
    def __init__(self, General):
        self.General = General
        
        # call method components
        self.GeneralComponents()

    def GeneralComponents(self):
        generalLayout = QGridLayout()
        self.General.setLayout(generalLayout)
        generalLayout.addWidget(QLabel("General"))