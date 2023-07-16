import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi



class PizzaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pizza.ui", self)  # .ui fájl betöltése

        # Gombokhoz csatlakoztatott eseménykezelők. Ha változik az állapotuk...
        self.comboBox.currentIndexChanged.connect(self.update_table)
        self.comboBox_2.currentIndexChanged.connect(self.update_table)

        # CheckBox-okhoz csatlakoztatott eseménykezelők. Ha változik az állapotuk
        checkboxes = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
            self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,
            self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
            self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16,
            self.checkBox_17, self.checkBox_18, self.checkBox_19,
            self.checkBox_20, self.checkBox_21, self.checkBox_22
        ]
        for checkbox in checkboxes:
            checkbox.stateChanged.connect(self.update_table)  # ha változik az állapot a táblázat frissül

        # Radio button-hoz csatlakoztatott eseménykezelő. Ha házhozszállítás, Beárazom
        self.radioButton_Helyben.toggled.connect(self.update_table)
        self.radioButton_hazhozszallitas.toggled.connect(self.update_table)

        # Táblázat inicializálása
        self.tableWidget.setColumnCount(2)  # Oszlopok száma
        self.tableWidget.setHorizontalHeaderLabels(["Tétel", "Ár"])
        self.tableWidget.setColumnWidth(0, 300)  # Tétel oszlop szélessége
        self.tableWidget.setColumnWidth(1, 90)  # Ár oszlop szélessége

        # Frame_hazhozszallitas kezdeti állapotának beállítása - Nem látszik
        self.frame_hazhozszallitas.setVisible(False)

        # Alapértelmezett állapot beállítása
        self.stackedWidget.setCurrentIndex(0)  # 0 indexű Widget

        # PushButton-hoz csatlakoztatott eseménykezelő
        self.pushButton.clicked.connect(self.process_order)  # futár rendelés gomb

        self.setWindowTitle("Pizza Napoletana - ételrendelés")  # az ablak neve

        self.show()

    def update_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        teszta = self.comboBox.currentText()  # az első két sor a pizza mindig
        alap = self.comboBox_2.currentText()

        teszta_ara = 900
        alap_ara = 0

        if teszta == "Vékony tészta":
            teszta_ara += 100
        elif teszta == "Vastag tészta":
            teszta_ara += 200
        elif teszta == "Sajt szélű tészta":
            teszta_ara += 300
        elif teszta == "Bacon szélű tészta":
            teszta_ara += 400

        if alap == "Paradicsomos alap":
            alap_ara += 100
        elif alap == "Tejszínes alap":
            alap_ara += 100
        elif alap == "Csípős alap":
            alap_ara += 100

        self.add_item_to_table(teszta, teszta_ara)
        self.add_item_to_table(alap, alap_ara)

        checkboxes = [
            self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
            self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8,
            self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
            self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16,
            self.checkBox_17, self.checkBox_18, self.checkBox_19,
            self.checkBox_20, self.checkBox_21, self.checkBox_22
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

        self.label_total_price.setStyleSheet("QLabel { color: yellow; }")
        self.label_total_price.setText(f"Összesen:   {total_price} Ft")  # 0-as indexű widget
        self.label_total_price_2.setText(f"Összesen fizetendő:   {total_price} Ft")  # 1-es indexű widget

    def process_order(self):
        nev = self.lineEdit.text()
        cim = self.lineEdit_2.text()
        telefon = self.lineEdit_3.text()
        megjegyzes = self.lineEdit_4.text()

        self.label_13.setText(nev)
        self.label_15.setText(cim)
        self.label_17.setText(telefon)
        self.label_19.setText(megjegyzes)
        self.stackedWidget.setCurrentIndex(1)
        self.frame_hazhozszallitas.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PizzaApp()
    sys.exit(app.exec())
