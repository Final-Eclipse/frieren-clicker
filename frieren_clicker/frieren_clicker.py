from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont
from random import choice

"""
Every time you press the button, the number increases, and we'll also have a reset button. 
This uses signals (clicked) and slots (custom functions).
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Frieren Clicker")
        self.setMinimumSize(QSize(600, 400))

        # Frieren button
        self.button_size = QSize(1080, 750)
        self.button = QPushButton()
        self.button.setFixedSize(self.button_size)
        self.frieren_pictures = ["frieren_clicker/Frieren Looking Up.jpg", "frieren_clicker/Underwater Frieren.jpg", 
                                 "frieren_clicker/Streetwear Frieren.png", "frieren_clicker/Bratty Frieren.jpg",
                                 "frieren_clicker/Smug Frieren.jpg", "frieren_clicker/Double Smug Frieren.jpg"]
        
        # Attempts to store the next picture in memory to prevent stuttering 
        # that can sometimes occur when loading the next image when clicked
        self.current_frieren = choice(self.frieren_pictures)
        self.next_frieren = choice(self.frieren_pictures)
        while self.current_frieren == self.next_frieren:
            self.next_frieren = choice(self.frieren_pictures)
            
        self.button.setIcon(QIcon(self.current_frieren))
        self.button.setIconSize(self.button_size)
        self.button.clicked.connect(self.frieren_clicked)
        self.button.clicked.connect(self.change_frieren)

        # Label for number of Frierens
        self.clicks = 0
        self.click_counter_label = QLabel()
        self.click_counter_label.setText(f"{self.clicks} Frierens")
        self.font_size = QFont()
        self.font_size.setPointSize(20)
        self.click_counter_label.setFont(self.font_size)

        # Takina (reset) button
        self.reset_button_size = QSize(300, 300)
        self.reset_button = QPushButton()
        self.reset_button.setFixedSize(self.reset_button_size)
        self.takina_pictures = ["frieren_clicker/Angry Takina.jpg", "frieren_clicker/Horror-Struck Takina.jpg", 
                                "frieren_clicker/Embarrassed Takina.jpg", "frieren_clicker/Smiling Takina.jpg",
                                "frieren_clicker/Chibi Sakana.jpg", "frieren_clicker/Sakana in Fish Tank.jpg",
                                "frieren_clicker/Sakana.jpg", "frieren_clicker/Matching Icons Takina Sakana.jpg"]
        
        # Attempts to store the next picture in memory to prevent stuttering 
        # that can sometimes occur when loading the next image when clicked
        self.current_takina = choice(self.takina_pictures)
        self.next_takina = choice(self.takina_pictures)
        while self.current_takina == self.next_takina:
            self.next_takina = choice(self.takina_pictures)

        self.reset_button.setIcon(QIcon(self.current_takina))
        self.reset_button.setIconSize(self.reset_button_size)
        self.reset_button.clicked.connect(self.takina_clicked)
        self.reset_button.clicked.connect(self.change_takina)
        
        # Layout
        self.window_layout = QVBoxLayout()
        self.window_layout.addWidget(self.button)
        self.window_layout.addWidget(self.reset_button)
        self.window_layout.addWidget(self.click_counter_label)
        self.container = QWidget()
        self.container.setLayout(self.window_layout)
        self.setCentralWidget(self.container)

    def frieren_clicked(self):
        self.clicks += 1
        self.click_counter_label.setText(f"{self.clicks} Frierens")

    def takina_clicked(self):
        self.clicks = 0
        self.click_counter_label.setText(f"{self.clicks} Frierens")

    def change_frieren(self):
        # Attempts to store the next picture in memory to prevent stuttering 
        # that can sometimes occur when loading the next image when clicked
        self.current_frieren = self.next_frieren
        self.button.setIcon(QIcon(self.current_frieren))

        icon = choice(self.frieren_pictures)
        while icon == self.current_frieren:
            icon = choice(self.frieren_pictures)
        self.next_frieren = icon
    
    def change_takina(self):
        # Attempts to store the next picture in memory to prevent stuttering 
        # that can sometimes occur when loading the next image when clicked
        self.current_takina = self.next_takina
        self.reset_button.setIcon(QIcon(self.current_takina))

        icon = choice(self.takina_pictures)
        while icon == self.current_takina:
            icon = choice(self.takina_pictures)
        self.next_takina = icon
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
