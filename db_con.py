#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import team

def db_add_player(tab):

    l = len(tab[0])
    for i in range(l):
        full_name = tab[0][i].find('a').text
        tea = tab[1][i].find('a').text
        pos = tab[2][i].text
        mat = tab[3][i].text
        goals = tab[4][i].text
        assists = tab[5][i].text
        yel = tab[6][i].text
        red = tab[7][i].text
        own = tab[8][i].text
        split_name = str(full_name).split(" ")
        if len(split_name) == 2:
            f_name = split_name[1]
            l_name = split_name[0]
        elif len(split_name) == 3:
            f_name = split_name[2]
            l_name = split_name[0] + " " + split_name[1]


        #sql_query_insert = "INSERT INTO `teams` (`id`, `full_name`, `competitions`, `link`) VALUES (NULL, '" + fna + "', '" + com + "', '" + lin + "');"
        sql_query_insert = "INSERT INTO `players`(`id`, `full_name`, `team`, `position`, `matches`, `goals`, \
        `assists`, `yellow_cards`, `red_cards`, `own_goals`, `first_name`, `last_name`) \
         VALUES (NULL, '" + full_name + "','" + tea + "','" + pos + "','" + mat + "','" + goals + "','" + assists + "','" + yel + "','" + red + "','" + own + "','" + f_name + "','" + l_name + "')"
        sql_query_if_exist = "SELECT * FROM players WHERE `full_name` = '" + full_name + "'"
        sql_query_update = "UPDATE `players` SET `team`='" + tea + "',`position`='" + pos + "',`matches`='" + mat + \
                           "',`goals`='" + goals + "',`assists`='" + assists + "',`yellow_cards`='" + yel + \
                           "',`red_cards`='" + red + "',`own_goals`='" + own + "' WHERE full_name='" + full_name + "' AND team='" + tea + "'"

        try:

            db = pymysql.connect("localhost", "root", "", "futsal")
            with db.cursor() as cursor1:
                cursor1.execute(sql_query_if_exist)
                player = cursor1.fetchone()
                if player is None:
                    with db.cursor() as cursor:
                        cursor.execute(sql_query_insert)
                else:
                    with db.cursor() as cursor:
                        cursor.execute(sql_query_update)
            db.commit()
            db.close()

        except:
            print('ERROR: ADD PLAYER')

def db_select_teams():
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM teams")
        teams = cursor.fetchall()
        db.close()
        return teams

    except:
        print('BLAD: db_get_teams')

def db_get_team(id):
    idstr = str(id)
    sql_query = "SELECT * FROM teams WHERE id='" + idstr + "'"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        team = cursor.fetchone()
        db.close()
        return team
    except:
        print('BLAD: db_get_team(id)')

def db_get_players(team_id):
    sql_query = "SELECT `players`.*, `teams`.`id` FROM players, teams WHERE teams.id='" + str(team_id) + "' AND teams.full_name = players.team"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        players = cursor.fetchall()
        db.close()
        return players

    except:
        print("BLAD: db_get_players")

def db_get_squad(team_id):
    sql_query = "SELECT `players`.*, `teams`.`id` FROM players, teams WHERE players.squad='1' AND teams.id='" + str(team_id) + "' AND teams.full_name = players.team"
    # sql_query = "SELECT * FROM players WHERE id='" + team_id + "' AND squad='1'"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        squad = cursor.fetchall()
        db.close()
        return squad

    except:
        print("BLAD: db_get_players")

def db_select_actual_match():
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `matches` WHERE `actual` = 1")
        actual_match = cursor.fetchone()
        db.close()
        return actual_match
    except:
        print('BLAD: db_get_match_action')

def db_get_match_actions():
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM match_action")
        match_actions = cursor.fetchall()
        db.close()
        return match_actions
    except:
        print('BLAD: db_get_match_action')

def db_select_info_bar_text():
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute("SELECT `info_bar_text` FROM `info_bar` ")
        actual_match = cursor.fetchall()
        db.close()
        return actual_match
    except:
        print('BLAD: db_select_info_bar_text')

def db_delete_by_id(table, id):
    sql_query = "DELETE FROM `" + table + "` WHERE `id`=" + str(id)
    print(sql_query)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        db.close()
    except:
        print('BLAD: db_delete_by_id')
# def db_update_colors(team):
#     sql_query_update = "UPDATE `teams` SET `color_one`='" + team[6] + "',`color_two`='" + team[7] + \
#                        "',`color_three`='" + team[8] + "',`color_lead`='" + team[9] + "' \
#                        WHERE full_name='" + team[2] + "'"
#     try:
#         db = pymysql.connect("localhost", "root", "", "futsal")
#         cursor = db.cursor()
#         cursor.execute(sql_query_update)
#         db.commit()
#         db.close()
#     except:
#         print('BLAD: db_update_colors')

def db_update_colors(tricot1, tricot2, bibs_color, ui_color, team_id):

    sql_query_update = "UPDATE `teams` SET `home_color_one`='" + str(tricot1[0]) + "',`home_color_two`='" + str(tricot1[1]) + \
                       "',`home_color_three`='" + str(tricot1[2]) + "',`away_color_one`='" + str(tricot2[0]) + \
                       "',`away_color_two`='" + str(tricot2[1]) + "',`away_color_three`='" + str(tricot2[2]) + \
                       "',`bibs_color`='" + str(bibs_color) + "',`color_for_ui`='" + str(ui_color) +  "' WHERE id='" + str(team_id) + "'"
    print(sql_query_update)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_colors')


def db_update_color_number(col, f_name):
    sql_query_update = "UPDATE `teams` SET `home_tricot_color_number`='" + col + "' WHERE full_name='" + f_name + "'"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_color_number')

# def db_update_color_lead(nr, f_name):
#     sql_query_update = "UPDATE `teams` SET `color_lead`='" + str(nr) + "' WHERE full_name='" + f_name + "'"
#     print(sql_query_update)
#
#     try:
#         db = pymysql.connect("localhost", "root", "", "futsal")
#         cursor = db.cursor()
#         cursor.execute(sql_query_update)
#         db.commit()
#         db.close()
#     except:
#         print('BLAD: db_update_color_number')


def db_update_numbers(table):

    x = table.rowCount()
    for i in range(x):
        if table.item(i, 1).text() != None:
            num = table.item(i, 1).text()
            player_id = str(table.item(i, 5).text())
            if num != "":
                sql_query_update = "UPDATE `players` SET `default_nr`='" + num + "' WHERE id='" + player_id + "'"

                try:
                    db = pymysql.connect("localhost", "root", "", "futsal")
                    cursor = db.cursor()
                    cursor.execute(sql_query_update)
                    db.commit()
                    db.close()
                except:
                    print('BLAD: db_update_numbers')

def db_update_first_name(table):

    x = table.rowCount()
    for i in range(x):
        if table.item(i, 2).text() != None:
            fname = table.item(i, 2).text()
            player_id = str(table.item(i, 5).text())
            if fname != "":
                sql_query_update = "UPDATE `players` SET `first_name`='" + fname + "' WHERE id='" + player_id + "'"

                try:
                    db = pymysql.connect("localhost", "root", "", "futsal")
                    cursor = db.cursor()
                    cursor.execute(sql_query_update)
                    db.commit()
                    db.close()
                except:
                    print('BLAD: db_update_first_name')

def db_update_last_name(table):
    x = table.rowCount()
    for i in range(x):
        if table.item(i, 3).text() != None:
            lname = table.item(i, 3).text()
            player_id = str(table.item(i, 5).text())
            if lname != "":
                sql_query_update = "UPDATE `players` SET `last_name`='" + lname + "' WHERE id='" + player_id + "'"

                try:
                    db = pymysql.connect("localhost", "root", "", "futsal")
                    cursor = db.cursor()
                    cursor.execute(sql_query_update)
                    db.commit()
                    db.close()
                except:
                    print('BLAD: db_update_last_name')

def db_update_position(table):
    x = table.rowCount()
    # pos = ""
    for i in range(x):
        if table.cellWidget(i, 4).isChecked():
            pos = "Bramkarz"
        else:
            pos = "Zawodnik z pola"

        player_id = str(table.item(i, 5).text())
        sql_query_update = "UPDATE `players` SET `position`='" + pos + "' WHERE id='" + player_id + "'"
        try:
            db = pymysql.connect("localhost", "root", "", "futsal")
            cursor = db.cursor()
            cursor.execute(sql_query_update)
            db.commit()
            db.close()
        except:
            print('BLAD: db_update_position')

def db_update_squad(table):
    x = table.rowCount()
    # pos = ""
    for i in range(x):
        if table.cellWidget(i, 0).isChecked():
            s = "1"
        else:
            s = "0"

        player_id = str(table.item(i, 5).text())
        sql_query_update = "UPDATE `players` SET `squad`='" + s + "' WHERE id='" + player_id + "'"
        try:
            db = pymysql.connect("localhost", "root", "", "futsal")
            cursor = db.cursor()
            cursor.execute(sql_query_update)
            db.commit()
            db.close()
        except:
            print('BLAD: db_update_squad')

def db_update_captain(table):
    x = table.rowCount()
    # pos = ""
    for i in range(x):
        if table.cellWidget(i, 6).isChecked():
            c = "1"
        else:
            c = "0"
        player_id = str(table.item(i, 5).text())
        sql_query_update = "UPDATE `players` SET `captain`='" + c + "' WHERE id='" + player_id + "'"
        try:
            db = pymysql.connect("localhost", "root", "", "futsal")
            cursor = db.cursor()
            cursor.execute(sql_query_update)
            db.commit()
            db.close()
        except:
            print('BLAD: db_update_captain')

def db_update_lead_color(col, f_name):
    sql_query_update = "UPDATE `teams` SET `color_lead`='" + col + "'\
     WHERE full_name='" + f_name + "'"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_lead_color')

def db_get_actual_match():
    sql_query = "SELECT * FROM `matches` WHERE actual='1'"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        actual_match = cursor.fetchall()
        db.close()
        return actual_match

    except:
        print('BLAD: db_get_actual_match')

def db_update_match_value(varia, value):
    sql_query_update = "UPDATE `matches` SET `" + varia + "`='" + str(value) + "'WHERE actual=1"
    print(sql_query_update)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_value')

def db_update_change_player(player_id, event_id):
    sql_query_update = "UPDATE `matches_data` SET `player_id`='" + str(player_id) + "'WHERE id=" + event_id
    print(sql_query_update)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_change_player')

def db_delete_action(event_id):
    sql_query_update = "DELETE FROM `matches_data` WHERE `matches_data`.`id` = " + event_id
    print(sql_query_update)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_delete_action')

def update_tricot(tricot_number, team_id):
    sql_query_update = "UPDATE `teams` SET `selected_tricot`='" + str(tricot_number) + "' WHERE id='" + str(team_id) + "'"
    print(sql_query_update)

    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: update_tricot')

def db_update_match_data(match_data):
    sql_query_update = "INSERT INTO `matches_data`(`time`, `action`, `player_id`, `match_id`, `team_id`) VALUES ("+ \
                       str(match_data[0]) + "," + str(match_data[1]) + "," + str(match_data[2]) + "," +\
                       str(match_data[3]) + "," + str(match_data[4]) + ")"
    print(sql_query_update)
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_match_data')

def db_update_match_actual_null():
    sql_query_update = "UPDATE `matches` SET `actual`=0 WHERE actual=1"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query_update)
        db.commit()
        db.close()
    except:
        print('BLAD: db_update_match_actual_null')

def db_insert_new_match():
    sql_query = "INSERT INTO `matches`(`id`, `team_a`, `team_b`, `score_a`, `score_b`, `fouls_a`, `fouls_b`, `actual`, `match_length`, `max_fouls`) VALUES (null,222,220,0,0,0,0,1,40,5)"
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        cursor.execute(sql_query)
        db.commit()
        db.close()
    except:
        print('BLAD: db_insert_new_match')
def db_select_match_data(team_id, match_id):
    try:
        db = pymysql.connect("localhost", "root", "", "futsal")
        cursor = db.cursor()
        sql_query = "SELECT `matches_data`.*, `players`.first_name, `players`.last_name, `match_action`.desc_polish, `teams`.* FROM matches_data, players, match_action, teams\
         WHERE matches_data.team_id=" + str(team_id) + " and matches_data.match_id=" + str(match_id) +\
                    " AND matches_data.team_id='" + str(team_id) +\
                    "' AND matches_data.team_id = teams.id AND matches_data.player_id = players.id AND matches_data.action = match_action.id ORDER BY `matches_data`.id ASC"
        print(sql_query)
        cursor.execute(sql_query)
        # cursor.execute("SELECT * FROM matches_data WHERE team_id=" + str(team_id) + " and match_id=" + str(match_id) + " ORDER BY `matches_data`.`event_time` ASC")
        match_data = cursor.fetchall()
        db.close()
        return match_data
    except:
        print('BLAD: db_select_match_data')

# def db_update_squad(tab):
#     id = tab[0]
#     nr = str(tab[1])
#     fn = tab[2]
#     ln = tab[3]
#     sql_query_update = "UPDATE `players` SET first_name='" + fn + "', last_name='" + ln + "', default_nr='" + nr + "'WHERE id='" + id + "'"
#     try:
#         db = pymysql.connect("localhost", "root", "", "futsal")
#         cursor = db.cursor()
#         cursor.execute(sql_query_update)
#         db.commit()
#         db.close()
#     except:
#         print('BLAD: db_update_squad')