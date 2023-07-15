import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QRadioButton
from PyQt6.uic import loadUi


class PizzaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pizza.ui", self)  # .ui fájl betöltése

        # Gombokhoz csatlakoztatott eseménykezelők
        self.comboBox.currentIndexChanged.connect(self.update_table)
        self.comboBox_2.currentIndexChanged.connect(self.update_table)

        # CheckBox-okhoz csatlakoztatott eseménykezelők
        checkboxes = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
            self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,
            self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
            self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16
        ]
        for checkbox in checkboxes:
            checkbox.stateChanged.connect(self.update_table)

        # Radio button-hoz csatlakoztatott eseménykezelő
        self.radioButton_Helyben.toggled.connect(self.update_table)
        self.radioButton_hazhozszallitas.toggled.connect(self.update_table)

        # Táblázat inicializálása
        self.tableWidget.setColumnCount(2)  # Oszlopok száma
        self.tableWidget.setHorizontalHeaderLabels(["Tétel", "Ár"])
        self.tableWidget.setColumnWidth(0, 300)  # Tétel oszlop szélessége
        self.tableWidget.setColumnWidth(1, 90)  # Ár oszlop szélessége

        # Frame_hazhozszallitas kezdeti állapotának beállítása
        self.frame_hazhozszallitas.setVisible(False)

        self.show()

    def update_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        crust = self.comboBox.currentText()
        sauce = self.comboBox_2.currentText()

        crust_price = 900
        sauce_price = 0

        if crust == "Vékony tészta":
            crust_price += 100
        elif crust == "Vastag tészta":
            crust_price += 200
        elif crust == "Sajt szélű tészta":
            crust_price += 300

        if sauce == "Paradicsomos alap":
            sauce_price += 100
        elif sauce == "Tejszínes alap":
            sauce_price += 100

        self.add_item_to_table(crust, crust_price)
        self.add_item_to_table(sauce, sauce_price)

        checkboxes = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
            self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,
            self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
            self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16
        ]
        for checkbox in checkboxes:
            if checkbox.isChecked():
                item_name = checkbox.text().split(" ")[0]  # Első szó a termék neve
                item_price = int(checkbox.text().split(" ")[-2].strip(",.-"))  # Ár kinyerése
                self.add_item_to_table(item_name, item_price)

        # Házhozszállítás díjának hozzáadása, ha a RadioButton a "Házhozszállítás" állapotban van
        if self.radioButton_hazhozszallitas.isChecked():
            delivery_item_name = "Házhozszállítás díja"
            delivery_item_price = 590
            self.add_item_to_table(delivery_item_name, delivery_item_price)
            self.frame_hazhozszallitas.setVisible(True)
        else:
            self.frame_hazhozszallitas.setVisible(False)

        self.calculate_total_price()

    def add_item_to_table(self, item_name, item_price):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(item_name))
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem(str(item_price)))

    def calculate_total_price(self):
        total_price = 0
        for row in range(self.tableWidget.rowCount()):
            price_item = self.tableWidget.item(row, 1)
            if price_item:
                item_price = int(price_item.text())
                total_price += item_price

        self.label_total_price.setText(f"Összesen: {total_price} Ft")

    def clear_selections(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(False)
        self.checkBox_13.setChecked(False)
        self.checkBox_14.setChecked(False)
        self.checkBox_15.setChecked(False)
        self.checkBox_16.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PizzaApp()
    sys.exit(app.exec())
