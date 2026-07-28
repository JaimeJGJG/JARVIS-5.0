#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  JANELA.py
#  
#  Copyright 2026 JaimeJGJG
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
#
#
#



from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QProcess
import sys
import datetime
import psutil
import time
import os



class Janela (QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.label_gif = QLabel(self)
		self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
		self.label_gif.move(0,0)
		self.label_gif.resize(400,300)
		self.movie = QMovie("Imagens//FundoAnimado.gif")
		self.label_gif.setMovie(self.movie)
		self.movie.start()

		self.label_jarvis = QLabel(self)
		self.label_jarvis.setText("J.A.R.V.I.S")
		self.label_jarvis.setAlignment(QtCore.Qt.AlignCenter)
		self.label_jarvis.move(0,0)
		self.label_jarvis.setStyleSheet('QLabel {font-family:Ubuntu;font:bold;font-size:15px;color:#2F00FF}')
		self.label_jarvis.resize(400,300)

		self.label_cpu = QLabel(self)
		self.label_cpu.setText("Uso da CPU: 32%")
		self.label_cpu.move(8,270)
		self.label_cpu.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_cpu.resize(135,20)
		cpu = QTimer(self)
		cpu.timeout.connect(self.MostrarCPU)
		cpu.start(1000)

		self.label_cputemp = QLabel(self)
		self.label_cputemp.setText("Temperatura: 32°")
		self.label_cputemp.move(8,250)
		self.label_cputemp.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_cputemp.resize(131,20)
		tempc = QTimer(self)
		tempc.timeout.connect(self.MostrarTMP)
		tempc.start(1000)

		self.label_assv = QLabel(self)
		self.label_assv.setText("Assistente Virtual")
		self.label_assv.move(5,5)
		self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#0000ff}')
		self.label_assv.resize(200,20)

		self.label_version = QLabel(self)
		self.label_version.setText("Versão Alpha 5.0.8")
		self.label_version.setAlignment(QtCore.Qt.AlignCenter)
		self.label_version.move(260,270)
		self.label_version.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_version.resize(131,20)

		self.label_cb = QLabel(self)
		self.label_cb.setText("created by ")
		self.label_cb.setAlignment(QtCore.Qt.AlignRight)
		self.label_cb.move(285,250)
		self.label_cb.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_cb.resize(80,20)
		
		self.label_JG = QLabel(self)
		self.label_JG.setText("JG")
		self.label_JG.setAlignment(QtCore.Qt.AlignRight)
		self.label_JG.move(305,250)
		self.label_JG.setStyleSheet('QLabel {font:bold;font-size:14px;color:#0000ff}')
		self.label_JG.resize(80,20)

		data =  QDate.currentDate()
		datahoje = data.toString('dd/MM/yyyy')
		self.label_data = QLabel(self)
		self.label_data.setText(datahoje)
		self.label_data.setAlignment(QtCore.Qt.AlignCenter)
		self.label_data.move(5,25)
		self.label_data.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_data.resize(80,20)
		  
		self.label_horas = QLabel(self)
		self.label_horas.setText("22:36:09")
		self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
		self.label_horas.move(0,45)
		self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		self.label_horas.resize(71,20)
		horas = QTimer(self)
		horas.timeout.connect(self.MostrarHorras)
		horas.start(1000)
		
		botao_lista = QPushButton("",self)
		botao_lista.move(310,8)
		botao_lista.resize(21,21)
		botao_lista.setStyleSheet("background-image : url(Imagens//Lista.png);border-radius: 0px;")
		botao_lista.clicked.connect(self.MostrarLista)
		
		botao_config = QPushButton("",self)
		botao_config.move(340,8)
		botao_config.resize(21,21)
		botao_config.setStyleSheet("background-image : url(Imagens//Config.png);border-radius: 0px;")
		botao_config.clicked.connect(self.Configurar)

		botao_fechar = QPushButton("",self)
		botao_fechar.move(370,8)
		botao_fechar.resize(21,21)
		botao_fechar.setStyleSheet("background-image : url(Imagens//Fechar.png);border-radius: 0px;") 
		botao_fechar.clicked.connect(self.fechartudo)

		self.CarregarJanela()
		self.iniciar_assistente()
		
	def CarregarJanela(self):
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setGeometry(50,50,400,300)
		self.setMinimumSize(400, 300)
		self.setMaximumSize(400, 300)
		self.setWindowOpacity(0.97) 
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		#self.setStyleSheet("background-color: black")
		self.setWindowIcon(QtGui.QIcon('Imagens//ICONE_JARVIS.png'))
		self.setWindowTitle("J.A.R.V.I.S")
		self.show()

	def fechartudo(self):
		print('botao fechar presionado')
		os.system('killall Assistente')
		sys.exit()
	
	def MostrarLista(self):
		self.listac = QProcess()
		self.listac.start("./ListaC")
		
	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
    
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def MostrarHorras(self):
		hora_atual = QTime.currentTime()
		label_time = hora_atual.toString('hh:mm:ss')
		self.label_horas.setText(label_time)

	def MostrarTMP(self):
		tempcpu = psutil.sensors_temperatures()
		cputemp = tempcpu['coretemp'][0]
		temperaturacpu = cputemp.current
		cputempint = "{:.0f}".format(float(temperaturacpu))
		self.label_cputemp.setText("Temperatura: " +cputempint +"°")
		if temperaturacpu <= 59:
			self.label_cputemp.setStyleSheet('QLabel {font-size:14px;color:#0000ff}')
		if temperaturacpu >= 60:
			self.label_cputemp.setStyleSheet('QLabel {font-size:14px;color:#FF0000}')
	
	def MostrarCPU(self):
		usocpu =  str(psutil.cpu_percent())
		self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
	
	def Configurar(self):
		self.confg = QProcess()
		self.confg.start("./Configurar")
		self.confg.finished.connect(self.fechartudo)
		
	def iniciar_assistente(self):
		self.p = QProcess()
		self.p.start("./Assistente")
		self.p.finished.connect(self.fechartudo)

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())









