#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CPN.py
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


numeros = {
	'um':1,
	'dois':2,
	'três':3,
	'quatro':4,
	'cinco':5,
	'seis':6,
	'sete':7,
	'oito':8,
	'nove':9,
	'dez':10,
	'onze':11,
	'doze':12,
	'treze':13,
	'quatorze':14,
	'quinze':15,
	'dezesseis':16,
	'dezessete':17,
	'dezoito':18,
	'dezenove':19,
	'vinte':20,
	'trinta':30,
	'quarenta':40,
	'cinquenta':50,
	'sessenta':60,
	'setenta':70,
	'oitenta':80,
	'noventa':90,
	'cento':100,
	'sem':100,
	'cem':100,
	'duzentos':200,
	'trezentos':300,
	'quatrocentos':400,
	'quinhentos':500,
	'seiscentos':600,
	'setecentos':700,
	'oitocentos':800,
	'novecentos':900,
	'mil':1000,
	'milhão':1000000
	}


def getnumero(entradatexto):
	escrita = entradatexto
	escrito = escrita.split()
	try:
		try:
			try:
				try:
					try:
						try:
							try:
								try:
									try:
										try:
											try:
												try:
													try:
														try:
															try:
																num1 = numeros[escrito[0]]
																num2 = numeros[escrito[2]]
																num3 = numeros[escrito[4]]
																num4 = numeros[escrito[5]]
																num5 = numeros[escrito[7]]
																num6 = numeros[escrito[9]]
																num7 = numeros[escrito[11]]
																conta = num1+num2+num3
																conta2 = conta*num4
																return conta2+num5+num6+num7
															except:
																num1 = numeros[escrito[0]]
																num2 = numeros[escrito[2]]
																num3 = numeros[escrito[3]]
																num4 = numeros[escrito[5]]
																num5 = numeros[escrito[7]]
																num6 = numeros[escrito[9]]
																conta = num1+num2
																conta2 = conta*num3
																return conta2+num4+num5+num6
														except:
															num1 = numeros[escrito[0]]
															num2 = numeros[escrito[2]]
															num3 = numeros[escrito[4]]
															num4 = numeros[escrito[5]]
															num5 = numeros[escrito[7]]
															num6 = numeros[escrito[9]]
															conta = num1+num2+num3
															conta2 = conta*num4
															return conta2+num5+num6
													except:
														num1 = numeros[escrito[0]]
														num2 = numeros[escrito[2]]
														num3 = numeros[escrito[4]]
														num4 = numeros[escrito[5]]
														num5 = numeros[escrito[7]]
														conta = num1+num2+num3
														conta2 = conta*num4
														return conta2+num5
												except:
													num1 = numeros[escrito[0]]
													num2 = numeros[escrito[2]]
													num3 = numeros[escrito[3]]
													num4 = numeros[escrito[5]]
													num5 = numeros[escrito[7]]
													conta = num1+num2
													conta2 = conta*num3
													return conta2+num4+num5
											except:
												num1 = numeros[escrito[0]]
												num2 = numeros[escrito[1]]
												num3 = numeros[escrito[2]]
												num4 = numeros[escrito[4]]
												num5 = numeros[escrito[6]]
												return num1 * num2 + num3 + num4 + num5
										except:
											if 'mil' in escrito[1]:
												try:
													try:
														num1 = numeros[escrito[0]]
														num2 = numeros[escrito[1]]
														num3 = numeros[escrito[3]]
														num4 = numeros[escrito[5]]
														num5 = numeros[escrito[7]]
														conta = num1 * num2
														return conta + num3 + num4 + num5
													except:
														num1 = numeros[escrito[0]]
														num2 = numeros[escrito[1]]
														num3 = numeros[escrito[3]]
														num4 = numeros[escrito[5]]
														conta = num1 * num2
														return conta + num3 + num4
												except:
													num1 = numeros[escrito[0]]
													num2 = numeros[escrito[1]]
													num3 = numeros[escrito[3]]
													return num1*num2+num3
											else:
												num1 = numeros[escrito[0]]
												num2 = numeros[escrito[1]]
												num3 = numeros[escrito[3]]
												num4 = numeros[escrito[5]]
												return num1 + num2 + num3 + num4
									except:
										num1 = numeros[escrito[0]]
										num2 = numeros[escrito[2]]
										num3 = numeros[escrito[4]]
										num4 = numeros[escrito[5]]
										conta = num1 + num2 + num3
										return conta * num4
								except:
									num1 = numeros[escrito[0]]
									num2 = numeros[escrito[2]]
									num3 = numeros[escrito[3]]
									num4 = numeros[escrito[5]]
									conta = num1+num2
									conta2 = conta*num3
									return conta2+num4
							except:
								num1 = numeros[escrito[0]]
								num2 = numeros[escrito[2]]
								num3 = numeros[escrito[3]]
								soma = num1 + num2
								return soma * num3
						except:
							num1 = numeros[escrito[0]]
							num2 = numeros[escrito[1]]
							num3 = numeros[escrito[3]]
							return num1 + num2 + num3
					except:
						num1 = numeros[escrito[0]]
						num2 = numeros[escrito[2]]
						num3 = numeros[escrito[4]]
						return num1 + num2 + num3
				except:
					num1 = numeros[escrito[0]]
					num2 = numeros[escrito[2]]
					return num1 + num2
			except:
				num1 = numeros[escrito[0]]
				num2 = numeros[escrito[1]]
				return num1 * num2
		except:
			num1 = numeros[escrito[0]]
			return num1
	except:
		if entradatexto == None:
			None
		else:
			None

def contas(entrada):
	dados = entrada
	if 'vezes' in dados:
		oper = 'vezes'
		oper2 = len(oper)
	if 'mais' in dados:
		oper = 'mais'
		oper2 = len(oper)
	if 'menos' in dados:
		oper = 'menos'
		oper2 = len(oper)
	if 'dividido por' in dados:
		oper = 'dividido por'
		oper2 = len(oper)
	data0 = dados.find(oper)
	data1 = data0-1
	num1 = dados[:data1]
	num2 = data0 + oper2
	num3 = dados[num2:]
	total1 = getnumero(str(num1))
	total2 = getnumero(str(num3))
	if 'vezes' in oper:
		conta = '{} vezes {} '.format(total1, total2)
		conta2 = total1 * total2
		final = 'O resultado de '+conta +'é ' +str(conta2)
		return final
	elif 'mais' in oper:
		conta = '{} mais {} '.format(total1, total2)
		conta2 = total1 + total2
		final = 'O resultado de '+conta +'é ' +str(conta2)
		return final
	elif 'menos' in oper:
		conta = '{} menos {} '.format(total1, total2)
		conta2 = total1 - total2
		final = 'O resultado de '+conta +'é ' +str(conta2)
		return final
	elif 'dividido por' in oper:
		conta = '{} dividido por {} '.format(total1, total2)
		conta2 = int(total1) / int(total2)
		final = 'O resultado de '+conta +'é ' +str(conta2)
		return final


		




