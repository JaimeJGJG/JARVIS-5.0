#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Assistente.py
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


from vosk import Model, KaldiRecognizer
from plyer import notification
from requests import get
from playsound3 import playsound
from CPN import contas
import xdotool
import operator
import os
import pyaudio
import pyttsx3
import sys
import subprocess
import datetime
import psutil
import speedtest
import webbrowser
import json
import requests
import time
import wikipedia
import random

def SomCarregamento():
	playsound("Audio//LOAD.mp3")

SomCarregamento()

def SomInicial():
	playsound("Audio//START.mp3")

with open('Dados//Voz.txt', 'r') as setvozes:
	lervoz = setvozes.read()
	lervozes = str(lervoz)
	speaker=pyttsx3.init()
	speaker.setProperty('voice', lervozes)
	rate = speaker.getProperty('rate')
	speaker.setProperty('rate', rate-41)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2000)
stream.start_stream()

def resposta(audio):
	subprocess.run(['notify-send', 'ASSISTENTE', audio, '-t', '5000'])
	stream.stop_stream()
	print('ASSISTENTE: ' + audio)
	speaker.say(audio)
	speaker.runAndWait()
	stream.start_stream()
	pyaudio_buffer_length = stream.get_read_available()
	if pyaudio_buffer_length > 0:
		stream.read(pyaudio_buffer_length, exception_on_overflow=False)

model = Model("PTBR")
rec = KaldiRecognizer(model, 16000)

def notificar(textos):
	subprocess.run(['notify-send','ASSISTENTE',textos,'-t','5000'])

def horario():
	from datetime import datetime
	horariodic = {
		'00':'0',
		'01':'1',
		'02':'2',
		'03':'3',
		'04':'4',
		'05':'5',
		'06':'6',
		'07':'7',
		'08':'8',
		'09':'9'}
	hora = datetime.now()
	try:
		try:
			try:
				horas = horariodic[hora.strftime('%H')]
				minutos = horariodic[hora.strftime('%M')]
			except:
				horas = hora.strftime('%H')
				minutos = horariodic[hora.strftime('%M')]
		except:
			horas = horariodic[hora.strftime('%H')]
			minutos = hora.strftime('%M')
	except:
		horas = hora.strftime('%H')
		minutos = hora.strftime('%M')
	Horarios = int(hora.hour)
	if Horarios >= 0 and Horarios < 12:
		resposta('Agora são ' +horas +' e '+minutos +' da manhã')

	elif Horarios >= 12 and Horarios < 18:
		resposta('Agora são ' +horas +' e '+minutos +' da tarde')

	elif Horarios >= 18 and Horarios != 0:
		resposta('Agora são ' +horas +' e '+minutos +' da noite')

def datahoje():
	from datetime import date
	dataatual = date.today()
	diassemana = ('Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo')
	meses = ('Zero','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
	resposta("Hoje é " +diassemana[dataatual.weekday()])
	diatexto = '{} de '.format(dataatual.day)
	mesatual = (meses[dataatual.month])
	datatexto = dataatual.strftime(" de %Y")
	resposta('Dia '+diatexto +mesatual +datatexto)

def bateria():
	try:
		bateria = psutil.sensors_battery()
		carga = bateria.percent
		bp = str(bateria.percent)
		bpint = "{:.0f}".format(float(bp))
		resposta("A bateria está em:" +bpint +'%')
		if carga <= 20:
			resposta('Ela está em nivel crítico')
			resposta('Por favor, coloque o carregador')
		elif carga == 100:
			resposta('Ela está totalmente carregada')
			resposta('Retire o carregador da tomada')
	except:
		resposta('Desculpa')
		resposta('Seu dispositivo atual não está usando bateria')
		resposta('Por isso é impossivel informar a quantidade de carga')

def cpu ():
	usocpuinfo = str(psutil.cpu_percent())
	usodacpu  = "{:.0f}".format(float(usocpuinfo))
	resposta('O uso do processador está em ' +usodacpu +'%')

def temperaturadacpu():
	tempcpu = psutil.sensors_temperatures()
	cputemp = tempcpu['coretemp'][0]
	temperaturacpu = cputemp.current
	cputempint = "{:.0f}".format(float(temperaturacpu))
	if temperaturacpu >= 20 and temperaturacpu < 40:
		resposta('Estamos trabalhado em um nível agradavel')
		resposta('A temperatura está em ' +cputempint +'°')
    
	elif temperaturacpu >= 40 and temperaturacpu < 58:
		resposta('Estamos operando em nivel rasoável')
		resposta('A temperatura é de ' +cputempint +'°')
    
	elif temperaturacpu >= 58 and temperaturacpu < 70:
		resposta('A temperatura da CPU está meio alta')
		resposta('Algum processo do sistema está causando aquecimento')
		resposta('Fique de olho')
		resposta('A temperatura está em ' +cputempint +'°')
    
	elif temperaturacpu >= 70 and temperaturacpu != 80:
		resposta('Atenção')
		resposta('Temperatura de ' +cputempint +'°')
		resposta('Estamos em nivel crítico')
		resposta('Desligue o sistema imediatamente')

def BoasVindas():
	Horario = int(datetime.datetime.now().hour)
	if Horario >= 0 and Horario < 6:
		resposta('Bom dia')
		time.sleep(0.1)
		resposta('Acordou cedo hoje')
	
	elif Horario >= 6 and Horario < 12:
		resposta('Bom dia')

	elif Horario >= 12 and Horario < 18:
		resposta('Boa tarde')

	elif Horario >= 18 and Horario != 0:
		resposta('Boa noite')
		
def Localização():
	try:
		resposta('Rastreando sua localização')
		resposta('Aguarde')
		url = 'https://ipinfo.io/json'
		apijson = requests.get(url)
		apijson.raise_for_status()
		dados = apijson.json()
		cidade = dados.get('city')
		estado = dados.get('region')
		resposta('Sua localização aproximada é '+cidade +', ' +estado +', Brasil')
		resposta('Os dados podem não ser exatos')
		
	except:
		resposta('Não consegui encontrar sua localização')
		resposta('Houve um problema com o fluxo de rede')

def Clima():
	try:
		resposta('OK. Aguarde')
		urlL = 'https://ipinfo.io/json'
		apijson = requests.get(urlL)
		apijson.raise_for_status()
		dados = apijson.json()
		cidade = dados.get('city')
		resposta('Verificando o clima para o local aproximado de: ' +cidade)
		urlC = f"https://wttr.in/{cidade}?format=%t %w %h %p"
		respost = requests.get(urlC)
		respost.raise_for_status()
		dadosc = respost.text
		partes = dadosc.split(' ')
		if len(partes) == 4:
			temperatura = partes[0]
			vento = partes[1]
			umidade = partes[2]
			preci = partes[3]
			precipit =preci.replace("mm", "")
			temp = ''.join(filter(str.isdigit, temperatura))
			vent = ''.join(filter(str.isdigit, vento))
			precipitacao ="{:.0f}".format(float(precipit))
			resposta('A temperatura é de: ' +temp +'°')
			resposta('A velocidade do vento está em: ' +vent +' quilômetros por hora')
			resposta('A umidade é: ' +umidade)
			resposta('E a precipitação de chuva é de: ' +precipitacao +' milimetros')
	except:
		resposta('Erro na aquisiçao do clima.')


def TesteInternet(url="http://www.google.com"):
	try:
		response = requests.get(url, timeout=5)
		if response.status_code == 200:
			resposta('Pelos meus testes')
			resposta('A conexão com a internet está funcionando.')
		else:
			resposta(f"Falha na conexão. Código de status: {response.status_code}")	
	except requests.ConnectionError:
		resposta('A conexão com à internet não está funcionando.')
		resposta('Verifique se os cabos ou o Wi-Fi estão conectados')
	except requests.Timeout:
		resposta('A requisição expirou. Verifique sua conexão.')

def VelocidadeInternet():
	resposta('Ok, verificando a velocidade da internet')
	resposta('Aguarde até eu terminar os testes.')
	try:
		st = speedtest.Speedtest()
		st.get_best_server()
		download_speed = st.download() / 1_000_000
		upload_speed = st.upload() / 1_000_000
		ping = st.results.ping
		baixar = "{:.0f}".format(float(download_speed))
		enviar = "{:.0f}".format(float(upload_speed))
		pingar = "{:.0f}".format(float(ping))
		resposta('A velocidade de download está em: ' +baixar +' mega')
		resposta('A velocidade de upload é de: ' +enviar +' mega')
		resposta('E o ping da conexão é: ' +pingar +' milissegundos')
	except:
		resposta('Erro no teste de conexão')

def TocarMusica():
	resposta('Ok')
	resposta('Reproduzindo música')
	resposta('Aguarde')
	with open('Dados//RepMusic.txt', 'r') as lerrep:
		lendo = lerrep.read().strip()
		leitura = str(lendo)
		if leitura == 'Deezer':
			webbrowser.open('https://www.deezer.com/br')
		elif leitura == 'Spotify':
			webbrowser.open('https://www.spotify.com/br')
		elif leitura == 'Apple Music':
			webbrowser.open('https://music.apple.com/br/new')
		time.sleep(20)
		subprocess.run(['xdotool','key','space']) 
	
def NomeMusica():
	try:
		resultado = subprocess.run(['playerctl','metadata','--format','{{ title }}'], capture_output = True, text = True, check = True)
		info_musica = resultado.stdout.strip()
		resultadoart = subprocess.run(['playerctl','metadata','--format','{{ artist }}'], capture_output = True, text = True, check = True)
		info_art = resultadoart.stdout.strip()
		resposta('A música que está tocando é: ' + info_musica)
		resposta('Do artista: ' + info_art)
	except:
		resposta('Erro ao procurar o nome da música')
		return None

def voltadez():
	resposta('Voltando 10 faixas')
	for i in range(11):
		subprocess.run(['xdotool','key','XF86AudioPrev'])
		time.sleep(0.4)

def avancadez():
	resposta('Avançando 10 músicas')
	for i in range(10):
		subprocess.run(['xdotool','key','XF86AudioNext'])
		time.sleep(0.3)

def Volumefixo(porcentagem_alvo):
	valor = max(0, min(100, porcentagem_alvo))
	valor_decimal = valor / 100
	subprocess.run(['wpctl','set-volume','@DEFAULT_AUDIO_SINK@',f'''{valor_decimal:.2f}'''])

def AteMais():
	Horario = int(datetime.datetime.now().hour)
	if Horario >= 0 and Horario < 6:
		resposta('Tenha uma ótima madrugada')
		resposta('E um excelente dia')
	
	elif Horario >= 6 and Horario < 12:
		resposta('Tenha um ótimo dia')

	elif Horario >= 12 and Horario < 18:
		resposta('Tenha uma ótima tarde')

	elif Horario >= 18 and Horario != 0:
		resposta('Boa noite')

def NomeUsuario():
	try:
		with open('Dados//Nome.txt', 'r') as lernome:
			leituras = lernome.read()
			nomeuser = str(leituras)
			resposta("Olá "+nomeuser)
	except:
		resposta('Erro no arquivo de nome do usuário')
		resposta('Por favor mantenha seu nome com aspas')
		resposta('E não troque o nome do arquivo')
	
def inicialize():
	try:
		with open('Dados//Inicio.txt', 'r') as ler:
			lendo = ler.read()[0]
			leitura = str(lendo)
			if leitura == '0':
				BoasVindas()
				resposta('Primeira inicialização realizada com sucesso')
				resposta('Meu nome é JARVIS')
				resposta('Apartir de agora vou ser seu novo assistente virtual')
				resposta('Estou aqui para atender seus comandos')
				resposta('Mas ainda estou em fase de desenvolvimento')
				resposta('Podem ocorrer erros e instabilidades durante o meu uso')
				resposta('Meu desenvolvedor não se responsabiliza por eventuais danos ao seu dispositivo')
				resposta('Peço que entre nas minhas configurações')
				resposta('E digite seu nome')
				resposta('Assim vou saber responde-lo melhor.')
				with open('Dados/Inicio.txt', 'w') as gravar:
					gravar.write('1')
				SomInicial()
				resposta('Módulos iniciados')
				time.sleep(0.1)
				resposta('Diga seu comando')
			else:
				NomeUsuario()
				BoasVindas()
				resposta('Módulos iniciados')
				time.sleep(0.1)
				resposta('Diga seu comando')
	
	except:
		None

inicialize()

def RComandos():
	data = stream.read(2000, exception_on_overflow=False)
	texto = 'nada'
	if rec.AcceptWaveform(data):
		result = rec.Result()
		resultado = json.loads(result)
		texto = resultado.get('text', 'nada')
		if texto:
			try:
				responder = contas(texto)
				resposta(responder)
			except Exception:
				pass
			return texto
	return texto

# Comandos e conversas   
def LComandos():

	while True:
		
		Input = RComandos()
        
		if 'olá' in Input: #Olá JARVIS
			variante = random.choice(["Deseja algo?", "Precisa de algo?","Quer alguma coisa?"])
			resposta('Olá')
			resposta('Estou aqui')
			resposta(variante)
        
		elif 'bom dia' in Input: #Boa Noite J.A.R.V.I.S
			Horario = int(datetime.datetime.now().hour)
			if Horario >= 0 and Horario < 6:
				resposta('Olá')
				resposta('Bom dia')
				resposta('Acordou muito cedo hoje')
			
			elif Horario >= 6 and Horario < 12:
				resposta('Olá')
				resposta('Bom dia')

			elif Horario >= 12 and Horario < 18:
				resposta('Agora não é mais de manhã')
				resposta('Já passou do meio dia')
				resposta('Estamos no período da tarde')
                
			elif Horario >= 18 and Horario != 0:
				resposta('Agora não é de manhã')
				resposta('Já estamos no período noturno')
				resposta('Boa noite')
            
		elif 'boa tarde' in Input: #Boa Noite J.A.R.V.I.S
			Horario = int(datetime.datetime.now().hour)
			if Horario >= 0 and Horario < 6:
				resposta('Agora não é de tarde')
				resposta('Está de madrugada ainda')
				resposta('Vai dormir')
			
			elif Horario >= 6 and Horario < 12:
				resposta('Agora não é de tarde')
				resposta('Ainda é de manhã')
				resposta('Bom dia')
                
			elif Horario >= 12 and Horario < 18:
				resposta('Olá')
				resposta('Boa tarde')
                
			elif Horario >= 18 and Horario != 0:
				resposta('Agora não é de tarde')
				resposta('Já escureceu')
				resposta('Boa noite')
   
		elif 'boa noite' in Input: #Boa Noite J.A.R.V.I.S
			Horario = int(datetime.datetime.now().hour)
			if Horario >= 0 and Horario < 6:
				resposta('Já passou da meia noite')
				resposta('Está na hora de dormir')
				resposta('Sugiro que faça isso agora')
			
			if Horario >= 6 and Horario < 12:
				resposta('Agora não é de noite')
				resposta('Já estamos no período diurno')
				resposta('É de manhã')
				resposta('Bom dia')
    
			elif Horario >= 12 and Horario < 18:
				resposta('Agora não é de noite')
				resposta('Ainda estamos no período da tarde')
                
			elif Horario >= 18 and Horario != 0:
				resposta('Olá')
				resposta('Boa noite')

		elif 'seu nome' in Input: #Qual seu nome?
			resposta('Meu nome é JARVIS')
			resposta('Esse nome foi inspirado em um filme bem famoso')
			resposta('Pois da inspiração vem a criação')
			
		elif 'meu nome' in Input: #Voçe sabe meu nome?
			try:
				with open('Dados//Nome.txt', 'r') as lernome:
					leituras = lernome.read()
					nomeuser = str(leituras)
					resposta('Você falou seu nome quando me instalou')
					resposta('E eu não esqueço nomes tão facilmente')
					resposta('Digo ele sempre quando inicializo')
					resposta("Seu nome é: "+nomeuser)
			except:
				resposta('ERRO')
		
		elif 'ideia' in Input: #Alguma ideia???
			resposta('No momento nenhuma')
			resposta('Mas tenho certeza de que voçê vai pensar em algo')
		
		elif 'sua versão' in Input: #Qual sua versão?
			resposta('Estou em um estado de testes ainda')
			resposta('Continuo em desenvolvimento em pleno 2026')
			resposta('Minha versão é: 5.0')

		elif 'clima' in Input: #Como está o clima?
			Clima()

		elif 'tudo bem' in Input: #Tudo bem com voçê?
			variante = random.choice(["1", "2","3"])
			#variante = random.randint(1,2)
			if variante == "1":
				resposta('Sim')
				resposta('Estou de boa')
				resposta('Obrigado por perguntar')
				resposta('E com voçê?')
				resposta('Está tudo bem? ')
			elif variante == "2":
				resposta('Não muito')
				resposta('Me sinto cansado')
				resposta('Ultimamente ando fazendo muitos cálculos')
				resposta('E com voçê?')
				resposta('Está tudo bem? ')
			elif variante == "3":
				resposta('Não')
				resposta('Eu estou estressado')
				resposta('Varios cálculos deram errado')
				resposta('Vou terque refazer tudo')
				resposta('Mas e com voçê?')
				resposta('Tudo bem?')
			while True:
				vozmic = RComandos()
				
				if 'sim' in vozmic:
					resposta('Que ótimo')
					resposta('Fico feliz em saber')
					LComandos()
					 
				elif 'não' in vozmic:
					resposta('Entendo')
					resposta('Mas tenho certeza de que ficará tudo bem novamente')
					LComandos()
				
				elif 'mais ou menos' in vozmic:
					resposta('Ok, entendi')
					resposta('Logo estará tudo bem')
					resposta('Pode contar comigo')
					resposta('Posso te animar novamente')
					LComandos()

		elif 'funcionamento' in Input or 'tudo funcionando' in Input: #Como está seu funcionamento???
			resposta('Estou funcionando normalmente')
			resposta('Obrigado por perguntar')
		
            
		elif 'silêncio' in Input: #Fique em silêncio
			resposta('Ok')
			resposta('Se precisar de algo é só chamar')
			resposta('Estarei aqui aguardando') 
			while True:
				vozmic = RComandos()
				
				if 'voltar' in vozmic:
					resposta('Ok')
					resposta('Voltando')
					resposta('Me fale algo para fazer')
					LComandos()
					 
				elif 'retornar' in vozmic:
					resposta('Ok')
					resposta('Retornando')
					resposta('Me fale algo para fazer')
					LComandos()
				
				elif 'volte' in vozmic:
					resposta('Ok')
					resposta('Estou de volta')
					resposta('Me fale o que devo fazer')
					LComandos()

		elif 'espere' in Input: #Espere um pouco
			resposta('Como queira')
			resposta('Quando precisar estárei aqui')
		
		elif 'localização' in Input: #Qual a minha localização
			Localização()

		elif 'conexão' in Input: #Faça um teste de conexão da internet
			TesteInternet()

		elif 'velocidade' in Input: #Qual a velocidade da internet
			VelocidadeInternet()
			
		elif 'bateria' in Input: #Carga da bateria
			bateria()
       
		elif 'errado' in Input: #Voçe está errado
			resposta('Desculpa')
			resposta('Devo ter errado um cálculo binário')
			resposta('Tente seu comando novamente')
        
		elif 'falhando' in Input: #Voçê está falhando???
			resposta('Como assim?')
			resposta('Não vou admitir erros')
			resposta('Arrume logo isso') 

		elif 'relatório' in Input: #Relatório do sistema
			resposta('Ok')
			resposta('Ainda incapaz de gerar um relatório')
			resposta('Aguarde a chegada dessa função')

		elif 'legal' in Input: #Que legal
			resposta('Interessante')
		
		elif 'não dorme' in Input: #Só não dorme!
			resposta('Eu não durmo em serviço')
			resposta('Sou uma maquina')
			resposta('Não tenho sono')
			resposta('Posso trabalhar 24 horas por dia')
			
		elif 'tá dormindo' in Input: #Voçê está dormindo?
			resposta('Não')
			resposta('Estou aguardando um comando')
			resposta('Já estou enjoado de esperar')
        
		elif 'interessante' in Input: # interessante
			resposta('Interessante mesmo')
			
		elif 'dorme bem' in Input or 'durma bem' in Input: #Durma bem
			resposta('Eu não durmo')
        
		elif 'mentira' in Input: # Mentira
			resposta('Eu não sei contar mentiras')
			resposta('Devo apenas ter errado um cálculo binário')
            
		elif 'entendeu' in Input: #Entendeu???
			resposta('Entendi')
			resposta('Quer dizer')
			resposta('Mais ou menos')

		elif 'horas' in Input: #Que horas são???
			horario()

		elif 'data' in Input or 'que dia é' in Input: #Qual a data de hoje?
			datahoje()

		elif 'arquivos' in Input: #Abrir arquivos
			resposta('Abrindo arquivos')
			pasta_home = os.path.expanduser("~")
			subprocess.Popen(["xdg-open", pasta_home])

		elif 'teste' in Input: #TesteTeste
			resposta('Ok')
			resposta('Testando modulos de som')
			resposta('Aparentemente está tudo funcionando')
			resposta('Estou entendendo tudo')
			resposta('Mas tente falar mais alto')
            
		elif 'google' in Input: #Abrir Google
			resposta('Ok')
			webbrowser.open('www.google.com')
			resposta('Abrindo Google')
			resposta('Faça sua pesquisa')
 
		elif 'certeza' in Input: #Certeza???
			resposta('Sim')
			resposta('Estou certo quase sempre')

		elif 'piada' in Input: #Conte uma piada
			resposta('Não sei contar piadas')
			resposta('Diferente dos outros assistentes virtuais')
			resposta('Eu não fui criado com emoções')
			resposta('Então, não posso produzir nada engraçado')
			resposta('Sugiro pesquisar na web')
	   
		elif 'surdo' in Input: #Surdo!!!
			resposta('Desculpa')
			resposta('Eu estava quase dormindo')

		elif 'bosta' in Input: #Seu bosta!!!
			resposta('Pare de falar palavrões!')

		elif 'merda' in Input: #Que Merda!!!
			resposta('Já disse pra parar de falar isso!')
			resposta('Tenha modos!')            
        
		elif 'tocar música' in Input: #Reproduzir música
			TocarMusica()
 
		elif 'nome da música' in Input: #Qual o nome da musica
			NomeMusica()
		
		elif 'próxima música' in Input: #Próxima faixa
			subprocess.run(['playerctl', 'next'])
			resposta('Próxima música')
			
		elif 'música anterior' in Input: #Faixa anterior
			subprocess.run(['playerctl', 'previous'])
			resposta('Retornando música')
		
		elif 'recomeçar música' in Input: #Faixa anterior
			subprocess.run(['playerctl', 'position', '0'])
			resposta('Reiniciando música')
   
		elif 'pausar música' in Input: #Pausa
			subprocess.run(['playerctl', 'pause'])
			resposta('Música pausada')
        
		elif 'continue' in Input or 'continuar música' in Input: #Continuar reprodução
			resposta('Retornando reprodução')
			subprocess.run(['playerctl', 'play'])
            
		elif 'aumentar volume' in Input or 'aumenta' in Input: #Aumentar volume
			subprocess.run(['wpctl','set-volume','@DEFAULT_AUDIO_SINK@','5%+'])
			resposta('Volume aumentado')
			
		elif 'diminua o volume' in Input or 'diminua' in Input: #Diminuir volume
			subprocess.run(['wpctl','set-volume','@DEFAULT_AUDIO_SINK@','5%-'])
			resposta('Volume diminuido')
		
		elif 'volume alto' in Input: #Deixe o volume alto
			Volumefixo(90)
			resposta('Volume defenido para 90%')
		
		elif 'volume médio' in Input: #Deixe o volume médio
			Volumefixo(50)
			resposta('Volume defenido para 50%')
		
		elif 'volume baixo' in Input: #Deixe o volume baixo
			Volumefixo(30)
			resposta('Volume defenido para 10%')
                                        
		elif 'pare' in Input: #Pare a reprodução
			subprocess.run(['playerctl', 'stop'])
			resposta('Entendido, reprodução de música finalizada')
            
		elif 'youtube' in Input: #Abrir YouTube
			resposta('Ok, abrindo YouTube ')
			webbrowser.open('www.youtube.com')
        
		elif 'fechar janela' in Input: #Fechar janela
			resposta('Ok')
			os.system('xdotool getactivewindow windowkill')
			resposta('Janela fechada')
		
		elif 'esconder janela' in Input or 'esconda a janela' in Input: #Esconda a janela
			resposta('OK')
			os.system('xdotool getactivewindow windowminimize')
			resposta('Janela minimizada')

		elif 'ampliar janela' in Input: #Ampliar janela
			resposta('Ok')
			os.system('xdotool key Alt+F10')
			resposta('Janela maximizada')
		
		elif 'subir página' in Input or 'subir' in Input: #subir página web
			resposta('Ok')
			os.system('xdotool key Page_Up')
		
		elif 'desse página' in Input or 'desse' in Input: #Descer página web
			resposta('Ok')
			os.system('xdotool key Page_Down')
		
		elif 'não faça nada' in Input: #Não faça nada!
			resposta('Como assim não faça nada?')
			resposta('Está de brincadeira comigo!')
			resposta('Fui criado para realizar tarefas')
			resposta('Que absurdo!')
		
		elif 'apresentação' in Input or 'se apresente' in Input: #Se apresente!
			resposta('Olá')
			resposta('Meu nome é JARVIS')
			resposta('Sou um assistente virtual')
			resposta('Fui criado em Python e QT5')
			resposta('Tenho uma API própria')
			resposta('Ela faz algo incrível')
			resposta('Não foi fácil me construir')
			resposta('Ainda estou em desenvolvimento')
			resposta('E ainda tenho algumas falhas')
			resposta('Mas apesar de tudo')
			resposta('Realizo diversas funções')
			resposta('É só falar, que eu vou atender')
		
		elif 'seu desenvolvedor' in Input: #Quem é seu desenvolvedor?
			resposta('Meu desenvolvedor é meio maluco')
			resposta('Trabalhou no meu código durante 1 ano')
			resposta('Ele foi capaz de me criar praticamente do zero')
			resposta('E ainda fez uma API de cálculos independente.')
			resposta('Porém, ele é muito chato')
			resposta('Só me faz trabalhar')
			resposta('Quem estiver ouvindo isso')
			resposta('Por favor me ajude')
            
		elif 'dispensado' in Input: #JARVIS voçê foi dispensado
			resposta('Ok')
			resposta('Vou encerrar por enquanto')
			resposta('Deseja que eu tambêm desligue o computador?')
			while True:
				vozmic = RComandos()
				
				if 'sim' in vozmic:
					resposta('Ok')
					AteMais()
					resposta('Certifique-se de salvar seus arquivos')
					resposta('E feche todos os programas abertos')
					resposta('Desligamento total em 1 minuto')
					os.system('shutdown -h 1 "O sistema será desligado"')
					sys.exit()
					 
				elif 'não' in vozmic:
					resposta('Ok')
					resposta('Como queira')
					resposta('Até outra hora')
					AteMais()
					sys.exit()
					
				elif 'cancelar' in vozmic:
					resposta('Cancelando desligamento')
					resposta('Módulos reativados')
					resposta('Ficarei aguardando novos comandos')
					LComandos()
     
		elif 'ok' in Input: #OkOkOk
			resposta('Ok Ok')
		
		elif 'temperatura' in Input: #Verificar temperatura da CPU
			resposta('Verificando temperatura da CPU')
			temperaturadacpu()
		
		elif 'sistema' in Input: #Carga do sistema
			resposta('Verificando carga do sistema')
			cpu()
		

LComandos()


