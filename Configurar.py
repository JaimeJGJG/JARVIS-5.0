#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Configurar.py
#  
#  Copyright 2026 JaimeJG
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
#  Código atualizado em 23/07/2026
#
#


from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLineEdit, QComboBox
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QProcess
import sys

class JanelaConfigurar (QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.label_conf = QLabel(self)
		self.label_conf.setText("CONFIGURAÇÕES\nJ.A.R.V.I.S")
		#self.label_conf.setAlignment(Qt.AlignCenter)
		self.label_conf.move(10,5)
		self.label_conf.setStyleSheet('QLabel {font-family:Ubuntu;font-size:18px;color:#0000FF;font:bold}')
		self.label_conf.resize(155,50)
		
		self.label_digite = QLabel(self)
		self.label_digite.setText("Digite seu nome aqui:")
		self.label_digite.setAlignment(Qt.AlignCenter)
		self.label_digite.move(10,350)
		self.label_digite.setStyleSheet('QLabel {font-size:15px;color:gray;}')
		self.label_digite.resize(155,20)
		
		self.label_att = QLabel(self)
		self.label_att.setText('''
		As configurações ainda são poucas.
		Tudo está em fase de testes.
		Em breve vem novas funções.
		Atenciosamente: JG
		''')
		self.label_att.setAlignment(Qt.AlignCenter)
		self.label_att.move(5,110)
		self.label_att.setStyleSheet('QLabel {font-size:15px;color:white}')
		self.label_att.resize(400,100)
		
		self.label_aviso = QLabel(self)
		self.label_aviso.setText("-Alterações só funcionarão reiniciando o assistente-")
		self.label_aviso.setAlignment(Qt.AlignCenter)
		self.label_aviso.move(5,430)
		self.label_aviso.setStyleSheet('QLabel {font-size:10px;color:gray;}')
		self.label_aviso.resize(400,10)
		
		self.label_selvoz = QLabel(self)
		self.label_selvoz.setText("Estilo de voz:")
		self.label_selvoz.setAlignment(Qt.AlignCenter)
		self.label_selvoz.move(10,270)
		self.label_selvoz.setStyleSheet('QLabel {font-size:15px;color:gray;}')
		self.label_selvoz.resize(95,20)
		
		self.voz_sel = QComboBox(self)
		self.voz_sel.move(10,295)
		self.voz_sel.setStyleSheet('''
		QComboBox{
			border-style:solid;
			border-width:1px;
			border-color:blue;
			color:white;
			background-color:black;
			selection-color:white}
		QComboBox:item{
			color:white;
			selection-color:white;
			selection-background-color:blue;
			background-color:black}
		''')
		self.voz_sel.resize(90,30)
		self.voz_sel.addItem("VOZ_M1")
		self.voz_sel.addItem("VOZ_M2")
		self.voz_sel.addItem("VOZ_M3")
		self.voz_sel.addItem("VOZ_M4")
		self.voz_sel.addItem("VOZ_M5")
		self.voz_sel.addItem("VOZ_M6")
		self.voz_sel.addItem("VOZ_F1")
		self.voz_sel.addItem("VOZ_F2")
		self.voz_sel.addItem("VOZ_F3")
		self.voz_sel.currentIndexChanged.connect(self.vozbox)
		
		self.nome_input = QLineEdit(self)
		self.nome_input.move(10,380)
		self.nome_input.setStyleSheet('''
		QLineEdit{
			border-style:solid;
			border-width:1px;
			border-color:blue;
			selection-color:white;
			selection-background-color:blue;
			color:white; font-size:20px}
		''')
		self.nome_input.resize(380,40)
		self.nome_input.setAlignment(Qt.AlignCenter)
		
		botao_fechar = QPushButton("",self)
		botao_fechar.move(370,10)
		botao_fechar.resize(20,20)
		botao_fechar.setStyleSheet("background-image : url(Imagens//Fechar.png);border-radius: 15px;") 
		botao_fechar.clicked.connect(self.fechartudo)
		
		botao_cancelar = QPushButton("CANCELAR",self)
		botao_cancelar.move(10,455)
		botao_cancelar.setStyleSheet('''
		QPushButton{
			border-style:solid;
			border-width:1px;
			font-size:20px;
			border-color:blue;
			color:blue}
		''')
		botao_cancelar.resize(105,30)
		botao_cancelar.clicked.connect(self.fechartudo)
		
		botao_padrao = QPushButton("PADRÃO",self)
		botao_padrao.move(148,455)
		botao_padrao.setStyleSheet('QPushButton {border-style:solid; border-width:1px; font-size:20px; border-color:blue; color:blue}')
		botao_padrao.resize(105,30)
		botao_padrao.clicked.connect(self.padrao)
		
		botao_concluir = QPushButton("CONCLUIR",self)
		botao_concluir.move(285,455)
		botao_concluir.setStyleSheet('QPushButton {border-style:solid; border-width:1px; font-size:20px; border-color:blue; color:blue}')
		botao_concluir.resize(105,30)
		botao_concluir.clicked.connect(self.salvarnome)
		
		self.CarregarJanela()
		
	def CarregarJanela(self):
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setGeometry(50,50,400,500)
		self.setMinimumSize(400, 500)
		self.setMaximumSize(400, 500)
		self.setWindowOpacity(0.95) 
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setStyleSheet("background-color: black")
		self.setWindowIcon(QtGui.QIcon('Imagens//ICONE_CONFIGURAR.png'))
		self.setWindowTitle("CONFIGURAR")
		self.show()
	
	def salvarnome(self):
		nome = self.nome_input.text()
		with open('Dados//Nome.txt', 'w') as nomeusr:
			nomeusr.write(nome)
		print('Nome > ' +nome +' < configurado com sucesso...')
	
	def vozbox(self):
		selvoz = self.voz_sel.currentText()
		print(selvoz +' selecionada...')
		setvozdic = {
			'VOZ_M1': 'pt-br+m1',
			'VOZ_M2': 'pt-br+m2',
			'VOZ_M3': 'pt-br+m3',
			'VOZ_M4': 'pt-br+m4',
			'VOZ_M5': 'pt-br+m5',
			'VOZ_M6': 'pt-br+m6',
			'VOZ_F1': 'pt-br+f1',
			'VOZ_F2': 'pt-br+f2',
			'VOZ_F3': 'pt-br+f3'}
		vozdic = setvozdic[selvoz]
		with open('Dados//Voz.txt','w') as vozdef:
			vozdef.write(vozdic)
	
	def padrao(self):
		with open('Dados//Voz.txt','w') as vozdef:
			vozdef.write('pt-br+m3')
			print('Voz definida para pt+m3')
		with open('Dados//Nome.txt', 'w') as nomeusr:
			nomeusr.write('USUÁRIO')
			print('Nome padrão "USUÁRIO" definido')
		
	
	def fechartudo(self):
		print('botao fechar presionado')
		sys.exit()
	
	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
    
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()
	
aplicacao = QApplication(sys.argv)
j = JanelaConfigurar()
sys.exit(aplicacao.exec_())

		
		
		
		
		
		
		
		
		
		
		
		
		
		
