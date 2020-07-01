# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pilot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QListWidget, QCheckBox, QRadioButton, QLabel, QComboBox, \
    QColorDialog, QButtonGroup, QLineEdit, QMessageBox
import sys, os
from PyQt5.QtGui import QPixmap, QMovie
#import select_teams
import match
import team
import db_con
import threading
import time
from select_teams import Select_teams
import colorpicker
import scrape
import start_window
from functools import partial
import gc

class Ui_Pilot(object):
    def __init__(self):
        self.actual_match = db_con.db_select_actual_match()
        self.all_teams = db_con.db_select_teams()
        self.team_a_id = self.actual_match[1]
        self.team_b_id = self.actual_match[2]
        self.team_a = team.Team(self.team_a_id)
        self.team_b = team.Team(self.team_b_id)
        self.select_team_a(self.team_a)
        self.select_team_b(self.team_b)
        self.make_match()
        self.edited_team_id = None

    def get_squad_a(self):
        # team_a_id = run.team_a_id
        name = self.team_a.name
        squad = db_con.db_get_squad(name)

        return squad

    def get_squad_b(self):
        # team_b_id = run.team_b_id
        # self.team_b = team.Team(db_con.db_get_team(str(team_b_id)))
        # return self.team_b.squad
        name = self.team_b.name
        squad = db_con.db_get_squad(name)

        return squad


    def setupUi(self, Panel):

        Panel.setObjectName("Panel")
        Panel.setEnabled(True)
        Panel.resize(278, 520)
        Panel.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(Panel)
        self.centralwidget.setObjectName("centralwidget")
        self.timerStartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerStartBtn.setEnabled(True)
        self.timerStartBtn.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.timerStartBtn.setObjectName("timerStartBtn")
        self.timerPauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerPauseBtn.setEnabled(True)
        self.timerPauseBtn.setGeometry(QtCore.QRect(100, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.timerPauseBtn.setFont(font)
        self.timerPauseBtn.setObjectName("timerPauseBtn")
        self.second_half_btn = QPushButton("II połowa", self.centralwidget)
        self.second_half_btn.setEnabled(True)
        self.second_half_btn.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.second_half_btn.setObjectName("second_half_btn")
        self.second_half_btn.setVisible(False)
        self.pause_control_light_off = QtWidgets.QLabel(self.centralwidget)
        self.pause_control_light_off.setGeometry(42, 12, 35, 35)
        self.pause_control_light_off.setText("")
        self.pause_control_light_off.setPixmap(QtGui.QPixmap("gfx/light_off.gif"))
        self.pause_control_light_off.setScaledContents(True)
        self.pause_control_light_off.setObjectName("pause_control_light_off")
        # set up the movie screen on a label
        self.movie_screen = QtWidgets.QLabel(self.centralwidget)
        self.movie_screen.setGeometry(41, 12, 36, 35)
        # expand and center the label
        # self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setScaledContents(True)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        self.pause_control_light_on = QMovie("gfx/light_on.gif")
        self.pause_control_light_on.setCacheMode(QMovie.CacheAll)
        self.pause_control_light_on.setSpeed(100)
        self.movie_screen.setMovie(self.pause_control_light_on)
        self.pause_control_light_on.start()

        # self.pause_control_light_on.setGeometry(12, 12, 35, 35)
        # self.pause_control_light_on.setText("")
        # self.pause_control_light_on.setPixmap(QtGui.QPixmap("gfx/light_on.gif"))
        # self.pause_control_light_on.setScaledContents(True)
        self.pause_control_light_on.setObjectName("pause_control_light_on")
        self.movie_screen.setVisible(False)
        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(100, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.displayLabel.setFont(font)
        self.displayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayLabel.setObjectName("displayLabel")
        self.teamAgbF = QtWidgets.QGroupBox(self.centralwidget)
        self.teamAgbF.setGeometry(QtCore.QRect(40, 50, 41, 111))
        self.teamAgbF.setTitle("")
        self.teamAgbF.setFlat(True)
        self.teamAgbF.setObjectName("teamAgbF")
        self.foulsAtxtBx = QtWidgets.QTextEdit(self.teamAgbF)
        self.foulsAtxtBx.setGeometry(QtCore.QRect(0, 20, 41, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.foulsAtxtBx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.foulsAtxtBx.setFont(font)
        self.foulsAtxtBx.setAutoFillBackground(True)
        self.foulsAtxtBx.setReadOnly(True)
        self.foulsAtxtBx.setObjectName("foulsAtxtBx")
        self.foulsAdownBtn = QtWidgets.QPushButton(self.teamAgbF)
        self.foulsAdownBtn.setGeometry(QtCore.QRect(0, 90, 41, 16))
        self.foulsAdownBtn.setText("")
        self.foulsAdownBtn.setObjectName("foulsAdownBtn")
        self.foulsAupBtn = QtWidgets.QPushButton(self.teamAgbF)
        self.foulsAupBtn.setGeometry(QtCore.QRect(0, 60, 41, 31))
        self.foulsAupBtn.setObjectName("foulsAupBtn")
        self.squadABtn = QtWidgets.QPushButton(self.teamAgbF)
        self.squadABtn.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.squadABtn.setObjectName("squadABtn")
        self.teamBgbS = QtWidgets.QGroupBox(self.centralwidget)
        self.teamBgbS.setGeometry(QtCore.QRect(140, 60, 41, 101))
        self.teamBgbS.setTitle("")
        self.teamBgbS.setFlat(True)
        self.teamBgbS.setObjectName("teamBgbS")
        self.scoreBupBtn = QtWidgets.QPushButton(self.teamBgbS)
        self.scoreBupBtn.setGeometry(QtCore.QRect(0, 50, 41, 31))
        self.scoreBupBtn.setObjectName("scoreBupBtn")
        self.scoreBdownBtn = QtWidgets.QPushButton(self.teamBgbS)
        self.scoreBdownBtn.setGeometry(QtCore.QRect(0, 80, 41, 16))
        self.scoreBdownBtn.setText("")
        self.scoreBdownBtn.setObjectName("scoreBdownBtn")
        self.scoreBtxtBx = QtWidgets.QLabel(self.teamBgbS)
        self.scoreBtxtBx.setGeometry(QtCore.QRect(0, 0, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.scoreBtxtBx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.scoreBtxtBx.setFont(font)
        self.scoreBtxtBx.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.scoreBtxtBx.setLineWidth(1)
        self.scoreBtxtBx.setStyleSheet("background-color: black")
        self.scoreBtxtBx.setObjectName("scoreBtxtBx")
        self.timerSecUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerSecUpBtn.setGeometry(QtCore.QRect(170, 10, 21, 20))
        self.timerSecUpBtn.setObjectName("timerSecUpBtn")
        self.timerMinUpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerMinUpBtn.setGeometry(QtCore.QRect(80, 10, 21, 20))
        self.timerMinUpBtn.setObjectName("timerMinUpBtn")
        self.timerSecDownBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerSecDownBtn.setGeometry(QtCore.QRect(170, 30, 21, 20))
        self.timerSecDownBtn.setObjectName("timerSecDownBtn")
        self.timerMinDownBtn = QtWidgets.QPushButton(self.centralwidget)
        self.timerMinDownBtn.setGeometry(QtCore.QRect(80, 30, 21, 20))
        self.timerMinDownBtn.setObjectName("timerMinDownBtn")
        self.endMatchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.endMatchBtn.setEnabled(True)
        self.endMatchBtn.setGeometry(QtCore.QRect(100, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.endMatchBtn.setFont(font)
        self.endMatchBtn.setObjectName("endMatchBtn")
        self.endMatchBtn.setVisible(False)
        self.moveItemsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.moveItemsBtn.setGeometry(QtCore.QRect(120, 160, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.moveItemsBtn.setFont(font)
        self.moveItemsBtn.setObjectName("moveItemsBtn")
        self.teamAgbS = QtWidgets.QGroupBox(self.centralwidget)
        self.teamAgbS.setGeometry(QtCore.QRect(90, 60, 41, 101))
        self.teamAgbS.setTitle("")
        self.teamAgbS.setFlat(True)
        self.teamAgbS.setObjectName("teamAgbS")
        self.scoreAupBtn = QtWidgets.QPushButton(self.teamAgbS)
        self.scoreAupBtn.setGeometry(QtCore.QRect(0, 50, 41, 31))
        self.scoreAupBtn.setObjectName("scoreAupBtn")
        # self.scoreAtxtBx = QtWidgets.QTextEdit(self.teamAgbS)
        self.scoreAtxtBx = QtWidgets.QLabel(self.teamAgbS)
        self.scoreAtxtBx.setGeometry(QtCore.QRect(0, 0, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.scoreAtxtBx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.scoreAtxtBx.setFont(font)
        self.scoreAtxtBx.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.scoreAtxtBx.setLineWidth(1)
        self.scoreAtxtBx.setStyleSheet("background-color: black")
        #self.scoreAtxtBx.setReadOnly(True)
        self.scoreAtxtBx.setObjectName("scoreAtxtBx")
        self.scoreAdownBtn = QtWidgets.QPushButton(self.teamAgbS)
        self.scoreAdownBtn.setGeometry(QtCore.QRect(0, 80, 41, 16))
        self.scoreAdownBtn.setText("")
        self.scoreAdownBtn.setObjectName("scoreAdownBtn")
        self.teamBgbF = QtWidgets.QGroupBox(self.centralwidget)
        self.teamBgbF.setGeometry(QtCore.QRect(190, 50, 41, 111))
        self.teamBgbF.setTitle("")
        self.teamBgbF.setFlat(True)
        self.teamBgbF.setObjectName("teamBgbF")
        self.foulsBupBtn = QtWidgets.QPushButton(self.teamBgbF)
        self.foulsBupBtn.setGeometry(QtCore.QRect(0, 60, 41, 31))
        self.foulsBupBtn.setObjectName("foulsBupBtn")
        self.foulsBdownBtn = QtWidgets.QPushButton(self.teamBgbF)
        self.foulsBdownBtn.setGeometry(QtCore.QRect(0, 90, 41, 16))
        self.foulsBdownBtn.setText("")
        self.foulsBdownBtn.setObjectName("foulsBdownBtn")
        self.foulsBtxtBx = QtWidgets.QTextEdit(self.teamBgbF)
        self.foulsBtxtBx.setGeometry(QtCore.QRect(0, 20, 41, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.foulsBtxtBx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.foulsBtxtBx.setFont(font)
        self.foulsBtxtBx.setAutoFillBackground(True)
        self.foulsBtxtBx.setReadOnly(True)
        self.foulsBtxtBx.setObjectName("foulsBtxtBx")
        self.squadBBtn = QtWidgets.QPushButton(self.teamBgbF)
        self.squadBBtn.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.squadBBtn.setObjectName("squadBBtn")
        self.teamAgbA = QtWidgets.QGroupBox(self.centralwidget)
        self.teamAgbA.setGeometry(QtCore.QRect(40, 160, 81, 105))
        self.teamAgbA.setTitle("")
        self.teamAgbA.setObjectName("teamAgbA")
        self.teamAtimeBtn = QtWidgets.QPushButton(self.teamAgbA)
        self.teamAtimeBtn.setGeometry(QtCore.QRect(40, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teamAtimeBtn.setFont(font)
        self.teamAtimeBtn.setObjectName("teamAtimeBtn")
        self.teamAogBtn = QtWidgets.QPushButton(self.teamAgbA)
        self.teamAogBtn.setGeometry(QtCore.QRect(60, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teamAogBtn.setFont(font)
        self.teamAogBtn.setObjectName("teamAogBtn")
        self.teamArcBtn = QtWidgets.QPushButton(self.teamAgbA)
        self.teamArcBtn.setGeometry(QtCore.QRect(20, 20, 21, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.teamArcBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teamArcBtn.setFont(font)
        self.teamArcBtn.setObjectName("teamArcBtn")
        self.teamAycBtn = QtWidgets.QPushButton(self.teamAgbA)
        self.teamAycBtn.setGeometry(QtCore.QRect(0, 20, 21, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.teamAycBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.teamAycBtn.setFont(font)
        self.teamAycBtn.setAutoFillBackground(False)
        self.teamAycBtn.setObjectName("teamAycBtn")
        self.team_a_match_data_btn = QPushButton("Popraw", self.teamAgbA)
        self.team_a_match_data_btn.setGeometry(10, 80, 60, 21)
        self.team_a_match_data_btn.clicked.connect(partial(self.match_data_gb_show, self.match.team_a.id, self.match.id ))
        self.build_info_bar_gb()

        self.labelTeamA = QtWidgets.QLabel(self.teamAgbA)
        self.labelTeamA.setGeometry(QtCore.QRect(0, 0, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamA.setFont(font)
        self.labelTeamA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamA.setObjectName("labelTeamA")
        self.labelTeamA3L = QtWidgets.QLabel(self.teamAgbA)
        self.labelTeamA3L.setGeometry(QtCore.QRect(0, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.labelTeamA3L.setFont(font)
        self.labelTeamA3L.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamA3L.setObjectName("labelTeamA3L")
        self.teamBgbA = QtWidgets.QGroupBox(self.centralwidget)
        self.teamBgbA.setGeometry(QtCore.QRect(150, 160, 81, 105))
        self.teamBgbA.setTitle("")
        self.teamBgbA.setObjectName("teamBgbA")
        self.team_b_match_data_btn = QPushButton("Popraw", self.teamBgbA)
        self.team_b_match_data_btn.setGeometry(10, 80, 60, 21)
        self.team_b_match_data_btn.clicked.connect(partial(self.match_data_gb_show, self.match.team_b.id, self.match.id ))
        self.teamBtimeBtn = QtWidgets.QPushButton(self.teamBgbA)
        self.teamBtimeBtn.setGeometry(QtCore.QRect(40, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teamBtimeBtn.setFont(font)
        self.teamBtimeBtn.setObjectName("teamBtimeBtn")
        self.teamBogBtn = QtWidgets.QPushButton(self.teamBgbA)
        self.teamBogBtn.setGeometry(QtCore.QRect(60, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teamBogBtn.setFont(font)
        self.teamBogBtn.setObjectName("teamBogBtn")
        self.teamBrcBtn = QtWidgets.QPushButton(self.teamBgbA)
        self.teamBrcBtn.setGeometry(QtCore.QRect(20, 20, 21, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.teamBrcBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teamBrcBtn.setFont(font)
        self.teamBrcBtn.setObjectName("teamBrcBtn")
        self.teamBycBtn = QtWidgets.QPushButton(self.teamBgbA)
        self.teamBycBtn.setGeometry(QtCore.QRect(0, 20, 21, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 200, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.teamBycBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.teamBycBtn.setFont(font)
        self.teamBycBtn.setAutoFillBackground(False)
        self.teamBycBtn.setObjectName("teamBycBtn")
        self.labelTeamB = QtWidgets.QLabel(self.teamBgbA)
        self.labelTeamB.setGeometry(QtCore.QRect(0, 0, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamB.setFont(font)
        self.labelTeamB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamB.setObjectName("labelTeamB")
        self.labelTeamB3L = QtWidgets.QLabel(self.teamBgbA)
        self.labelTeamB3L.setGeometry(QtCore.QRect(0, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(22)
        self.labelTeamB3L.setFont(font)
        self.labelTeamB3L.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamB3L.setObjectName("labelTeamB3L")
        self.squad_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.squad_gb.setGeometry(QtCore.QRect(10, 200, 261, 271))
        self.squad_gb.setTitle("")
        self.squad_gb.setObjectName("squad_gb")
        self.squadTable = QtWidgets.QTableWidget(self.squad_gb)
        self.squadTable.setGeometry(QtCore.QRect(0, 0, 261, 251))
        self.squadTable.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.squadTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.squadTable.setObjectName("squadTable")
        self.squadTable.setColumnCount(6)
        self.squadTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.squadTable.setHorizontalHeaderItem(5, item)
        header = self.squadTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()



        self.close_squad_gbBtn = QtWidgets.QPushButton(self.squad_gb)
        self.close_squad_gbBtn.setGeometry(QtCore.QRect(0, 250, 261, 21))
        self.close_squad_gbBtn.setObjectName("close_squad_gbBtn")
        self.close_squad_gbBtn.raise_()
        self.squadTable.raise_()
        self.clearMatchActionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearMatchActionBtn.setGeometry(QtCore.QRect(120, 180, 31, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.clearMatchActionBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearMatchActionBtn.setFont(font)
        self.clearMatchActionBtn.setObjectName("clearMatchActionBtn")
        self.clearMatchActionBtn.raise_()
        self.timerPauseBtn.raise_()
        self.timerStartBtn.raise_()
        self.displayLabel.raise_()
        self.teamAgbF.raise_()
        self.teamBgbS.raise_()
        self.timerSecUpBtn.raise_()
        self.timerMinUpBtn.raise_()
        self.timerSecDownBtn.raise_()
        self.timerMinDownBtn.raise_()
        self.endMatchBtn.raise_()
        self.moveItemsBtn.raise_()
        self.teamAgbS.raise_()
        self.teamBgbF.raise_()
        self.teamAgbA.raise_()
        self.teamBgbA.raise_()
        self.squad_gb.raise_()
        Panel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Panel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 278, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        Panel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Panel)
        self.statusbar.setObjectName("statusbar")
        Panel.setStatusBar(self.statusbar)
        self.selectTeamsMenu = QtWidgets.QAction(Panel)
        self.selectTeamsMenu.setObjectName("selectTeamsMenu")
        self.scrapeTeamsMenu = QtWidgets.QAction(Panel)
        self.scrapeTeamsMenu.setObjectName("scrapeTeamsMenu")
        self.scrapeTableMenu = QtWidgets.QAction(Panel)
        self.scrapeTableMenu.setObjectName("scrapeTableMenu")
        self.menuMenu.addAction(self.selectTeamsMenu)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.scrapeTableMenu)
        self.menuMenu.addAction(self.scrapeTeamsMenu)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.select_teams()
        self.build_edit_team_gb()
        self.build_colors_gb()
        self.build_match_data_gb()
        self.build_change_player_gb()
        self.buttons_events_connect_const()
        self.retranslateUi(Panel)
        self.gb_setVisible()
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def buttons_events_connect_const(self):
        # zdarzenia dla przycisków
        self.scoreAupBtn.clicked.connect(self.on_scoreaupbtn_clicked)
        self.scoreAdownBtn.clicked.connect(self.on_scoreadownbtn_clicked)
        self.foulsAupBtn.clicked.connect(self.on_foulsaupbtn_clicked)
        self.foulsAdownBtn.clicked.connect(self.on_foulsadownbtn_clicked)
        self.teamAycBtn.clicked.connect(self.teamAycBtn_clicked)
        self.teamArcBtn.clicked.connect(self.teamArcBtn_clicked)
        self.teamAtimeBtn.clicked.connect(self.teamAtimeBtn_clicked)
        self.teamAogBtn.clicked.connect(self.own_goal_team_a)
        #
        self.scoreBupBtn.clicked.connect(self.on_scorebupbtn_clicked)
        self.scoreBdownBtn.clicked.connect(self.on_scorebdownbtn_clicked)
        self.foulsBupBtn.clicked.connect(self.on_foulsbupbtn_clicked)
        self.foulsBdownBtn.clicked.connect(self.on_foulsbdownbtn_clicked)
        self.teamBycBtn.clicked.connect(self.teamBycBtn_clicked)
        self.teamBrcBtn.clicked.connect(self.teamBrcBtn_clicked)
        self.teamBtimeBtn.clicked.connect(self.teamBtimeBtn_clicked)
        self.teamBogBtn.clicked.connect(self.own_goal_team_b)

        #
        # # self.teamBycBtn.clicked.connect(self.teamBycBtn_clicked)
        #
        self.timerStartBtn.clicked.connect(self.stopper_start)
        self.timerPauseBtn.clicked.connect(self.stopper_pause)
        self.second_half_btn.clicked.connect(self.second_half)
        self.timerMinUpBtn.clicked.connect(self.timer_min_up)
        self.timerSecUpBtn.clicked.connect(self.timer_sec_up)
        self.timerMinDownBtn.clicked.connect(self.timer_min_down)
        self.endMatchBtn.clicked.connect(self.end_match)
        self.timerSecDownBtn.clicked.connect(self.timer_sec_down)
        self.moveItemsBtn.clicked.connect(self.change_side)
        self.squadTable.itemSelectionChanged.connect(self.select_player)
        self.squadTable.cellDoubleClicked.connect(self.double_clicked_squadTable)
        self.close_squad_gbBtn.clicked.connect(self.close_squad_gb)
        self.clearMatchActionBtn.clicked.connect(self.clear_match_action)

        self.selectTeamsMenu.triggered.connect(self.select_teams_show)
        self.scrapeTeamsMenu.triggered.connect(self.scrape_all_players)
        self.scrapeTableMenu.triggered.connect(self.scrape_all_tables)
        self.teamList.itemDoubleClicked.connect(self.edit_team_show)
        self.select_team_a_btn.clicked.connect(self.set_team_a)
        self.select_team_b_btn.clicked.connect(self.set_team_b)
        # self.start_new_match_btn.clicked.connect(self.new_match)
        self.continue_match_btn.clicked.connect(self.continue_match)

    def buttons_events_connect_varia(self):
        self.squadABtn.clicked.connect(partial(self.squad_show, self.team_a.id))
        self.squadBBtn.clicked.connect(partial(self.squad_show, self.team_b.id))

    def buttons_events_disconnect_varia(self):
        # zdarzenia dla przycisków
        self.squadABtn.clicked.disconnect()
        self.squadBBtn.clicked.disconnect()

    # def set_match_team(self, ab, team_ab):
    #     if self.teamList.currentItem() != None:
    #         full_name = self.teamList.currentItem().text()
    #         for i, t in enumerate(all_teams):
    #             if t[1] == full_name:
    #                 # id = team[0]
    #                 # del self.team_ab
    #                 del team_ab
    #                 tm = team.Team(t[0])
    #                 team_ab = tm
    #                 #self.team_b = tm
    #                 self.buttons_events_disconnect_varia()
    #
    #                 self.retlanslate_team_info()
    #                 tm.tricot_color_divs("colors_b")
    #                 tm_txt = "team" + ab + ".txt"
    #                 self.match.save_as_txt(tm.sh_name, tm_txt)
    #                 print(tm.squad)
    #                 squad_info_bar = tm.name + " (" + tm.sh_name + ")  "
    #                 squad = tm.squad
    #                 squad = sorted(squad, key=lambda x: (x[3], x[14], x[13]))
    #                 for i in squad:  # 12 - imię; 13 - nazwisko
    #                     nr = i[14]
    #                     fname = i[12]
    #                     initial = fname[0:1]
    #                     last_name = i[13]
    #                     gk = ""
    #                     if i[3] == "Bramkarz":
    #                         gk = " (B)"
    #                     plr = [nr, initial, last_name, gk]
    #                     captain = ""
    #                     if i[17] == 1:
    #                         captain = " (K)"
    #
    #                     squad_info_bar += str(nr) + " " + initial + ". " + last_name + gk + captain + "  "
    #                 tm.squad_info_bar = squad_info_bar
    #                 print(squad_info_bar)

    def set_squad_info_bar(self, tm):
        squad_info_bar = tm.name + "   (" + tm.sh_name + ")   "
        squad = tm.squad
        squad = sorted(squad, key=lambda x: (x[3], x[14], x[13]))
        for i in squad:  # 12 - imię; 13 - nazwisko
            nr = i[14]
            fname = i[12]
            initial = fname[0:1]
            last_name = i[13]
            gk = ""
            if i[3] == "Bramkarz":
                gk = " (B)"
            plr = [nr, initial, last_name, gk]
            captain = ""
            if i[17] == 1:
                captain = " (K)"

            squad_info_bar += str(nr) + " " + initial + ". " + last_name + gk + captain + "   "
        tm.squad_info_bar = squad_info_bar

    def set_team_a(self):
        if self.teamList.currentItem() != None:
            full_name = self.teamList.currentItem().text()
            for i, t in enumerate(all_teams):
                if t[1] == full_name:
                    # id = team[0]
                    del self.team_a
                    del self.match.team_a
                    tm = team.Team(t[0])
                    self.match.team_a = tm
                    self.team_a = tm
                    self.buttons_events_disconnect_varia()

                    self.retlanslate_team_info()
                    tm.tricot_color_divs("colors_a")
                    self.match.save_as_txt(tm.sh_name, "teama.txt")
                    self.set_squad_info_bar(tm)
                    db_con.db_update_match_value("team_a", tm.id)
                    self.match.team_a_set_logo()
                    self.match.squad_divs()

    def set_team_b(self):
        if self.teamList.currentItem() != None:
            full_name = self.teamList.currentItem().text()
            for i, t in enumerate(all_teams):
                if t[1] == full_name:
                    # id = team[0]
                    del self.team_b
                    del self.match.team_b
                    tm = team.Team(t[0])
                    self.match.team_b = tm
                    self.team_b = tm
                    self.buttons_events_disconnect_varia()

                    self.retlanslate_team_info()
                    tm.tricot_color_divs("colors_b")
                    self.match.save_as_txt(tm.sh_name, "teamb.txt")
                    self.set_squad_info_bar(tm)
                    db_con.db_update_match_value("team_b", tm.id)
                    self.match.team_b_set_logo()
                    self.match.squad_divs()


    def select_team_a(self, tea):
        self.team_a = tea
        return self.team_a

    def select_team_b(self, teb):
        self.team_b = teb
        return self.team_b

    def make_match(self):
        self.match = match.Match(self.team_a, self.team_b, self.actual_match)
        self.match.last_saved_min = self.match.match_length
        self.match.last_saved_sec = 0
        self.move_items = False

    def end_match(self):
        db_con.db_update_match_actual_null()
        db_con.db_insert_new_match()
        self.actual_match = db_con.db_select_actual_match()
        self.team_a_id = self.actual_match[1]
        self.team_b_id = self.actual_match[2]


    def retranslateUi(self, Panel):

        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "MainWindow"))
        self.timerStartBtn.setText(_translate("Panel", "►"))
        self.timerPauseBtn.setText(_translate("Panel", " ▌▌"))
        self.displayLabel.setText(_translate("Panel", "00:00"))
        self.foulsAtxtBx.setHtml(_translate("Panel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.foulsAupBtn.setText(_translate("Panel", "▲"))
        self.squadABtn.setText(_translate("Panel", "Skład"))
        self.scoreBupBtn.setText(_translate("Panel", "▲"))
        self.timerSecUpBtn.setText(_translate("Panel", "▲"))
        self.timerMinUpBtn.setText(_translate("Panel", "▲"))
        self.timerSecDownBtn.setText(_translate("Panel", "▼"))
        self.timerMinDownBtn.setText(_translate("Panel", "▼"))
        self.endMatchBtn.setText(_translate("Panel", "KONIEC MECZU"))
        self.moveItemsBtn.setText(_translate("Panel", "<<>>"))
        self.scoreAupBtn.setText(_translate("Panel", "▲"))
#         self.scoreAtxtBx.setHtml(_translate("Panel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.foulsBupBtn.setText(_translate("Panel", "▲"))
        self.foulsBtxtBx.setHtml(_translate("Panel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.squadBBtn.setText(_translate("Panel", "Skład"))
        self.teamAtimeBtn.setText(_translate("Panel", "T"))
        self.teamAogBtn.setText(_translate("Panel", "S"))
        self.teamArcBtn.setText(_translate("Panel", "█"))
        self.teamAycBtn.setText(_translate("Panel", "█"))
        self.teamBtimeBtn.setText(_translate("Panel", "T"))
        self.teamBogBtn.setText(_translate("Panel", "S"))
        self.teamBrcBtn.setText(_translate("Panel", "█"))
        self.teamBycBtn.setText(_translate("Panel", "█"))
        self.squadTable.setSortingEnabled(True)
        item = self.squadTable.horizontalHeaderItem(0)
        item.setText(_translate("Panel", "nr"))
        item = self.squadTable.horizontalHeaderItem(1)
        item.setText(_translate("Panel", "imię"))
        item = self.squadTable.horizontalHeaderItem(2)
        item.setText(_translate("Panel", "nazwisko"))
        item = self.squadTable.horizontalHeaderItem(3)
        item.setText(_translate("Panel", ""))
        item = self.squadTable.horizontalHeaderItem(5)
        item.setText(_translate("Panel", ""))

        self.close_squad_gbBtn.setText(_translate("Panel", "Zamknij"))
        self.clearMatchActionBtn.setText(_translate("Panel", "X"))
        self.menuMenu.setTitle(_translate("Panel", "Menu"))
        self.selectTeamsMenu.setText(_translate("Panel", "Drużyny"))
        self.scrapeTableMenu.setText(_translate("Panel", "Pobierz tabele z nalffutsal.pl"))
        self.scrapeTeamsMenu.setText(_translate("Panel", "Pobierz drużyny z nalffutsal.pl"))

        self.time_display()



        self.retlanslate_team_info()

        self.squad_gb.setVisible(False)
        self.squadTable.verticalHeader().hide()
        self.squadTable.horizontalHeader().hide()
        self.squadTable.hideColumn(4)
        self.squadTable.setColumnWidth(4, 40)



        # for obj in gc.get_objects():
        #     if isinstance(obj, Ui_Pilot):
        #         print(obj)

    #####################
    # METODY DLA TEAM A #
    #####################

    # BRAMKI A UP
    def on_scoreaupbtn_clicked(self):
        self.match.score_a_up()
        self.scoreAtxtBx.setText(str(self.match.score_a))
        self.set_alignment()
        #self.scoreAtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        self.match.set_match_action(1)
        val = str(self.match.get_score_a())
        team_id = str(self.match.team_a.id)
        self.match.save_as_txt(val, 'bramki_a.txt')
        db_con.db_update_match_value("score_a", val)
        self.squad_show(team_id)
        self.gb_setVisible(self.squad_gb)



    # BRAMKI A DOWN
    def on_scoreadownbtn_clicked(self):
        self.match.score_a_down()
        self.scoreAtxtBx.setText(str(self.match.score_a))
        self.scoreAtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        val = str(self.match.get_score_a())
        self.match.save_as_txt(val, 'bramki_a.txt')
        db_con.db_update_match_value("score_a", val)

    # BRAMKA SAMOBÓJCZA TEAM A
    def own_goal_team_a(self):
        self.match.set_match_action(4)
        self.squad_show(self.team_b.id)
        self.gb_setVisible(self.squad_gb)


    # FAULE TEAM A UP
    def on_foulsaupbtn_clicked(self):
        self.match.fouls_a_up()
        self.fouls_a_display_and_save()

    def fouls_a_display_and_save(self):
        val = str(self.match.get_fouls_a())
        self.foulsAtxtBx.setText(str(val))
        self.foulsAtxtBx.setAlignment((QtCore.Qt.AlignCenter))
        db_con.db_update_match_value("fouls_a", val)
        self.match.save_both_fouls_a_versions()

    # FAULE TEAM A DOWN
    def on_foulsadownbtn_clicked(self):
        self.match.fouls_a_down()
        self.fouls_a_display_and_save()



    # ŻÓŁTA KARTKA TEAM A
    def teamAycBtn_clicked(self):
        self.match.set_match_action(2)
        self.squad_show(self.team_a.id)

    # CZERWONA KARTKA TEAM A
    def teamArcBtn_clicked(self):
        self.match.set_match_action(3)
        self.squad_show(self.team_a.id)

    # CZAS TEAM A
    def teamAtimeBtn_clicked(self):
        x = self.match.team_a.squad
        self.match.set_match_action(5)
        y = self.show_timeout_bar(x[0])
        self.match.save_as_txt(y, "akcja.txt")
        self.match.set_match_action(0)



    #####################
    # METODY DLA TEAM B #
    #####################

    # BRAMKI TEAM B UP

    # def on_scorebupbtn_clicked(self):
    #     self.match.score_b_up()
    #     self.scoreBtxtBx.setText(str(self.match.score_b))
    #     self.scoreBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
    #     self.match.save_as_txt(str(self.match.get_score_b()), 'bramki_b.txt')
    #     self.match.set_match_action(1)
    #     self.squad_show(self.team_b.id)

    def on_scorebupbtn_clicked(self):
        self.match.score_b_up()
        self.scoreBtxtBx.setText(str(self.match.score_b))
        self.scoreBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        self.match.set_match_action(1)
        val = str(self.match.get_score_b())
        team_id = str(self.match.team_b.id)
        self.match.save_as_txt(val, 'bramki_b.txt')
        db_con.db_update_match_value("score_b", val)
        self.squad_show(team_id)
        self.gb_setVisible(self.squad_gb)


    # BRAMKI TEAM B DOWN
    def on_scorebdownbtn_clicked(self):
        # self.match.score_b_down()
        # self.scoreBtxtBx.setText(str(self.match.score_b))
        # self.scoreBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        # self.match.save_as_txt(str(self.match.get_score_b()), 'bramki_b.txt')

        self.match.score_b_down()
        self.scoreBtxtBx.setText(str(self.match.score_b))
        self.scoreBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        val = str(self.match.get_score_b())
        self.match.save_as_txt(val, 'bramki_b.txt')
        db_con.db_update_match_value("score_b", val)

    # BRAMKA SAMOBÓJCZA TEAM B
    def own_goal_team_b(self):
        self.match.set_match_action(4)
        self.squad_show(self.team_a.id)
        self.gb_setVisible(self.squad_gb)


    # FAULE TEAM B UP
    def on_foulsbupbtn_clicked(self):
        self.match.fouls_b_up()
        self.fouls_b_display_and_save()
        # self.foulsBtxtBx.setText(str(self.match.fouls_b))
        # self.foulsBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        # self.match.save_as_txt(str(self.match.get_fouls_b()), 'fouls_b.txt')
        # self.match.save_as_symbol(self.match.get_fouls_b(), "●", 'faule_b.txt')
        #dbConnection.db_update_match('fouls_b', mecz.foulsB)

    # FAULE TEAM B DOWN
    def on_foulsbdownbtn_clicked(self):
        self.match.fouls_b_down()
        self.fouls_b_display_and_save()
        # self.foulsBtxtBx.setText(str(self.match.fouls_b))
        # self.foulsBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        # self.match.save_as_txt(str(self.match.get_fouls_b()), 'fouls_b.txt')
        # self.match.save_as_symbol(self.match.get_fouls_b(), "●", 'faule_b.txt')
        #dbConnection.db_update_match('fouls_b', mecz.foulsB)

    def fouls_b_display_and_save(self):
        self.foulsBtxtBx.setText(str(self.match.fouls_b))
        self.foulsBtxtBx.setAlignment((QtCore.Qt.AlignCenter))
        val = str(self.match.get_fouls_b())
        db_con.db_update_match_value("fouls_b", val)
        self.match.save_both_fouls_b_versions()

    # ŻÓŁTA KARTKA TEAM B
    def teamBycBtn_clicked(self):
        self.match.set_match_action(2)
        self.squad_show(self.team_b.id)

    # CZERWONA KARTKA TEAM B
    def teamBrcBtn_clicked(self):
        self.match.set_match_action(3)
        self.squad_show(self.team_b.id)

    # CZAS TEAM B
    def teamBtimeBtn_clicked(self):
        x = self.match.team_b.squad
        self.match.set_match_action(5)
        y = self.show_timeout_bar(x[0])
        self.match.save_as_txt(y, "akcja.txt")
        self.match.set_match_action(0)


    def squad_show(self, team_id):
        self.select_teams_gb.setVisible(False)
        self.edit_team_gb.setVisible(False)

        # squad = db_con.db_get_squad(str(team_id))

        if str(self.match.team_a.id) == str(team_id):
            squad = self.match.team_a.squad
        else:
            squad = self.match.team_b.squad
        self.squadTable.setRowCount(0)
        r = 0
        squad = sorted(squad, key=lambda x:(x[3], x[14], x[13]))
        for i, x in enumerate(squad):

            self.squadTable.insertRow(r)
            self.squadTable.setRowHeight(r, 10)
            if x[14] != 0:
                self.squadTable.setItem(r, 0, QTableWidgetItem(str(x[14])))
            else:
                self.squadTable.setItem(r, 0, QTableWidgetItem(""))
            self.squadTable.setItem(r, 1, QTableWidgetItem(x[12]))
            self.squadTable.setItem(r, 2, QTableWidgetItem(x[13]))
            if x[3] == "Bramkarz":
                self.squadTable.setItem(r, 3, QTableWidgetItem("(B)"))
            self.squadTable.setItem(r, 4, QTableWidgetItem(str(x[0])))
            if x[17] == "1":
                self.squadTable.setItem(r, 5, QTableWidgetItem("(K)"))

            r += 1


        if self.squad_gb.isVisible():
            self.squad_gb.setVisible(False)
        else:
            # self.squad_gb.setVisible(True)
            self.gb_setVisible(self.squad_gb)
    # WYBIERZ ZAWODNIKA
    def select_player(self):
        x = self.squadTable.currentRow()
        self.squadTable.selectRow(x)

    def double_clicked_squadTable(self):
        if self.match.match_action == 0:
            self.close_squad_gb()
        else:
            row = self.squadTable.currentRow()
            player_id = self.squadTable.item(row, 4)
            all_players = self.match.team_a.squad + self.match.team_b.squad
            for i in all_players:
                if str(i[0]) == player_id.text():
                    x = self.show_action_bar(i)
                    self.match.save_as_txt(x, "akcja.txt")
                    data = self.make_db_match_data(i)
                    db_con.db_update_match_data(data)
            self.match.set_match_action(0)
            self.close_squad_gb()

    def show_action_bar(self, player):
        act = self.match.match_actions[self.match.match_action - 1]
        if self.match.actual_min() == 0:
            min = ""
        else:
            min = str(self.match.actual_min()) + "'  "
        pla = player[12] + " " + player[13]
        if player[14] == 0:
            num = ""
        else:
            num = str(player[14])
        tea = player[2]
        bar = min + act[1] +"  " + num + " " + pla + " (" + tea + ")"
        return bar

    def make_db_match_data(self, player):
        min = str(self.match.actual_min())
        act = self.match.match_actions[self.match.match_action - 1]
        pla = player[0]
        match_id = self.match.id
        # teams_id = [self.match.team_a.id, self.match.team_b.id]
        team_id = player[18]
        if act[0] == 4:
            if team_id == self.match.team_a.id:
                team_id = self.match.team_b.id
            elif team_id == self.match.team_b.id:
                team_id = self.match.team_a.id
        data = [min, str(act[0]), pla, match_id, team_id]
        print(data)
        return data

    def show_timeout_bar(self, teamto):
        act = self.match.match_actions[self.match.match_action - 1]
        if self.match.actual_min() == 0:
            min = ""
        else:
            min = str(self.match.actual_min()) + "' "
        tea = teamto[2]
        bar = min + "   " + act[1] + "   " + tea
        return bar

    def clear_match_action(self):
        self.match.save_as_txt("", "akcja.txt")
        self.match.strikers_divs()

    def close_squad_gb(self):
        self.squadTable.clear()
        self.squad_gb.setVisible(False)

    ### metody obsługujące zegar ###
    def stopper_start(self):
        threading.Timer(1, self.time_flow).start()
        self.timerPauseBtn.setVisible(True)
        self.timerStartBtn.setVisible(False)
        self.movie_screen.setVisible(False)
        self.match.timer_on = True

    def stopper_pause(self):
        self.timerPauseBtn.setVisible(False)
        self.timerStartBtn.setVisible(True)
        self.movie_screen.setVisible(True)
        self.match.timer_on = False

    def timer_start(self):
        self.timerStartBtn.setVisible(False)
        self.match.timerOn = True
        self.timerPauseBtn.setVisible(True)
        t1 = threading.Thread(target=self.time_flow)
        t1.start()

    def time_flow(self):
        while self.match.timer_on == True:
            if self.match.last_saved_sec == 0:
                self.match.last_saved_sec = 59
                self.match.last_saved_min -= 1
                self.time_display()
                self.match.save_as_txt(str(self.match.actual_min()) + "'", "czasmin.txt")
                self.match.save_as_txt(str(self.match.score_a), "bramkia.txt")
                self.match.save_as_txt(str(self.match.score_b), "bramkib.txt")
            elif self.match.last_saved_min == 0 and self.match.last_saved_sec == 1:
                self.match.last_saved_sec = 0
                self.stopper_pause()
                self.time_display()
                self.timerStartBtn.setVisible(False)
                self.timerPauseBtn.setVisible(False)
                self.endMatchBtn.setVisible(True)
                self.match.save_as_txt(str(self.match.actual_min()) + "'", "czasmin.txt")
                self.match.strikers_divs()
            elif self.match.last_saved_min is int(self.match.match_length / 2) and self.match.last_saved_sec == 1:
                self.match.last_saved_sec = 0
                self.stopper_pause()
                self.time_display()
                self.match.save_as_txt("", "czasmin.txt")
                self.timerStartBtn.setVisible(False)
                self.timerPauseBtn.setVisible(False)
                self.second_half_btn.setVisible(True)
                self.match.strikers_divs()
            else:
                self.match.last_saved_sec -= 1
                self.time_display()
            time.sleep(1)

    def timer_min_up(self):
        if self.match.last_saved_min <= self.match.match_length - 1:
            self.match.last_saved_min += 1
        if self.match.last_saved_min == self.match.match_length:
            self.match.lastSavedSec = 0
        self.time_display()
        self.match.save_as_txt(str(self.match.actual_min()) + "'", "czasmin.txt")

    def timer_min_down(self):
        if self.match.last_saved_min > 0:
            self.match.last_saved_min -= 1
        self.time_display()
        self.match.save_as_txt(str(self.match.actual_min()) + "'", "czasmin.txt")

    def timer_sec_up(self):
        if self.match.last_saved_sec < 58 and not self.match.last_saved_min == self.match.match_length:
            self.match.last_saved_sec += 1
        else:
            self.match.lastSavedSec = 0
            if self.match.last_saved_min < self.match.match_length:
                self.match.last_saved_min += 1
        self.time_display()

    def timer_sec_down(self):
        if self.match.last_saved_sec > 0 and self.match.last_saved_min >= 0:
            self.match.last_saved_sec -= 1
        elif self.match.last_saved_sec == 0 and self.match.last_saved_min > 0 and not self.match.last_saved_min == self.match.last_saved_min:
            self.match.last_saved_min -= 1
        elif self.match.last_saved_sec == 0 and self.match.last_saved_min > 0 and self.match.last_saved_min == self.match.match_length:
            self.match.last_saved_min -= 1
            self.match.last_saved_sec = 59

        self.time_display()

    def time_display(self):
        x = str(self.match.last_saved_min)
        y = str(self.match.last_saved_sec)
        if len(x) == 1:
            x = '0' + x
        if len(y) == 1:
            y = '0' + y

        self.displayLabel.setText(x + ":" + y)
        self.displayLabel.setAlignment(QtCore.Qt.AlignCenter)

    ### zamiana stron ###
    def change_side(self):
        if self.move_items == True:
            self.move_items = False
            self.teamAgbF.move(40, 50)
            self.teamAgbS.move(90, 60)
            self.teamAgbA.move(40, 160)
            self.teamBgbS.move(140, 60)
            self.teamBgbF.move(190, 50)
            self.teamBgbA.move(150, 160)
        else:
            self.move_items = True
            self.teamAgbF.move(190, 50)
            self.teamAgbS.move(140, 60)
            self.teamAgbA.move(150, 160)
            self.teamBgbS.move(90, 60)
            self.teamBgbF.move(40, 50)
            self.teamBgbA.move(40, 160)

    def second_half(self):
        self.change_side()
        self.match.fouls_a = 0
        self.match.fouls_b = 0
        self.fouls_a_display_and_save()
        self.fouls_b_display_and_save()
        self.second_half_btn.setVisible(False)
        self.timerStartBtn.setVisible(True)

    # def show_select_team(self):
    #     self.all_teams = db_con.db_get_teams()
    #     self.select_teams_widget = select_teams.Select_teams(self.all_teams)
    #     self.select_teams_widget.show()

    def scrape_all_players(self):
        scraper = scrape.Scrape()
        teams = db_con.db_select_teams()
        for i, team in enumerate(teams):
            link = str(team[3])
            print(team[3])
            scraper.scrape_players(link)

    def scrape_all_tables(self):
        scraper = scrape.Scrape()
        scraper.scrape_table(scraper.adress_a, scraper.file_a)
        scraper.scrape_table(scraper.adress_b, scraper.file_b)

    def set_lead_color_team_a(self, nr):

        x = "#000000"
        return x

    def set_lead_color_team_b(self, nr):
        x = "#000000"
        # if nr == "1":
        #     x = self.team_b.col1
        # elif nr == "2":
        #     x = self.team_b.col2
        # else:
        #     x = self.team_b.col3
        return x

    def retlanslate_team_info(self):
        # for obj in gc.get_objects():
        #     if isinstance(obj, team.Team):
        #         print(obj.name)
        self.buttons_events_connect_varia()
        #self.col_l_a = self.set_lead_color_team_a(self.match.team_a.color_for_ui)
        self.col_l_a = self.match.team_a.color_for_ui
        #self.col_l_b = self.set_lead_color_team_b(self.match.team_b.color_for_ui)
        self.col_l_b = self.match.team_b.color_for_ui
        self.labelTeamB.setText(self.match.team_b.name)
        self.labelTeamB3L.setText(self.match.team_b.sh_name)
        self.labelTeamA.setText(self.match.team_a.name)
        self.labelTeamA3L.setText(self.match.team_a.sh_name)
        self.labelTeamA3L.setStyleSheet("QLabel#labelTeamA3L {color: " + self.match.team_a.color_for_ui + "}")
        self.labelTeamB3L.setStyleSheet("QLabel#labelTeamB3L {color: " + self.match.team_b.color_for_ui + "}")
        self.labelTeamA.setStyleSheet("QLabel#labelTeamA {color: " + self.match.team_a.color_for_ui + "}")
        self.labelTeamB.setStyleSheet("QLabel#labelTeamB {color: " + self.match.team_b.color_for_ui + "}")
        self.scoreAtxtBx.setText(str(self.match.score_a))
        self.scoreBtxtBx.setText(str(self.match.score_b))
        self.foulsAtxtBx.setText(str(self.match.fouls_a))
        self.foulsBtxtBx.setText(str(self.match.fouls_b))
        self.set_alignment()




    ### def group-boxa do edycji danych zespołu i wyboru drużyn
    def select_teams(self):
        self.select_teams_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.select_teams_gb.setGeometry(QtCore.QRect(10, 200, 261, 271))
        self.select_teams_gb.setTitle("")
        self.select_teams_gb.setObjectName("select_teams")
        # self.team_a_id = None
        # self.team_b_id = None
        self.select_team_a_btn = QPushButton("Team A", self.select_teams_gb)
        self.select_team_b_btn = QPushButton("Team B", self.select_teams_gb)
        self.start_new_match_btn = QPushButton("Mecz", self.select_teams_gb)
        self.continue_match_btn = QPushButton("Kontynuuj", self.select_teams_gb)
        self.select_team_a_btn.move(10, 205)
        self.select_team_b_btn.move(170, 205)
        self.start_new_match_btn.move(90, 205)
        self.continue_match_btn.move(90, 232)
        self.teamList = QListWidget(self.select_teams_gb)
        self.teamList.setGeometry(0, 0, 260, 200)
        self.select_teams_gb.setVisible(False)


    def select_teams_show(self):
        self.teamList.clear()
        self.list = all_teams
        for i, team in enumerate(self.list):
            self.teamList.addItem(team[1])
        self.teamList.sortItems()
        if self.squad_gb.isVisible():
            self.squad_gb.setVisible(False)
        # self.select_teams_gb.setVisible(True)
        self.gb_setVisible(self.select_teams_gb)

    def continue_match(self):
        self.select_teams_gb.setVisible(False)

    ### EDIT TEAM ###
    def build_edit_team_gb(self):
        self.edit_team_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.edit_team_gb.setGeometry(QtCore.QRect(0, 0, 275, 460))
        self.edit_team_gb.setAutoFillBackground(True)
        self.squad_table_edit = QtWidgets.QTableWidget(self.edit_team_gb)
        self.squad_table_edit.setGeometry(QtCore.QRect(0, 80, 275, 251))
        self.squad_table_edit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        #self.squad_table_edit.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.squad_table_edit.setObjectName("squad_table_edit")
        self.squad_table_edit.setColumnCount(7)
        self.squad_table_edit.setRowCount(0)
        header = self.squad_table_edit.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        # #header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.hide()
        self.squad_table_edit.hideColumn(5)
        v_header = self.squad_table_edit.verticalHeader()
        v_header.hide()
        self.tricot1_rb = QRadioButton(self.edit_team_gb)
        self.tricot1_rb.move(7, 10)
        self.tricot2_rb = QRadioButton(self.edit_team_gb)
        self.tricot2_rb.move(7, 35)
        self.tricot3_rb = QRadioButton(self.edit_team_gb)
        self.tricot3_rb.move(7, 60)
        self.tricots_button_group = QButtonGroup()
        self.tricots_button_group.addButton(self.tricot1_rb)
        self.tricots_button_group.addButton(self.tricot2_rb)
        self.tricots_button_group.addButton(self.tricot3_rb)
        self.save_colors_btn = QPushButton("Zapisz kolory", self.edit_team_gb)
        self.save_colors_btn.move(200, 55)
        # self.tricot1_btn = QPushButton("Strój 1", self.edit_team_gb)
        # self.tricot1_btn.move(25, 5)
        # self.tricot2_btn = QPushButton("Strój 2", self.edit_team_gb)
        # self.tricot2_btn.move(25, 30)
        # self.tricot3_btn = QPushButton("Znacznik", self.edit_team_gb)
        # self.tricot3_btn.move(25, 55)
        # self.tricot1_label = QLabel(self.edit_team_gb)
        # self.tricot1_label.setGeometry(50, 5, 25, 30)
        # self.tricot2_label = QLabel(self.edit_team_gb)
        # self.tricot2_label.setGeometry(50, 30, 25, 30)
        # self.tricot3_label = QLabel(self.edit_team_gb)
        # self.tricot3_label.setGeometry(50, 55, 25, 30)
        self.tricot1_colors_cb = QComboBox(self.edit_team_gb)
        self.tricot1_colors_cb.addItem("1")
        self.tricot1_colors_cb.addItem("2")
        self.tricot1_colors_cb.addItem("3")
        self.tricot1_color1_label = QLabel(self.edit_team_gb)
        self.tricot1_color2_label = QLabel(self.edit_team_gb)
        self.tricot1_color3_label = QLabel(self.edit_team_gb)
        self.tricot2_colors_cb = QComboBox(self.edit_team_gb)
        self.tricot2_colors_cb.addItem("1")
        self.tricot2_colors_cb.addItem("2")
        self.tricot2_colors_cb.addItem("3")
        self.tricot2_color1_label = QLabel(self.edit_team_gb)
        self.tricot2_color2_label = QLabel(self.edit_team_gb)
        self.tricot2_color3_label = QLabel(self.edit_team_gb)
        self.bibs_color_label = QLabel(self.edit_team_gb)
        self.ui_color_label = QLabel(self.edit_team_gb)

        self.tricot1_colors_cb.move(30, 6)
        self.tricot1_color1_label.setGeometry(65, 6, 20, 20)
        self.tricot1_color2_label.setGeometry(85, 6, 20, 20)
        self.tricot1_color3_label.setGeometry(105, 6, 20, 20)
        self.tricot2_colors_cb.move(30, 31)
        self.tricot2_color1_label.setGeometry(65, 31, 20, 20)
        self.tricot2_color2_label.setGeometry(85, 31, 20, 20)
        self.tricot2_color3_label.setGeometry(105, 31, 20, 20)

        self.bibs_color_label.setGeometry(65, 56, 20, 20)
        self.ui_color_label.setGeometry(105, 56, 20, 20)

        save_team_btn = QPushButton("Zapisz", self.edit_team_gb)
        save_team_btn.clicked.connect(self.edit_team_save)
        save_team_btn.move(5, 430)
        cancel_team_btn = QPushButton("Anuluj", self.edit_team_gb)
        cancel_team_btn.clicked.connect(self.edit_team_close)
        cancel_team_btn.move(80, 430)


        self.edit_team_gb.setVisible(False)

    def edit_team_show(self):

        team_id = None
        team_name = self.teamList.currentItem().text()
        for i, tm in enumerate(self.all_teams):
            if tm[1] == team_name:
                team_id = tm[0]
                self.edited_team = team.Team(team_id)
                squad = self.edited_team.players

                self.squad_table_edit.setRowCount(0)
                r = 0
                squad = sorted(squad, key=lambda x:(x[3], x[14], x[13]))
                print(squad)
                for i, x in enumerate(squad):

                    self.squad_table_edit.insertRow(r)
                    self.squad_table_edit.setRowHeight(r, 10)
                    if x[14] != 0:
                        self.squad_table_edit.setItem(r, 1, QTableWidgetItem(str(x[14])))
                    else:
                        self.squad_table_edit.setItem(r, 1, QTableWidgetItem(""))
                    self.squad_table_edit.setItem(r, 2, QTableWidgetItem(x[12]))
                    self.squad_table_edit.setItem(r, 3, QTableWidgetItem(x[13]))
                    checkbox_goal_keeper = QCheckBox()
                    self.squad_table_edit.setCellWidget(r, 4, checkbox_goal_keeper)
                    if x[3] == "Bramkarz":
                        checkbox_goal_keeper.setChecked(True)
                    self.squad_table_edit.setItem(r, 5, QTableWidgetItem(str(x[0])))
                    checkbox_squad = QCheckBox()
                    self.squad_table_edit.setCellWidget(r, 0, checkbox_squad)
                    # checkbox_squad.stateChanged.connect(self.checkbox_squad_state_changed)
                    if x[15] == 1:
                        checkbox_squad.setChecked(True)
                    else:
                        checkbox_squad.setChecked(False)
                    radio_button_captain = QRadioButton(self.squad_table_edit)
                    self.squad_table_edit.setCellWidget(r, 6, radio_button_captain)

                    if x[17] == 1:
                        radio_button_captain.setChecked(True)

                    r += 1

                self.set_tricot_rb(self.edited_team)
                self.tricot1_rb.toggled.connect(partial(self.select_tricot, self.edited_team, 1))
                self.tricot2_rb.toggled.connect(partial(self.select_tricot, self.edited_team, 2))
                self.tricot3_rb.toggled.connect(partial(self.select_tricot, self.edited_team, 3))
                #self.edited_team_id = team_id
                self.save_colors_btn.clicked.connect(partial(self.save_tricot_colors, self.edited_team))


                # if t.selected_tricot == 1:
                #     self.tricot1_rb.setChecked(True)
                # elif t.selected_tricot == 2:
                #     self.tricot2_rb.setChecked(True)
                # elif t.selected_tricot == 3:
                #     self.tricot3_rb.setChecked(True)
                # print('przed')
                # t = team.Team(team_id)
                # print('po')
                self.tricot1_colors_labels = [self.tricot1_color1_label, self.tricot1_color2_label, self.tricot1_color3_label]
                self.tricot2_colors_labels = [self.tricot2_color1_label, self.tricot2_color2_label, self.tricot2_color3_label]

                self.tricot1_colors_labels[0].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_1_colors[0])
                self.tricot1_colors_labels[1].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_1_colors[1])
                self.tricot1_colors_labels[2].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_1_colors[2])
                self.tricot2_colors_labels[0].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_2_colors[0])
                self.tricot2_colors_labels[1].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_2_colors[1])
                self.tricot2_colors_labels[2].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.tricot_2_colors[2])
                self.bibs_color_label.setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.bibs_color)
                self.bibs_color_label.mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 7)
                self.ui_color_label.setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % self.edited_team.color_for_ui)
                self.ui_color_label.mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 8)

                self.tricot1_colors_labels[0].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 1)
                self.tricot1_colors_labels[1].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 2)
                self.tricot1_colors_labels[2].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 3)
                self.tricot2_colors_labels[0].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 4)
                self.tricot2_colors_labels[1].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 5)
                self.tricot2_colors_labels[2].mouseDoubleClickEvent = partial(self.showColorDialog, self.edited_team, 6)


                self.tricot1_colors_cb.activated.connect(partial(self.set_colors_number, self.tricot1_colors_cb, self.tricot1_colors_labels))
                self.tricot2_colors_cb.activated.connect(partial(self.set_colors_number, self.tricot2_colors_cb, self.tricot2_colors_labels))

                self.get_colors_number(self.tricot1_colors_cb, self.edited_team, self.edited_team.tricot_1_colors)
                self.get_colors_number(self.tricot2_colors_cb, self.edited_team, self.edited_team.tricot_2_colors)
                self.set_colors_number(self.tricot1_colors_cb, self.tricot1_colors_labels)
                self.set_colors_number(self.tricot2_colors_cb, self.tricot2_colors_labels)
                self.tricot1_colors_cb.currentIndex()
        self.gb_setVisible(self.edit_team_gb)


    def disconnect_edit_team(self):
        self.tricot1_rb.disconnect()
        self.tricot2_rb.disconnect()
        self.tricot3_rb.disconnect()
        self.tricot1_colors_cb.disconnect()
        self.tricot2_colors_cb.disconnect()
        self.save_colors_btn.disconnect()


    def save_tricot_colors(self, ttt):
        if ttt.bibs_color == "":
            ttt.bibs_color = "#adeb31"
        ttt.home_colors_nr = self.set_colors_number(self.tricot1_colors_cb, self.tricot1_colors_labels)
        ttt.away_colors_nr = self.set_colors_number(self.tricot2_colors_cb, self.tricot2_colors_labels)
        ttt.setColorsNumber()


        db_con.db_update_colors(ttt.tricot_1_colors, ttt.tricot_2_colors, ttt.bibs_color, ttt.color_for_ui, ttt.id)

    def set_colors_number(self, combobox, labels):
        if combobox.currentText() == "1":
            labels[0].setVisible(True)
            labels[1].setVisible(False)
            labels[2].setVisible(False)
            return 1
        elif combobox.currentText() == "2":
            labels[0].setVisible(True)
            labels[1].setVisible(True)
            labels[2].setVisible(False)
            return 2
        elif combobox.currentText() == "3":
            labels[0].setVisible(True)
            labels[1].setVisible(True)
            labels[2].setVisible(True)
            return 3

    def get_colors_number(self, combobox, t, tricot):
        if t.getColorsNumber(tricot) == 3:
            combobox.setCurrentIndex(2)
        elif t.getColorsNumber(tricot) == 2:
            combobox.setCurrentIndex(1)
        elif t.getColorsNumber(tricot) == 1:
            combobox.setCurrentIndex(0)

    def showColorDialog(self, t, n, event):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            if n == 1:
                #self.tricot1_colors_labels[0].setStyleSheet("QWidget { background-color: %s }" % selected_color.name())
                t.tricot_1_colors[0] = selected_color.name()
                self.tricot1_colors_labels[0].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_1_colors[0])
            elif n == 2:
                #self.tricot1_colors_labels[1].setStyleSheet("QWidget { background-color: %s }" % selected_color.name())
                t.tricot_1_colors[1] = selected_color.name()
                self.tricot1_colors_labels[1].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_1_colors[1])
            elif n == 3:
                #self.tricot1_colors_labels[2].setStyleSheet("QWidget { background-color: %s }" % selected_color.name())
                t.tricot_1_colors[2] = selected_color.name()
                self.tricot1_colors_labels[2].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_1_colors[2])
            elif n == 4:
                #self.tricot2_colors_labels[0].setStyleSheet("QWidget { background-color: %s }" % selected_color.name())
                t.tricot_2_colors[0] = selected_color.name()
                self.tricot2_colors_labels[0].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_2_colors[0])
            elif n == 5:
                #self.tricot2_colors_labels[1].setStyleSheet("QWidget { background-color: %s }" % selected_color.name())
                t.tricot_2_colors[1] = selected_color.name()
                self.tricot2_colors_labels[1].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_2_colors[1])
            elif n == 6:
                t.tricot_2_colors[2] = selected_color.name()
                self.tricot2_colors_labels[2].setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.tricot_2_colors[2])
            elif n == 7:
                t.bibs_color = selected_color.name()
                self.bibs_color_label.setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.bibs_color)
            elif n == 8:
                t.color_for_ui = selected_color.name()
                self.ui_color_label.setStyleSheet("QWidget { background-color: %s; border: 1px solid black; }" % t.color_for_ui)



    def set_tricot_rb(self, t):
        if t.selected_tricot == 1:
            self.tricot1_rb.setChecked(True)
        elif t.selected_tricot == 2:
            self.tricot2_rb.setChecked(True)
        elif t.selected_tricot == 3:
            self.tricot3_rb.setChecked(True)

    def select_tricot(self, t, n):
        db_con.update_tricot(n, t.id)


    def edit_team_close(self):
        #del self.edited_team
        self.gb_setVisible(self.select_teams_gb)
        self.squad_table_edit.clear()
        self.disconnect_edit_team()

    ###############################
    #### WYBÓR KOLORÓW STROJÓW ####
    ###############################

    def build_colors_gb(self):
        self.colors_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.colors_gb.setGeometry(QtCore.QRect(0, 0, 275, 460))
        self.colors_gb.setAutoFillBackground(True)

    def edit_colors_show(self, team_id):
        # t = team.Team(team_id)
        #         # print('po')
        # self.tricot1_color1_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_1_colors[0])
        # self.tricot1_color2_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_1_colors[1])
        # self.tricot1_color3_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_1_colors[2])
        # self.tricot2_color1_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_2_colors[0])
        # self.tricot2_color2_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_2_colors[1])
        # self.tricot2_color3_label.setStyleSheet("QWidget { background-color: %s }" % t.tricot_2_colors[2])
        # self.ui_color_label.setStyleSheet("QWidget { background-color: %s }" % t.color_for_ui)
        self.gb_setVisible(self.colors_gb)

    def gb_setVisible(self, visible_gb=None):
        self.squad_gb.setVisible(False)
        self.edit_team_gb.setVisible(False)
        self.select_teams_gb.setVisible(False)
        self.colors_gb.setVisible(False)
        self.match_data_gb.setVisible(False)
        self.change_player_gb.setVisible(False)
        if visible_gb != None:
            visible_gb.setVisible(True)

    def build_match_data_gb(self):
        self.match_data_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.match_data_gb.setGeometry((QtCore.QRect(10, 200, 261, 271)))
        self.match_data_gb.setAutoFillBackground(True)
        self.match_data_table = QtWidgets.QTableWidget(self.match_data_gb)
        self.match_data_table.setGeometry(0, 30, 261, 211)
        self.match_data_table.setColumnCount(6)
        for i in range(0, self.match_data_table.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.match_data_table.setHorizontalHeaderItem(i, item)
            header = self.match_data_table.horizontalHeader()
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        self.match_data_table.verticalHeader().hide()
        self.match_data_table_add_btn = QPushButton("Dodaj", self.match_data_gb)
        self.match_data_table_add_btn.setGeometry(0, 243, 40, 25)
        self.match_data_table_edit_btn = QPushButton("Edytuj", self.match_data_gb)
        self.match_data_table_edit_btn.setGeometry(40, 243, 40, 25)
        self.match_data_table_del_btn = QPushButton("Usuń", self.match_data_gb)
        self.match_data_table_del_btn.setGeometry(80, 243, 40, 25)
        self.match_data_table_close_btn = QPushButton("Zamknij", self.match_data_gb)
        self.match_data_table_close_btn.setGeometry(120, 243, 60, 25)
        self.match_data_table_save_btn = QPushButton("Zapisz i zamknij", self.match_data_gb)
        self.match_data_table_save_btn.setGeometry(180, 243, 81, 25)

        ################################################
        # DISABLE MATCH_DATA_GROUPBOX'S UNUSED BUTTONS #
        self.match_data_table_add_btn.setEnabled(False)
        self.match_data_table_edit_btn.setEnabled(False)
        self.match_data_table_del_btn.setEnabled(False)
        self.match_data_table_save_btn.setEnabled(False)
        ################################################
        #self.gb_setVisible()
        #self.match_data_gb_show(self.match.team_a.id, self.match.id)

    def match_data_gb_show(self, team_id, match_id):
        print(team_id)
        match_teams_players = self.match.team_a.players + self.match.team_b.players
        data = db_con.db_select_match_data(team_id, match_id)
        self.match_data_table.clearContents()
        self.match_data_table.setRowCount(0)
        print("po setrowcount")
        row = 0
        for i in data:
            player_id = i[3]
            action_cb = QComboBox(self.match_data_table)
            action_cb.addItem("G")
            action_cb.addItem("Ż")
            action_cb.addItem("Cz")
            action_cb.addItem("S")
            self.match_data_table.insertRow(row)
            self.match_data_table.setRowHeight(row, 10)
            self.match_data_table.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.match_data_table.setCellWidget(row, 2, action_cb)
            if i[2] == 1:
                action_cb.setCurrentIndex(0)
            elif i[2] == 2:
                action_cb.setCurrentIndex(1)
            elif i[2] == 3:
                action_cb.setCurrentIndex(2)
            elif i[2] == 4:
                action_cb.setCurrentIndex(3)

            self.match_data_table.setItem(row, 3, QTableWidgetItem(str(i[1])))
            for j in match_teams_players:
                if str(player_id) == str(j[0]):
                    ini = j[12][0:1]
                    lname = j[13]
                    nr = str(j[14])
                    self.match_data_table.setItem(row, 1, QTableWidgetItem(str(i[3])))
                    self.match_data_table.setItem(row, 4, QTableWidgetItem(nr + " " + ini + ". " + lname))
            row += 1
            print(row)
        self.match_data_table.hideColumn(0)
        self.match_data_table.hideColumn(1)
        self.gb_setVisible(self.match_data_gb)
        self.edited_team_id = team_id
        self.match_data_table_edit_btn.clicked.connect(partial(self.change_player_gb_show, self.edited_team_id))
        self.match_data_table_close_btn.clicked.connect(self.gb_notVisible)
        self.match_data_table.itemDoubleClicked.connect(partial(self.change_player_gb_show, self.edited_team_id))
        # self.match_data_table_del_btn.clicked.connect(self.del_event)
        self.match_data_table.itemSelectionChanged.connect(self.select_event)

    def select_event(self):
        x = self.match_data_table.currentRow()
        self.match_data_table.selectRow(x)
        event_id = self.match_data_table.item(x, 0).text()
        self.match_data_table.itemSelectionChanged.disconnect()
        self.match_data_table.itemDoubleClicked.disconnect()
        self.match_data_table.itemDoubleClicked.connect(partial(self.change_player_gb_show, self.edited_team_id))
        self.match_data_table.itemSelectionChanged.connect(self.select_event)
        return event_id

    def gb_notVisible(self):
        self.gb_setVisible()

    def build_change_player_gb(self):
        self.change_player_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.change_player_gb.setGeometry((QtCore.QRect(10, 200, 261, 271)))
        self.change_player_gb.setAutoFillBackground(True)
        self.delete_player_btn = QPushButton("Usuń wpis", self.change_player_gb)
        self.delete_player_btn.setGeometry(25,5,210,21)
        self.close_gb_player_btn = QPushButton("Zamknij", self.change_player_gb)
        self.close_gb_player_btn.setGeometry(25,245,210,21)
        self.change_player_table = QtWidgets.QTableWidget(self.change_player_gb)
        self.change_player_table.setGeometry(0, 30, 261, 211)
        self.change_player_table.setColumnCount(2)
        for i in range(2):
            item = QtWidgets.QTableWidgetItem()
            self.change_player_table.setHorizontalHeaderItem(i, item)
            header = self.change_player_table.horizontalHeader()
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        self.change_player_table.verticalHeader().hide()
        self.change_player_table.horizontalHeader().hide()
        self.change_player_table.hideColumn(0)
        self.change_player_table.itemSelectionChanged.connect(self.select_player_change_row)
        self.change_player_table.itemDoubleClicked.connect(self.update_event_player)
        self.delete_player_btn.clicked.connect(self.delete_action)
        self.close_gb_player_btn.clicked.connect(self.close_gb_player)
        self.gb_setVisible()

    def close_gb_player(self):
        self.change_player_table.itemDoubleClicked.disconnect()
        self.change_player_table.itemDoubleClicked.connect(self.update_event_player)
        self.match_data_gb_show(self.edited_team_id, self.match.id)
        self.gb_setVisible(self.match_data_gb)

    # def messagebox_confirm_delete_event(self):
    #     self.msg = QMessageBox(self.centralwidget)
    #     self.msg.setIcon(QMessageBox.Warning)
    #
    #     self.msg.setText("Tej operacji nie da się cofnąć!")
    #     self.msg.setInformativeText("Czy usunąć")
    #     self.msg.setWindowTitle("Usuwanie wpisu")
    #     self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     self.msg.buttonClicked.connect(self.confirm_delete_event)
    #
    # def confirm_delete_event(self):
    #     self.delete_action()



    def select_player_change_row(self):
        row = self.change_player_table.currentRow()
        self.change_player_table.selectRow(row)

    def update_event_player(self):
        row_match_data = self.match_data_table.currentRow()
        event_id = self.match_data_table.item(row_match_data, 0).text()
        row_player_change = self.change_player_table.currentRow()
        player_id = self.change_player_table.item(row_player_change, 0).text()
        db_con.db_update_change_player(player_id, event_id)
        self.change_player_table.itemDoubleClicked.disconnect()
        self.change_player_table.itemDoubleClicked.connect(self.update_event_player)
        self.match_data_gb_show(self.edited_team_id, self.match.id)
        self.gb_setVisible(self.match_data_gb)

    def delete_action(self):
        row_match_data = self.match_data_table.currentRow()
        event_id = self.match_data_table.item(row_match_data, 0).text()
        db_con.db_delete_action(event_id)
        self.change_player_table.itemDoubleClicked.disconnect()
        self.change_player_table.itemDoubleClicked.connect(self.update_event_player)
        self.match_data_gb_show(self.edited_team_id, self.match.id)
        self.gb_setVisible(self.match_data_gb)

    def change_player_gb_show(self, team_id):
        if self.match_data_table.currentRow() != -1:
            row = self.match_data_table.currentRow()
            print('ponizej ten row')
            print(row)
            event_id = self.match_data_table.item(row, 0)
            self.change_player_table.setRowCount(0)
            if str(self.match.team_a.id) == str(team_id):
                squad = self.match.team_a.squad
            elif str(self.match.team_b.id) == str(team_id):
                squad = self.match.team_b.squad
            row = 0
            squad = sorted(squad, key=lambda x: (x[3], x[1]))
            for i in squad:
                self.change_player_table.insertRow(row)
                self.change_player_table.setItem(row, 0, QTableWidgetItem(str(i[0])))
                self.change_player_table.setItem(row, 1, QTableWidgetItem(str(i[14]) + " " + str(i[1])))
                print(str(i[1]))
                print(row)
                row += 1
            self.match_data_table_edit_btn.disconnect()
            self.gb_setVisible(self.change_player_gb)

    def del_event(self):
        if self.match_data_table.currentRow() != -1:
            x = self.match_data_table.currentRow()
            event_id = self.match_data_table.item(x, 0).text()
            db_con.db_delete_by_id("matches_data", event_id)
            # self.match_data_table_del_btn.clicked.disconnect()
            # self.match_data_table_del_btn.clicked.connect(self.del_event)

    def build_info_bar_gb(self):
        self.info_bar_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.info_bar_gb.setGeometry(10, 265, 261, 100)
        self.info_bar_cb = QtWidgets.QComboBox(self.info_bar_gb)
        self.info_bar_cb.setFixedWidth(261)
        text_list = db_con.db_select_info_bar_text()
        for i in text_list:
            self.info_bar_cb.addItem(str(i[0]))
        self.info_bar_txtln = QtWidgets.QLineEdit(self.info_bar_gb)
        self.info_bar_txtln.setGeometry(0, 25, 200, 21)
        self.info_bar_send_btn = QPushButton("Wyślij", self.info_bar_gb)
        self.info_bar_send_btn.setGeometry(201, 24, 60, 23)
        self.info_bar_send_btn.clicked.connect(self.info_bar_to_txt)
        self.info_bar_squad_send_btn = QPushButton("Skład", self.info_bar_gb)
        self.info_bar_squad_send_btn.setGeometry(5, 70, 60, 23)
        self.info_bar_squad_send_btn.clicked.connect(self.info_bar_squad_to_txt)
        self.info_bar_clear_btn = QPushButton("Kasuj", self.info_bar_gb)
        self.info_bar_clear_btn.setGeometry(196, 70, 60, 23)
        self.info_bar_clear_btn.clicked.connect(self.info_bar_clear)
        #self.info_bar_txtln_set_text(self.info_bar_cb.currentText().text)
        self.info_bar_cb.activated[str].connect(self.info_bar_txtln_set_text)


    def info_bar_txtln_set_text(self, text):
        self.info_bar_txtln.setText(text)
        # self.info_bar_txtln.adjustSize()

    def info_bar_to_txt(self):
        self.match.save_as_txt(self.info_bar_txtln.text(), "pasek.txt")

    def info_bar_squad_to_txt(self):
        squad_ab_info_bar = ""
        spc = "   ●●●     "
        self.set_squad_info_bar(self.match.team_a)
        self.set_squad_info_bar(self.match.team_b)
        squad_ab_info_bar = spc + self.match.team_a.squad_info_bar + spc + self.match.team_b.squad_info_bar
        self.match.save_as_txt(squad_ab_info_bar, "pasek.txt")

    def info_bar_clear(self):
        self.match.save_as_txt("", "pasek.txt")


#################################################################


    def edit_team_players_db_update(self):
        db_con.db_update_numbers(self.squad_table_edit)
        db_con.db_update_position(self.squad_table_edit)
        db_con.db_update_first_name(self.squad_table_edit)
        db_con.db_update_last_name(self.squad_table_edit)
        db_con.db_update_squad(self.squad_table_edit)
        db_con.db_update_captain(self.squad_table_edit)
        #del self.edited_team

    def edit_team_save(self):
        self.edit_team_players_db_update()
        self.edit_team_close()

    def checkbox_squad_state_changed(self):
        print(self.squad_table_edit.currentRow())
        print('cokolwiek')
#################################################################
    def set_alignment(self):
        self.scoreAtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreBtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        self.foulsAtxtBx.setAlignment(QtCore.Qt.AlignCenter)
        self.foulsBtxtBx.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)  # instancja aplikacji?

    all_teams = db_con.db_select_teams()
    # team_a_id = 205
    # team_b_id = 207
    # team_a = team.Team(team_a_id)
    # team_b = team.Team(team_b_id)

    # start_window = start_window.StartWindow(all_teams)
    # start_window.show()

    pilot = QtWidgets.QMainWindow() # instancja głównego okna programu?

    ui = Ui_Pilot()  # instancja klasy z pliku QDesignera :)
    # ui.select_team_a(team_a)
    # ui.select_team_b(team_b)
    # ui.make_match()
    ui.setupUi(pilot)  # wywołanie metody, która za argument przyjmuje obiekt z biblioteki PyQt5?
    pilot.show()  # wywołanie metody wyświetlającej okno

    #scraper = scrape.Scrape()
    #scraper.scrape_teams('http://nalffutsal.pl/?page_id=16', 'http://nalffutsal.pl/?page_id=36')
    #scraper.scrape_players("http://nalffutsal.pl/?sp_team=drug-ony")
    #scraper.scrape_players("http://nalffutsal.pl/?sp_team=enha")
    # TO WAŻNE !!! # colpic = colorpicker.ColorPicker()
    # TO WAŻNE !!! # colpic.show()

    sys.exit(app.exec_())

