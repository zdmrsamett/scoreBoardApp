import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from kontrolPaneli_python import Ui_Form
from skorTabelasiNew import SkorTabelasiSayfasiNew

class KontrolPaneliSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.kontrolPaneli = Ui_Form()
        self.kontrolPaneli.setupUi(self)
        self.setWindowTitle("ScoreBoardApp")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMinimumSize(460, 170)
        self.setMaximumSize(460, 801)
        self.default_geometry = (730,150,460,800)
        self.setGeometry(*self.default_geometry)
        self.skorTabelasiNew = SkorTabelasiSayfasiNew()
        self.kontrolPaneli.scoreTableOpClBt.clicked.connect(self.skorTabelasiAcKapa)
        self.kontrolPaneli.comboBox.currentIndexChanged.connect(self.updateGeometryKontrol)

        # Renklerin indexlere göre eşleştirildiği liste
        renkler = [
            "black", "gray", "#eee", "blue", "cyan", "red", "#FF7F00",
            "#FFFF00", "#66FF00", "#008000", "#660099", "#FF00FF", "#964B00"
        ]

        # arttır-azalt ve colorpicker butonlarını sırayla alıyor
        for i in range(1, 11):
            inc_button = getattr(self.kontrolPaneli, f'incBt_{i}')
            dec_button = getattr(self.kontrolPaneli, f'decBt_{i}')
            color_picker = getattr(self.kontrolPaneli, f'colorPicker_{i}')  # Renk seçiciyi al

            inc_button.clicked.connect(lambda _, index=i: self.scoreArttir(index))
            dec_button.clicked.connect(lambda _, index=i: self.scoreAzalt(index))
            color_picker.currentIndexChanged.connect(
                lambda _, index=i: self.updateColor(index, renkler))  # Her renk seçicinin değişikliğini yakala
            # Connect the textChanged signals of teamName_X and teamScore_X inputs
            team_name_input = getattr(self.kontrolPaneli, f'teamName_{i}')
            team_score_input = getattr(self.kontrolPaneli, f'teamScore_{i}')
            team_name_input.textChanged.connect(lambda _, index=i: self.updateTeamData(index))
            team_score_input.textChanged.connect(lambda _, index=i: self.updateTeamData(index))

        self.initUI()

    def updateGeometryKontrol(self):
        playerCount = int(self.kontrolPaneli.comboBox.currentText())  # Seçili metni sayıya çevir
        if 1 <= playerCount < 10:
            new_geometry = (730, 150, 460, 170 + 70 * (playerCount - 1))
            self.setGeometry(*new_geometry)
            new_geometry_skor = (400, 150, 289, 70 + 40 * (playerCount - 1))
            self.skorTabelasiNew.setGeometry(*new_geometry_skor)
        elif playerCount == 10:
            new_geometry_skor = (400, 150, 289, 440)
            self.skorTabelasiNew.setGeometry(*new_geometry_skor)

    def updateTeamData(self, index):
        team_name_input = getattr(self.kontrolPaneli, f'teamName_{index}').text()
        team_score_input = getattr(self.kontrolPaneli, f'teamScore_{index}').text()

        team_name_skor = getattr(self.skorTabelasiNew.skorTabelasiNew, f'name_{index}')
        team_score_skor = getattr(self.skorTabelasiNew.skorTabelasiNew, f'score_{index}')

        team_name_skor.setText(team_name_input)
        team_score_skor.setText(team_score_input)

    def updateTeamAreas(self):
        selected_index = self.kontrolPaneli.comboBox.currentIndex() + 1
        checkbox_checked = self.kontrolPaneli.checkBox.isChecked()

        # Tüm teamArea'ları gizle
        for i in range(1, 11):
            team_area = getattr(self.kontrolPaneli, f'teamArea_{i}')
            team_area.setVisible(False)

        # Seçili index'e kadar olan teamArea'ları göster
        for i in range(1, selected_index + 1):
            team_area = getattr(self.kontrolPaneli, f'teamArea_{i}')
            team_area.setVisible(True)

        # tabelada tüm alanları temizle
        for i in range(1, 11):
            isimler_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'name_{i}')
            eşittirler_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'equal_{i}')
            skorlar_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'score_{i}')
            isimler_tabelanew.setVisible(False)
            eşittirler_tabelanew.setVisible(False)
            skorlar_tabelanew.setVisible(False)

        # tabelada tüm alanları temizle
        for i in range(1, selected_index + 1):
            isimler_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'name_{i}')
            eşittirler_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'equal_{i}')
            skorlar_tabelanew = getattr(self.skorTabelasiNew.skorTabelasiNew, f'score_{i}')
            isimler_tabelanew.setVisible(True)
            if checkbox_checked:
                eşittirler_tabelanew.setVisible(True)
                skorlar_tabelanew.setVisible(True)

    def updateTableVisibility(self):
        checkbox_checked = self.kontrolPaneli.checkBox.isChecked()
        selected_index = self.kontrolPaneli.comboBox.currentIndex() + 1
        for i in range(1, selected_index + 1):
            aa = getattr(self.skorTabelasiNew.skorTabelasiNew, f'equal_{i}')
            bb = getattr(self.skorTabelasiNew.skorTabelasiNew, f'score_{i}')
            aa.setVisible(checkbox_checked)
            bb.setVisible(checkbox_checked)

    def skorTabelasiAcKapa(self):
        if not self.skorTabelasiNew.isVisible():
            self.skorTabelasiNew.show()
        else:
            self.skorTabelasiNew.close()

    def closeEvent(self, event):
        if self.skorTabelasiNew.isVisible():
            self.skorTabelasiNew.close()
        event.accept()

    # Function to increase the team score for a specific index
    def scoreArttir(self, index):
        current_score = int(getattr(self.kontrolPaneli, f'teamScore_{index}').text())
        new_score = current_score + 1
        getattr(self.kontrolPaneli, f'teamScore_{index}').setText(str(new_score))

    # Function to decrease the team score for a specific index
    def scoreAzalt(self, index):
        current_score = int(getattr(self.kontrolPaneli, f'teamScore_{index}').text())
        new_score = max(0, current_score - 1)  # Ensure the score does not go below 0
        getattr(self.kontrolPaneli, f'teamScore_{index}').setText(str(new_score))

    def updateColor(self, index, renkler):
        color_index = getattr(self.kontrolPaneli, f'colorPicker_{index}').currentIndex()
        selected_color = renkler[color_index]

        team_name_input = getattr(self.kontrolPaneli, f'teamName_{index}')
        team_score_input = getattr(self.kontrolPaneli, f'teamScore_{index}')
        incBt_input = getattr(self.kontrolPaneli, f'incBt_{index}')
        decBt_input = getattr(self.kontrolPaneli, f'decBt_{index}')

        team_name_skor = getattr(self.skorTabelasiNew.skorTabelasiNew, f'name_{index}')
        team_score_skor = getattr(self.skorTabelasiNew.skorTabelasiNew, f'score_{index}')
        team_equal_skor = getattr(self.skorTabelasiNew.skorTabelasiNew, f'equal_{index}')


        style_input = f"color: {selected_color}; font-family: Poppins; font-weight: bold; font-size: 16px;"
        style_skor = f"color: {selected_color}; font-family: Poppins; font-weight: bold; font-size: 19px; background-color: transparent; border: none;"
        style_button = f"background-color: {selected_color}; border-radius: 15px; border: 1px solid black; color: white; font-family: Poppins; font-size: 16px; font-weight: bold;"

        team_name_input.setStyleSheet(style_input)
        team_score_input.setStyleSheet(style_input)

        incBt_input.setStyleSheet(style_button)
        decBt_input.setStyleSheet(style_button)

        team_name_skor.setStyleSheet(style_skor)
        team_score_skor.setStyleSheet(style_skor)
        team_equal_skor.setStyleSheet(style_skor)


    def initUI(self):
        # Connect the stateChanged signal of the checkBox to the updateTableVisibility function
        self.kontrolPaneli.checkBox.stateChanged.connect(self.updateTableVisibility)

        # Call the function initially to set the initial visibility based on the checkbox state
        self.updateTableVisibility()

        # ComboBox'ın değeri değiştiğinde updateTeamAreas fonksiyonunu çağır
        self.kontrolPaneli.comboBox.currentIndexChanged.connect(self.updateTeamAreas)

        # İlk başta da bir kere çağrılarak başlangıçta doğru durumu ayarla
        self.updateTeamAreas()

        # kontrolpanelindeki isim ve skor alanlarını bold yapar
        for i in range(1, 11):
            isimler = getattr(self.kontrolPaneli, f'teamName_{i}')
            isimler.setStyleSheet(""" font-weight: bold; """)
        for i in range(1, 11):
            skorlar = getattr(self.kontrolPaneli, f'teamScore_{i}')
            skorlar.setStyleSheet(""" font-weight: bold; """)

        cssKontrolPaneli = """
            background-color: gray;
            border-radius: 15px;
            box-shadow: 5px 5px 5px black;
            border: 1px solid black;
            color: white;
            font-size: 16px;
            font-weight: bold;
        """
        self.kontrolPaneli.scoreTableOpClBt.setStyleSheet(cssKontrolPaneli)

        for i in range(1, 11):
            arttir = getattr(self.kontrolPaneli, f'incBt_{i}')
            arttir.setStyleSheet(cssKontrolPaneli)

        for i in range(1, 11):
            azalt = getattr(self.kontrolPaneli, f'decBt_{i}')
            azalt.setStyleSheet(cssKontrolPaneli)


