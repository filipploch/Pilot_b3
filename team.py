import db_con


class Team():

    def __init__(self, id):
        tab = db_con.db_get_team(id)
        self.id = tab[0]
        self.name = tab[1]
        self.competition = tab[2]
        self.link = tab[3]
        self.sh_name = tab[4]
        self.tricot_1_colors = [tab[6], tab[7], tab[8]]
        self.tricot_2_colors = [tab[10], tab[11], tab[12]]
        self.home_colors_nr = self.getColorsNumber(self.tricot_1_colors)
        self.away_colors_nr = self.getColorsNumber(self.tricot_2_colors)
        self.bibs_color = tab[14]
        # self.col1 = tab[6]
        # self.col2 = tab[7]
        # self.col3 = tab[8]
        self.color_for_ui = tab[9   ]
        self.players = db_con.db_get_players(str(self.id))
        self.squad = db_con.db_get_squad(str(self.id))
        self.selected_tricot = tab[13]
        self.logo_file = tab[16]
        self.squad_info_bar = ""
        #self.set_lead_color()

    def __del__(self):
        print("__del__")

    def match_squad(self):
        s = db_con.db_get_squad(str(self.name))
        return s

    def getColorsNumber(self, tricot_colors):
        number = 0
        for i in range(3):
            if tricot_colors[i] != "":
                number += 1
        return number

    def setColorsNumber(self):
        if self.home_colors_nr == 1:
            self.tricot_1_colors[1] = ""
            self.tricot_1_colors[2] = ""
        if self.home_colors_nr == 2:
            self.tricot_1_colors[2] = ""
        if self.away_colors_nr == 1:
            self.tricot_2_colors[1] = ""
            self.tricot_2_colors[2] = ""
        if self.away_colors_nr == 2:
            self.tricot_2_colors[2] = ""

    def tricot_color_divs(self, file_name):
        if self.selected_tricot == 1:
            tricot = self.tricot_1_colors
        elif self.selected_tricot == 2:
            tricot = self.tricot_2_colors
        else: tricot = self.bibs_color

        colors_number = self.getColorsNumber(tricot)
        print(colors_number)
        path = 'txt/'
        x = ""
        for i in range(colors_number):
            d = str(int(1 / colors_number * 100))
            if i == colors_number - 1:
                x += '<div style="float: left; height: 6px; width: ' + d + '%; background-color: ' \
                     + tricot[i] + ';"></div><div class="cleaner"></div>'
            else:
                x += '<div style="float: left; height: 6px; width: ' + d + '%; background-color: ' \
                     + tricot[i] + ';"></div>'
        f = open(path + file_name + ".txt", "w+")
        f.write(x)
        f.close()


    # def set_lead_color(self):
    #     if self.color_for_ui == "1":
    #         col_x = self.tricot_1_colors[0]
    #     elif self.color_for_ui == "2":
    #         col_x = self.tricot_1_colors
    #     else:
    #         col_x = self.col3
    #     return col_x

