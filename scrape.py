#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import team
import db_con
import re
import lxml

class Scrape():

    adress_a = 'http://nalffutsal.pl/?page_id=16'
    adress_b = 'http://nalffutsal.pl/?page_id=36'
    file_a = 'table_a'
    file_b = 'table_b'

    def scrape_table(self, adress, file):
        source = requests.get(adress).text
        soup = BeautifulSoup(source, 'lxml')
        table_a_div = soup.find('div', class_='sportspress')

        team_position = table_a_div.find_all("td", {"class":"data-rank"})
        team_name = table_a_div.find_all("td", {"class":"data-name"})
        team_matches = table_a_div.find_all("td", {"class":"data-m"})
        team_wins = table_a_div.find_all("td", {"class":"data-z"})
        team_ties = table_a_div.find_all("td", {"class":"data-r"})
        team_loses = table_a_div.find_all("td", {"class":"data-p"})
        team_goals_scored = table_a_div.find_all("td", {"class":"data-gz"})
        team_goals_lost = table_a_div.find_all("td", {"class":"data-gs"})
        team_points = table_a_div.find_all("td", {"class":"data-pkt"})
        team_a = []

        table = []

        ile = len(team_position)

        for i in range(ile):
            row = [team_position[i].text, team_name[i].text, team_matches[i].text, team_wins[i].text, team_ties[i].text,\
                           team_loses[i].text, team_goals_scored[i].text, team_goals_lost[i].text, team_points[i].text]
            table.append(row)
            print(row)


       # # def save_table2(adress):
        my_filename = file + ".html"
        start_html = '<html><head><meta charset="ISO-8859" /><meta http-equiv="X-UA-Compatible"/>'\
                     '<link rel="stylesheet" href="css\cssteams.css"></head>'\
                     '<body"><div id="container"><div id="top_bar"><img src="gfx/belka_gora.png" id="img_top">'\
                     '<div id="league">NOWOHUCKA AMATORSKA LIGA FUTSALU</div>'
        if adress == self.adress_a:
            table_html = '<div id="division">Dywizja A</div></div><table class="table_a"><thead><tr class="class_header"><th class="data-rank"></th><th class="data-name"></th><th class="data-m">M</th><th class="data-z">Z</th><th class="data-r">R</th><th class="data-p">P</th><th class="data-gz">GZ</th><th class="data-gs">GS</th><th class="data-pkt">Pkt</th></tr></thead><tbody>'
        elif adress == self.adress_b:
            table_html = '<div id="division">Dywizja B</div></div><table class="table_b"><thead><tr class="class_header"><th class="data-rank"></th><th class="data-name"></th><th class="data-m">M</th><th class="data-z">Z</th><th class="data-r">R</th><th class="data-p">P</th><th class="data-gz">GZ</th><th class="data-gs">GS</th><th class="data-pkt">Pkt</th></tr></thead><tbody>'
        insert_html = ''
        end_html = '</div></div><div id="bottom_bar"><img src="gfx/druzyny-logo-belka.png" id="img_bottom">'\
                   '</div></div></body></html>'
        which = bool
        tr_class = ''
        for i in range(ile):
            if which != True:
                tr_class = "first"
            else: tr_class = "second"
            insert_html += '<tr class="class_'+ tr_class +'"><td class="team_pos">' + table[i][0] + \
                           '</td><td class="team_name">' + table[i][1] + '</td><td>' + table[i][2] + \
                           '</td><td>' + table[i][3] + '</td><td>' + table[i][4] + \
                          '</td><td>' + table[i][5] + '</td><td>' + table[i][6] + \
                          '</td><td>' + table[i][7] + '</td><td class="points">' + table[i][8] + \
                           '</td></tr>'
            if which == True:
                which = False
            else: which = True

        final_html = start_html + table_html + insert_html + end_html

        f = open(my_filename, "w+")
        f.write(final_html)
        f.close()
        table.clear()

    def scrape_teams(self, adress_a, adress_b):
        source_a = requests.get(adress_a).text
        source_b = requests.get(adress_b).text
        soup_a = BeautifulSoup(source_a, 'lxml')
        soup_b = BeautifulSoup(source_b, 'lxml')
        table_a_div = soup_a.find('div', class_='sportspress')
        table_b_div = soup_b.find('div', class_='sportspress')
        teams = table_a_div.find_all("td", {"class": "data-name"})
        teams += table_b_div.find_all("td", {"class": "data-name"})


    def scrape_players(self, adress):
        source = requests.get(adress).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('div', class_="sp-template sp-template-player-list")
        if table is None:
            pass
        else:
            tab = []
            tab.append(table.find_all("td", {"class":"data-name"}))
            tab.append(table.find_all("td", {"class":"data-team"}))
            tab.append(table.find_all("td", {"class":"data-position"}))
            tab.append(table.find_all("td", {"class":"data-appearances"}))
            tab.append(table.find_all("td", {"class":"data-goals"}))
            tab.append(table.find_all("td", {"class":"data-assists"}))
            tab.append(table.find_all("td", {"class":"data-yellowcards"}))
            tab.append(table.find_all("td", {"class":"data-redcards"}))
            tab.append(table.find_all("td", {"class":"data-owngoals"}))
            tab.append(table.find_all("td", {"class":"data-pitkakolejki"}))
            tab.append(table.find_all("td", {"class":"data-zawodnikkolejki"}))
            db_con.db_add_player(tab)



