from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  currency = soup.find("span", class_="ccOutputRslt").get_text()
  get_value= float(currency.split(" ")[0])
  return get_value


def show_currency():
    #this takes the input widget text
    input_text = float(text.text())
    rate = get_currency("USD", "EUR")
    output = round(input_text * rate, 3)
    output_label.setText(str(output))

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
btn = QPushButton("Convert")
layout.addWidget(btn) #add button to the layout
#clicked is the signal (the signal could be clicked or checked etc.)
#when the button is clicked inside the parenteses (slot) will be triggered
#thw slot is function we need to creaate
btn.clicked.connect(show_currency)

#create the output that make_sentence function gives
output_label = QLabel('')
layout.addWidget(output_label)


#connect the layout to the window
window.setLayout(layout)

#to see the application
window.show()
app.exec()
