from PySide2.QtWidgets import QWidget, QGridLayout, QLabel

class Settings:
    def __init__(self, Settings):
        self.Settings = Settings
        
        # call method components
        self.SettingsComponents()

    def SettingsComponents(self):
        settingsLayout = QGridLayout()
        self.Settings.setLayout(settingsLayout)
        settingsLayout.addWidget(QLabel("Settings"))