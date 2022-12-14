import sys
from PyQt5.QtWidgets import *

class Template(QWidget):

    def __init__(self):
        super().__init__()
        tab = QTabWidget()
        tab.addTab(QWidget(), 'TAB 1')
        tab.addTab(QWidget(), 'TAB 2')
        tab.addTab(QWidget(), 'TAB 3')
        grid = QGridLayout(self)
        grid.addWidget(tab)
        self.setStyleSheet('''
        QTabWidget::tab-bar {
            alignment: center;
        }''')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Template()
    window.show()
    sys.exit(app.exec_())