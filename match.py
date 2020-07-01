import team
import db_con
import shutil


class Match:

    def __init__(self, tea, teb, actual_match):
        self.id = actual_match[0]
        self.team_a = tea
        self.team_b = teb
        self.score_a = actual_match[3]
        self.score_b = actual_match[4]
        self.fouls_a = actual_match[5]
        self.fouls_b = actual_match[6]
        self.max_fouls = actual_match[9]
        self.match_length = actual_match[8]
        self.last_saved_min = actual_match[8]
        self.last_saved_sec = 0
        self.timer_on = False
        self.match_action = 0
        self.match_actions = db_con.db_get_match_actions()
        self.save_as_txt(self.team_a.sh_name, "teama.txt")
        self.save_as_txt(self.team_b.sh_name, "teamb.txt")
        self.save_as_txt("", "bramkia.txt")
        self.save_as_txt("", "bramkib.txt")
        self.team_a.tricot_color_divs("colors_a")
        self.team_b.tricot_color_divs("colors_b")
        self.squad_divs()

    # def __init__(self, tma, tmb, sca = 0, scb = 0, foa = 0, fob = 0, fox = 5, mle = 40):
    #     self.team_a = tma
    #     self.team_b = tmb
    #     self.score_a = sca
    #     self.score_b = scb
    #     self.fouls_a = foa
    #     self.fouls_b = fob
    #     self.max_fouls = fox
    #     self.match_length = mle
    #     self.last_saved_min = mle
    #     self.last_saved_sec = 0
    #     self.timer_on = False
    #     self.match_action = 0
    #     self.match_actions = db_con.db_get_match_actions()

    #####################
    # METODY DLA TEAM A #
    #####################

    def score_a_up(self):
        self.score_a += 1
        self.save_as_txt(self.score_a, "bramkia.txt")

    def score_a_down(self):
        if self.score_a > 0:
            self.score_a -= 1
        self.save_as_txt(self.score_a, "bramkia.txt")

    def get_score_a(self):
        return self.score_a

    def fouls_a_up(self):
        if self.fouls_a < self.max_fouls:
            self.fouls_a += 1
        self.save_both_fouls_a_versions()

        # self.save_as_txt(self.fouls_a, "fouls_a.txt")
        # self.save_as_symbol(self.fouls_a, "●", "faulea.txt")

    def fouls_a_down(self):
        if self.fouls_a > 0:
            self.fouls_a -= 1
        self.save_both_fouls_a_versions()
        # self.save_as_txt(self.fouls_a, "fouls_a.txt")
        # self.save_as_symbol(self.fouls_a, "●", "faulea.txt")

    def get_fouls_a(self):
        return self.fouls_a

    def save_both_fouls_a_versions(self):
        self.save_as_txt(self.fouls_a, "fouls_a.txt")
        self.save_as_symbol(self.fouls_a, "●", "faulea.txt")

    def team_a_set_logo(self):
        shutil.copy("gfx/logo/" + self.team_a.logo_file, "gfx/logoa.png")


    #####################
    # METODY DLA TEAM B #
    #####################

    def score_b_up(self):
        self.score_b += 1
        self.save_as_txt(self.score_b, "bramkib.txt")

    def score_b_down(self):
        if self.score_b > 0:
            self.score_b -= 1
        self.save_as_txt(self.score_b, "bramkib.txt")

    def get_score_b(self):
        return self.score_b

    def fouls_b_up(self):
        if self.fouls_b < self.max_fouls:
            self.fouls_b += 1
        self.save_both_fouls_b_versions()

        # self.save_as_txt(self.fouls_b, "fouls_b.txt")
        # self.save_as_symbol(self.fouls_b, "●", "fauleb.txt")

    def fouls_b_down(self):
        if self.fouls_b > 0:
            self.fouls_b -= 1
        self.save_both_fouls_b_versions()
        # self.save_as_txt(self.fouls_b, "fouls_b.txt")
        # self.save_as_symbol(self.fouls_b, "●", "fauleb.txt")

    def get_fouls_b(self):
        return self.fouls_b

    def save_both_fouls_b_versions(self):
        self.save_as_txt(self.fouls_b, "fouls_b.txt")
        self.save_as_symbol(self.fouls_b, "●", "fauleb.txt")

    def team_b_set_logo(self):
        shutil.copy("gfx/logo/" + self.team_b.logo_file, "gfx/logob.png")





    ### ZAPISUJE PLIKI ODCZYTYWANE PRZEZ OBS ###
    #
    def save_as_txt(self, val, file):
        with open('txt/' + file, 'w', encoding="utf-8") as f:
            f.write(str(val))
    # wariant zapisu ilości fauli w postaci kropek, albo innego symbolu
    def save_as_symbol(self, val, symbol, file):
        x = val * symbol
        with open('txt/' + file, 'w', encoding="utf-8") as f:
            f.write(str(x))

    def actual_min(self):
        return self.match_length - self.last_saved_min

    def set_match_action(self, x):
        self.match_action = x

    # tworzy div-y ze strzelcami bramek
    def strikers_divs(self):
        events_a = db_con.db_select_match_data(self.team_a.id, self.id)
        events_b = db_con.db_select_match_data(self.team_b.id, self.id)
        # "<tr><td>15' K. Bosak</td></tr>"
        print(events_a)
        divs_a = "<table class='strikersa'>"
        for i in events_a:
            if i[2] == 1:
                first_name = i[7]
                initial = first_name[0:1]
                divs_a += "<tr><td class='time'>" + i[1] + "'</td><td class='name_a'>" + initial + ". " + i[8] + "</td></tr>"
            elif i[2] == 4:
                first_name = i[7]
                initial = first_name[0:1]
                divs_a += "<tr><td class='time'>" + i[1] + "'</td><td class='name_a'>" + initial + ". " + i[8] + "</td><td>(S)</td></tr>"
        divs_a += "</table>"
        self.save_as_txt(divs_a, "strikers_a.txt")

        divs_b = "<table class='strikersb'>"
        for i in events_b:
            if i[2] == 1:
                first_name = i[7]
                initial = first_name[0:1]
                divs_b += "<tr><td class='time'>" + i[1] + "'</td><td class='name_b'>" + initial + ". " + i[8] + "</td></tr>"
            elif i[2] == 4:
                first_name = i[7]
                initial = first_name[0:1]
                divs_b += "<tr><td class='time'>" + i[1] + "'</td><td class='name_b'>" + initial + ". " + i[8] + "</td><td>(S)</td></tr>"
        divs_b += "</table>"
        self.save_as_txt(divs_b, "strikers_b.txt")


    def squad_divs(self):
        squad_a = self.team_a.squad
        squad_a = sorted(squad_a, key=lambda x: (x[3], x[14], x[13]))
        squad_b = self.team_b.squad
        squad_b = sorted(squad_b, key=lambda x: (x[3], x[14], x[13]))

        divs_a = '<table id="matchSquad">'
        delay = 10
        for i in squad_a:
            delay = 20
            # initial = i[12][0:1]+"."
            initial = i[12]
            nr = i[14]
            if i[14] == 0:
                nr = " "
            else:
                nr = str(i[14])
            if i[3] == "Bramkarz" and i[17] == 1:
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> B K </td><td> </td></tr>'
                divs_a += x
            elif i[3] == "Bramkarz":
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> B </td><td> </td></tr>'
                divs_a += x
            elif i[17] == 1:
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> K </td><td> </td></tr>'
                divs_a += x
            else:
                # x = "<tr><td> </td><td>"+ nr + " </td><td> </td><td>" + initial + ".  " + i[13] + "</td><td> </td><td> </td></tr>"
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + \
                    i[13] + '</td><td> </td><td> </td></tr>'
                divs_a += x
        divs_a += "</table>"
        self.save_as_txt(divs_a, "squad_a_div.txt")

        divs_b = '<table id="matchSquad">'
        delay = 10
        for i in squad_b:
            delay = 20
            initial = i[12]
            # initial = i[12][0:1]+"."
            nr = i[14]
            if i[14] == 0:
                nr = " "
            else:
                nr = str(i[14])
            if i[3] == "Bramkarz" and i[17] == 1:
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> B K </td><td> </td></tr>'
                divs_b += x
            elif i[3] == "Bramkarz":
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> B </td><td> </td></tr>'
                divs_b += x
            elif i[17] == 1:
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + i[13] + '</td><td> K </td><td> </td></tr>'
                divs_b += x
            else:
                x = '<tr class="row" style="-webkit-animation: fadeMe ' + str(delay) + 's;"><td>' + nr + ' </td><td class="playerName">' + initial + ' ' + \
                    i[13] + '</td><td> </td><td> </td></tr>'
                divs_b += x
        divs_b += "</table>"
        self.save_as_txt(divs_b, "squad_b_div.txt")
        # <table>
        # <tr><td>ccccccccccccc</td></tr>
        # </table>