from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

def make_sentence():
    #this takes the input widget text
    input_text = text.text()
    output_label.setText(input_text.capitalize() + '.')

#CRETAE THE APPLICATION INSTANCE
app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')

#Create a vertical Layout V symbol before Q represent the vertical
layout = QVBoxLayout()

#input text
text = QLineEdit()
layout.addWidget(text) #add text to the layout

#add button
btn = QPushButton("Make Sentence")
layout.addWidget(btn) #add button to the layout
#clicked is the signal (the signal could be clicked or checked etc.)
#when the button is clicked inside the parenteses (slot) will be triggered
#thw slot is function we need to creaate
btn.clicked.connect(make_sentence)

#create the output that make_sentence function gives
output_label = QLabel('')
layout.addWidget(output_label)


#connect the layout to the window
window.setLayout(layout)

#to see the application
window.show()
app.exec()
