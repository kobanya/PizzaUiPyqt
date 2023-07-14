import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi


class PizzaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pizza.ui", self)  # .ui fájl betöltése

        # Gombokhoz csatlakoztatott eseménykezelők
        self.comboBox.currentIndexChanged.connect(self.calculate_price)
        self.comboBox_2.currentIndexChanged.connect(self.calculate_price)

        # CheckBox-okhoz csatlakoztatott eseménykezelők
        self.checkBox.stateChanged.connect(self.update_table)
        self.checkBox_2.stateChanged.connect(self.update_table)
        self.checkBox_3.stateChanged.connect(self.update_table)
        self.checkBox_4.stateChanged.connect(self.update_table)
        self.checkBox_5.stateChanged.connect(self.update_table)
        self.checkBox_6.stateChanged.connect(self.update_table)
        self.checkBox_7.stateChanged.connect(self.update_table)
        self.checkBox_8.stateChanged.connect(self.update_table)
        self.checkBox_9.stateChanged.connect(self.update_table)
        self.checkBox_10.stateChanged.connect(self.update_table)
        self.checkBox_11.stateChanged.connect(self.update_table)
        self.checkBox_12.stateChanged.connect(self.update_table)
        # Táblázat inicializálása
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Tétel", "Ár"])

        self.row_count = 0

        self.show()

    def update_table(self):
        checkbox = self.sender()
        item_name = checkbox.text()
        item_price = 0

        if checkbox.isChecked():
            if item_name == "Kolbász":
                item_price = 350
            elif item_name == "Sonka":
                item_price = 350
            elif item_name == "Szalámi":
                item_price = 350
            elif item_name == "Tojás":
                item_price = 250
            elif item_name == "Articsóka":
                item_price = 250
            elif item_name == "Gomba":
                item_price = 250
            elif item_name == "Sajt":
                item_price = 250
            elif item_name == "Olajbogyó":
                item_price = 250
            elif item_name == "Paprika":
                item_price = 250

            self.tableWidget.insertRow(self.row_count)
            self.tableWidget.setItem(self.row_count, 0, QTableWidgetItem(item_name))
            self.tableWidget.setItem(self.row_count, 1, QTableWidgetItem(str(item_price)))
            self.row_count += 1
        else:
            for row in range(self.tableWidget.rowCount()):
                name_item = self.tableWidget.item(row, 0)
                if name_item.text() == item_name:
                    self.tableWidget.removeRow(row)
                    self.row_count -= 1

    def calculate_price(self):
        crust = self.comboBox.currentText()
        sauce = self.comboBox_2.currentText()

        price = 0

        if crust == "Vékony tészta":
            price += 100
        elif crust == "Vastag tészta":
            price += 200
        elif crust == "Sajt szélű tészta":
            price += 300

        if sauce == "Paradicsomos alap":
            price += 50
        elif sauce == "Tejszínes alap":
            price += 100

        self.label_price.setText(f"Ár: {price} Ft")
        self.price = price


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PizzaApp()
    sys.exit(app.exec())
