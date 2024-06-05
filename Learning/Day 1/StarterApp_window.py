# PyQt - pip3 install pyqt5
# Pillow - pip3 install pillow
# matplotlib - pip3 install matplotlib

# Import necessary modules from PyQt5 and other libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from random import choice

# Initialize the main application object
app = QApplication([])

# Create the main window and set its title and size
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(300, 200)

# Create QLabel widgets to display text
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

# List of words to choose from
my_words = ["Hello", "GoodBye", "Test", "Python", "Surbhi"]

# Function to display a random word in text1
def display_word1():
    word = choice(my_words)
    text1.setText(word)

# Function to display a random word in text2
def display_word2():
    word = choice(my_words)
    text2.setText(word)

# Function to display a random word in text3
def display_word3():
    word = choice(my_words)
    text3.setText(word)

# Create a QLabel widget for the title text
title_text = QLabel("Random Keywords")

# Create QPushButton widgets for user interaction
button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

# Set up the layout structure for the main window
master_Layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Add widgets to the layout
row1.addWidget(title_text, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

# Add the rows to the main layout
master_Layout.addLayout(row1)
master_Layout.addLayout(row2)
master_Layout.addLayout(row3)

# Set the layout for the main window
main_window.setLayout(master_Layout)

# Button is clicked to connect with corresponding functions
button1.clicked.connect(display_word1)
button2.clicked.connect(display_word2)
button3.clicked.connect(display_word3)

# Show the main window and run the application event loop
main_window.show()
app.exec_()
