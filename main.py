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
        checkboxes = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
            self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,
            self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
            self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16
        ]
        for checkbox in checkboxes:
            checkbox.stateChanged.connect(self.update_table)

        # Táblázat inicializálása
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Tétel", "Ár"])
        self.tableWidget.setColumnWidth(0, 300)  # Tétel oszlop szélessége
        self.tableWidget.setColumnWidth(1, 90)  # Ár oszlop szélessége

        self.row_count = 0
        self.total_price = 0

        self.show()

    def calculate_price(self):
        crust = self.comboBox.currentText()
        sauce = self.comboBox_2.currentText()

        crust_price = 0
        sauce_price = 0

        if crust == "Vékony tészta":
            crust_price = 100
        elif crust == "Vastag tészta":
            crust_price = 200
        elif crust == "Sajt szélű tészta":
            crust_price = 300

        if sauce == "Paradicsomos alap":
            sauce_price = 100
        elif sauce == "Tejszínes alap":
            sauce_price = 100

        self.update_total_price(crust_price + sauce_price)

    def update_table(self):
        checkbox = self.sender()
        item_name = checkbox.text().split(" ")[0]  # Első szó a termék neve
        item_price = int(checkbox.text().split(" ")[-2].strip(",.-"))  # Ár kinyerése

        if checkbox.isChecked():
            # Ellenőrizzük, hogy az elem már szerepel-e a táblázatban
            exists = False
            for row in range(self.tableWidget.rowCount()):
                name_item = self.tableWidget.item(row, 0)
                if name_item and name_item.text() == item_name:
                    exists = True
                    price_item = self.tableWidget.item(row, 1)
                    if price_item:
                        prev_price = int(price_item.text())
                        self.total_price += item_price - prev_price
                        price_item.setText(str(item_price))
                    break

            # Ha az elem még nem szerepel a táblázatban, adjunk hozzá egy új sort
            if not exists:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(item_name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(item_price)))
                self.row_count += 1
                self.total_price += item_price

        else:
            # Ellenőrizzük, hogy az elem szerepel-e a táblázatban, és töröljük
            for row in range(self.tableWidget.rowCount()):
                name_item = self.tableWidget.item(row, 0)
                if name_item and name_item.text() == item_name:
                    price_item = self.tableWidget.item(row, 1)
                    if price_item:
                        prev_price = int(price_item.text())
                        self.total_price -= prev_price
                    self.tableWidget.removeRow(row)
                    self.row_count -= 1
                    break

        self.label_total_price.setText(f"Összesen:     {self.total_price} Ft")

    def update_total_price(self, price):
        self.total_price = price
        for row in range(self.tableWidget.rowCount()):
            price_item = self.tableWidget.item(row, 1)
            if price_item:
                item_price = int(price_item.text())
                self.total_price += item_price

        self.label_total_price.setText(f"Összesen: {self.total_price} Ft")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PizzaApp()
    sys.exit(app.exec())
