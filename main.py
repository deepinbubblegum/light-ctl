from pathlib import Path
import sys
import signal

# disable __pycache__ folder
sys.dont_write_bytecode = True

from PySide2 import QtGui, QtWidgets
from handlers.KeyboardHandle import handleVisibleChanged
from interfaces.MainWindow import MainWindow

def main():
    # fix ctrl+c not working
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    # init Qt Application 
    application = QtWidgets.QApplication(sys.argv)
    application.setStyleSheet(Path('style.qss').read_text())
    
    # This is the line that makes the keyboard work
    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)

    # create main window
    window = MainWindow()
    
    # start Qt Application
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()