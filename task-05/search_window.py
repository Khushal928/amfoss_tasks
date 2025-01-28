import os
import requests
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap


class DisplayWindow(QWidget):
    def __init__(self, list_of_the_fallen):
        super().__init__()

        self.list_of_the_fallen = list_of_the_fallen  
        self.pointer = 0  

        self.setFixedSize(850, 500)

        backbutton = QPushButton("Back", self)
        backbutton.setGeometry(50, 400, 160, 43)
        backbutton.clicked.connect(self.clickback)

        nextbutton = QPushButton("Next", self)
        nextbutton.setGeometry(640, 400, 160, 43)
        nextbutton.clicked.connect(self.clicknext)

        self.name_of_the_fallen = QLabel(self)
        self.name_of_the_fallen.setGeometry(345, 20, 160, 43)

        self.image_of_the_fallen = QLabel(self)
        self.image_of_the_fallen.setGeometry(225, 80, 400, 300)

        self.update_display()


    def update_display(self):
        if not self.list_of_the_fallen:
            self.name_of_the_fallen.setText("No Pokémon Captured")
            self.image_of_the_fallen.clear()
            return
        
        name = self.list_of_the_fallen[self.pointer]
        self.name_of_the_fallen.setText(name.capitalize())
        image_path = f"captured_pokemon/{name}.png"
        pixmap = QPixmap(image_path)
        self.image_of_the_fallen.setPixmap(pixmap.scaled(200, 200))


    def clickback(self):
        if self.list_of_the_fallen:
            self.pointer = (self.pointer - 1) % len(self.list_of_the_fallen)
            self.update_display()

    def clicknext(self):
        if self.list_of_the_fallen:
            self.pointer = (self.pointer + 1) % len(self.list_of_the_fallen)
            self.update_display()


class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_of_the_fallen = []  # The list where captured Pokémon are stored

        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.getinfo)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_window)

        self.pokemon_name_label = QLabel(self)
        self.pokemon_name_label.setGeometry(450, 20, 300, 30)

        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(400, 70, 200, 200)

        self.pokemon_types_label = QLabel(self)
        self.pokemon_types_label.setGeometry(400, 270, 300, 30)

        self.pokemon_abilities_label_1 = QLabel(self)
        self.pokemon_abilities_label_1.setGeometry(400, 300, 300, 30)

        self.pokemon_abilities_label_2 = QLabel(self)
        self.pokemon_abilities_label_2.setGeometry(400, 330, 300, 30)

        self.pokemon_height_label = QLabel(self)
        self.pokemon_height_label.setGeometry(400, 360, 300, 30)

        self.pokemon_weight_label = QLabel(self)
        self.pokemon_weight_label.setGeometry(400, 390, 300, 30)

    def display_window(self):
        if not self.list_of_the_fallen:
            print("No Pokémon captured yet.")
            return  # Avoid opening the display window if no Pokémon are captured
        
        self.window = DisplayWindow(self.list_of_the_fallen)
        self.window.show()

    def getinfo(self):
        name = self.textbox.text().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data['name']
            self.pokemon_name_label.setText(f"Name: {name}")

            linkofimage = data['sprites']['other']['official-artwork']['front_default']
            image = requests.get(linkofimage).content
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.pokemon_image_label.setPixmap(pixmap.scaled(200, 200))

            abilities = [a['ability']['name'] for a in data['abilities']]
            self.pokemon_abilities_label_1.setText(f"Ability 1: {abilities[0].capitalize()}" if abilities else "Ability 1: N/A")
            self.pokemon_abilities_label_2.setText(f"Ability 2: {abilities[1].capitalize()}" if len(abilities) > 1 else "Ability 2: N/A")

            types = [t['type']['name'] for t in data['types']]
            types_display = ", ".join(types)
            self.pokemon_types_label.setText(f"Types: {types_display}")

            height = data['height'] * 10
            weight = data['weight'] / 10
            self.pokemon_height_label.setText(f"Height: {height} cm")
            self.pokemon_weight_label.setText(f"Weight: {weight} kg")

    def capture(self):
        name = self.textbox.text().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            linkofimage = data['sprites']['other']['official-artwork']['front_default']
            image = requests.get(linkofimage).content

            capture_folder = "captured_pokemon"
            if not os.path.exists(capture_folder):
                os.makedirs(capture_folder)

            filename = f"{capture_folder}/{name}.png"
            with open(filename, "wb") as f:
                f.write(image)

            self.list_of_the_fallen.append(name)  # Add captured Pokémon to the list
            print(f"Image of {name} captured and saved as {filename}")


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())

