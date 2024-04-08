# PyHotel - Sistema de Gestão para Hotéis.
### oi
import os
from time import sleep
import pickle
print("oi")
##################################################
###################### Menus #####################
##################################################

def menu_inicial():
	print("=" * 42)
	print("========  M E N U   I N I C I A L  =======")
	print("=" * 42)
	print("""
           Bem vindo usuário!

        O que você deseja fazer ?

	     1. Ir ao Menu Clientes.
	    2. Ir ao Menu de Quartos.
  3. Ir ao Menu de Gestão de Movimentos.
  		4. Ir ao Menu Relatórios.
	 5. Ir aos Créditos do Programa.
	     6. Encerrar o Programa.
""")
	print()
	print("=" * 42)
	print()
	opcao = input("Digite o número da opção que desejar: ")
	return opcao

def menu_clientes():
	print("=" * 40)
	print("======  M E N U   C L I E N T E S  =====")
	print("=" * 40)
	print("""
	    Bem vindo usuário!
	
	 O que você deseja fazer ?
	
	 1. Cadastrar Novo Cliente.
	     2. Buscar Cliente.
	     3. Editar Cliente.
	     4. Excluir Cliente.
	 5. Voltar ao Menu Inicial.
""")
	print()
	print("=" * 40)
	print()
	opcao = input("Digite o número da opção que desejar: ")
	return opcao

def menu_quartos():
	print("=" * 41)
	print("====  M E N U   D E   Q U A R T O S  ====")
	print("=" * 41)
	print("""
	    Bem vindo usuário!
	
	 O que você deseja fazer ?
	
	 1. Cadastrar Novo Quarto.               
	     2. Buscar Quarto.
	     3. Editar Quarto.         
	     4. Excluir Quarto.
	 5. Voltar ao Menu Inicial.
""")                                         
	print()
	print("=" * 41)
	print()
	opcao = input("Digite o número da opção que desejar: ")
	return opcao

def menu_gestao():
	print("=" * 41)
	print("=====  M E N U   D E   G E S T Ã O  =====")
	print("=" * 41)
	print("""
	    Bem vindo usuário!
	
	 O que você deseja fazer ?
	
	     1. Gerir Quarto.    
  2. Ver Situação de algum Quarto.
     3. Voltar ao Menu Inicial.
""")
	print()
	print("=" * 41)
	print()
	opcao = input("Digite o número da opção que desejar: ")
	return opcao

def relatorio():
	print("=" * 44)
	print("===========  R E L A T Ó R I O S  ==========")
	print("=" * 44)
	print("""
           Bem vindo usuário!

        O que você deseja fazer ?

	   1. Ver relatórios dos Clientes.
	    2. Ver relatórios dos Quartos.
	     3. Voltar ao Menu Inicial.
""")
	print()
	print("=" * 44)
	print()
	opcao = input("Digite o número da opção que desejar: ")
	return opcao

def creditos():
	print("=" * 41)
	print("===========  C R É D I T O S  ===========")
	print("=" * 41)
	print("""
Créditos e informações do projeto:

PyHotel - Sistema de Gestão para Hotéis.
  Developer: Luiz Miguel Santos Silva
   Estudante de BSI na UFRN - Ceres
	     Ano da Criação: 2023
 """)
	print("=" * 41)
	print()
	opcao = input("Digite Enter para voltar ao Menu Inicial. ")
	return opcao

def encerramento():
	print("=" * 41)
	print("======  A T É   A   P R Ó X I M A  ======")
	print("=" * 41)
	sleep(4)
	os.system("cls || clear")

##################################################
###################### Subs ######################
##################################################

def error():
	print()
	print("Opps, ocorreu algum erro...")
	print()
	print("Por favor, digite novamente.")
	print()

def error2():
	print()
	print("O CPF digitado não pertence a nenhum cliente cadastrado!")
	print()
	print("Por favor, digite novamente.")
	print()

def validar_cpf(cpf):			#BASEADO NO SLIDE DA AULA DA SEMANA 16
	tam = len(cpf)
	soma = 0
	d1 = 0
	d2 = 0
	if tam != 11:
		return False
	for i in range(11):
		if (cpf[i]<'0')or(cpf[i]>'9'):
			return False
	for i in range(9):
		soma += (int(cpf[i])*(10 - i))
	d1 = 11 - (soma % 11)
	if (d1 == 10 or d1 == 11):
		d1 = 0
	if d1 != int(cpf[9]):
		return False
	
	soma = 0
	for i in range(10):
		soma += (int(cpf[i])*(11-i))
	d2 = 11 - (soma%11)
	if (d2 == 10 or d2 == 11):
		d2 = 0
	if d2 != int(cpf[10]):
		return False
	
	return True				

def validar_nome():
	while True:
		nome = input("Nome: ")
		if len(nome) < 2:
			error()
		elif not nome.replace(" ", "").isalpha():	
			error()
		else:
			break
	return nome		

def validar_nome2():
	while True:
		nome = input("Digite o novo nome: ")
		if len(nome) < 2:
			error()
		elif not nome.replace(" ", "").isalpha():	
			error()
		else:
			break
	return nome		

def validar_esc():
	esc = input("Digite o número da opção que deseja editar: ")
	while esc not in ["1", "2", "3"]:
		print()
		print("Opção inválida. Por favor, digite novamente.")
		print()
		esc = input("Digite o número da opção que deseja editar: ")
	return esc	

def val_esc2():
	esc = input("Digite o número da opção que deseja editar: ")
	while esc not in ["1", "2", "3", "4", "5"]:
		print()
		print("Opção inválida. Por favor, digite novamente.")
		print()
		esc = input("Digite o número da opção que deseja editar: ")
	return esc	

def validar_resp():
	resp = input("Deseja mesmo editar esse cliente (S/N)? ").upper()
	while resp not in ["S","N"]:
		print()
		print("Resposta inválida. Por favor, digite novamente.")
		print()
		resp = input("Deseja mesmo editar esse cliente (S/N)? ").upper()
	return resp	

def validar_resp2():
	resp = input("Deseja mesmo excluir esse cliente (S/N)? ").upper()
	while resp not in ["S","N"]:
		print()
		print("Resposta inválida. Por favor, digite novamente.")
		print()
		resp = input("Deseja mesmo excluir esse cliente (S/N)? ").upper()
	return resp	

def val_resp2():
	resp = input("Deseja mesmo excluir esse quarto (S/N)? ").upper()
	while resp not in ["S","N"]:
		print()
		print("Resposta inválida. Por favor, digite novamente.")
		print()
		resp = input("Deseja mesmo excluir esse quarto (S/N)? ").upper()
	return resp	

def val_resp3():
	resp = input("Deseja mesmo editar esse quarto (S/N)? ").upper()
	while resp not in ["S","N"]:
		print()
		print("Resposta inválida. Por favor, digite novamente.")
		print()
		resp = input("Deseja mesmo editar esse quarto (S/N)? ").upper()
	return resp	

def validar_num():
	num = input("Número do Quarto: ")
	while not num.isdigit():	
		print()
		print("Opps, ocorreu algum erro...")
		print()
		print("Por favor, digite novamente.")
		print()
		num = input("Número do Quarto: ")
	return num	

def val_num2():
	num = input("Digite o número do quarto que deseja gerir: ")
	while not num.isdigit():	
		error()
		num = input("Digite o número do quarto que deseja gerir: ")
	return num	

def val_hos():
	hos = input("Quantos hóspedes cabem no quarto: ")
	while not hos.isdigit():	
		error()
		hos = input("Quantos hóspedes cabem no quarto: ")
	return hos	

def val_hos2():
	hos = input("Digite a nova capacidade de hóspedes: ")
	while not hos.isdigit():	
		error()
		hos = input("Digite a nova capacidade de hóspedes: ")
	return hos	

def val_cama():
	cama = input("Quantas camas tem no quarto: ")
	while not cama.isdigit():
		error()
		cama = input("Quantas camas tem no quarto: ")
	return cama	

def val_cama2():
	cama = input("Digite a nova quantidade de camas: ")
	while not cama.isdigit():
		error()
		cama = input("Digite a nova quantidade de camas: ")
	return cama

def val_ban():
	ban = input("Quantos banheiros tem no quarto: ")
	while not ban.isdigit():
		error()
		ban = input("Quantos banheiros tem no quarto: ")
	return ban	

def val_ban2():
	ban = input("Digite a nova quantidade de banheiros: ")
	while not ban.isdigit():
		error()
		ban = input("Digite a nova quantidade de banheiros: ")
	return ban	

def val_preco():
	while True:
		try:
			preco = float(input("Preço/dia do Quarto: "))
			break
		except:
			error()
	return preco		

def val_preco2():
	while True:
		try:
			preco = float(input("Digite o novo preço/dia: "))
			break
		except:
			error()
	return preco		

def val_tel1():
	tel = input("Telefone (com DDD): ")
	tel = replace(tel)
	while not tel.isdigit() or len(tel) != 11 or tel[2] != "9":
		error()
		tel = input("Telefone (com DDD): ")
		tel = replace(tel)
	return tel	

def val_tel2():
	tel = input("Digite o novo telefone (com DDD): ")
	tel = replace(tel)
	while not tel.isdigit() or len(tel) != 11 or tel[2] != "9":
		error()
		tel = input("Digite o novo telefone (com DDD): ")
	return tel	

def val_idade1():
	idade = input("Idade: ")
	while not idade.isdigit():
		error()
		idade = input("Idade: ")
	return idade	

def val_idade2():
	idade = input("Digite a nova idade: ")
	while not idade.isdigit():
		error()
		idade = input("Digite a nova idade: ")
	return idade	

def val_alug(num):
	alug = input("O quarto %s está alugado (S/N)? "%num).upper()
	while alug not in ["S","N"]:
		print()
		print("Resposta inválida. Por favor, digite novamente.")
		print()
		alug = input("O quarto %s está alugado (S/N)? "%num).upper()
	return alug

def val_dias(num):
	dias = input("O quarto %s estará alugado por quantos dias? "%num)
	while not dias.isdigit():	
		error()
		dias = input("O quarto %s estará alugado por quantos dias? "%num)
	return dias	

def print_dados():
	print("=" * 30)
	print()
	print("""
1. Nome
2. Telefone
3. Idade
""")
	print()
	print("=" * 30)
	print()

def print_edit(dCli,cpf):
	print("=" * 30)
	print()
	print("Nome:", dCli[cpf][0])
	print("Telefone:", dCli[cpf][1])
	print("Idade:", dCli[cpf][2])
	print()
	print("=" * 30)
	print()

def print_edit2(dQuar,num):
	print("=" * 30)
	print()
	print("Quantos hóspedes cabem no quarto:", dQuar[num][0])
	print("Quantas camas tem no quarto:", dQuar[num][1])
	print("Quantos banheiros tem no quarto:", dQuar[num][2])
	print("Detalhes do Quarto:", dQuar[num][3])
	print("Preço/dia do Quarto:", dQuar[num][4])
	print()
	print("=" * 30)
	print()

def print_dados2():
	print("=" * 30)
	print()
	print("""
1. Hóspedes
2. Camas
3. Banheiros
4. Detalhes
5. Preço
""")
	print()
	print("=" * 30)
	print()

def print_busc1(dCli,cpf):
	print("Nome:",dCli[cpf][0])
	print("CPF:",cpf)
	print("Telefone:",dCli[cpf][1])
	print("Idade:",dCli[cpf][2])

def print_dados_cli(cpf):
	os.system("cls || clear")
	print()
	print("Cliente encontrado com sucesso!")
	print()
	print("=" * 30)
	print()
	dCli = try_exc1()
	print_busc1(dCli,cpf)
	print()
	print("=" * 30)
	print()

def print_exc1(cpf):
	os.system("cls || clear")
	print()
	print("Cliente encontrado com sucesso!")
	print()
	print("=" * 30)
	print()
	dCli = try_exc1()
	print_busc1(dCli,cpf)
	print()
	print("=" * 30)
	print()
	return dCli

def print_exc2(num):
	os.system("cls || clear")
	print()
	print("Quarto encontrado com sucesso!")
	print()
	print("=" * 30)
	print()
	dQuar = try_exc2()
	print_busc2(dQuar,num)
	print()
	print("=" * 30)
	print()
	return dQuar

def print_busc2(dQuar,num):
	print("Número do Quarto:", num)
	print("Quantos hóspedes cabem no quarto:", dQuar[num][0])
	print("Quantas camas tem no quarto:", dQuar[num][1])
	print("Quantos banheiros tem no quarto:", dQuar[num][2])
	print("Detalhes do Quarto:", dQuar[num][3])
	print("Preço/dia do Quarto: R$ %.2f/dia "%dQuar[num][4])

def print_dados_quar(num):
	os.system("cls || clear")
	print()
	print("Quarto encontrado com sucesso!")
	print()
	print("=" * 30)
	print()
	dQuar = try_exc2()
	print_busc2(dQuar,num)
	print()
	print("=" * 30)
	print()

def dados_quarto(num):
	print("=" * 30)
	print()
	print("Quantos hóspedes cabem no quarto:", quartos[num][0])
	print("Quantas camas tem no quarto:", quartos[num][1])
	print("Quantos banheiros tem no quarto:", quartos[num][2])
	print("Detalhes do Quarto:", quartos[num][3])
	print("Preço/dia do Quarto:", quartos[num][4])
	print()

def dados_ver_ger(dQuar,dCli,num,cpf):
	print("=" * 30)
	print()
	print("Número do Quarto:", num)
	if dQuar[num][5] == 0 or cpf not in dCli:
		print("O quarto está alugado: Sem informação!")
	else:	
		print("O quarto está alugado:", dQuar[num][5])
	if dQuar[num][5] == "N" or dQuar[num][5] == 0 or cpf not in dCli:
		print("Por quantos dias o quarto estará alugado: Sem informação!")
	else:	
		print("Por quantos dias o quarto estará alugado:", dQuar[num][6])
	if dQuar[num][5] == "N" or dQuar[num][5] == 0 or cpf not in dCli:
		print("Nome do hóspede que alugou o quarto: Sem informação!")
	else:	
		print("Nome do hóspede que alugou o quarto:", dCli[cpf][0])
	if dQuar[num][5] == "N" or dQuar[num][5] == 0 or cpf not in dCli:
		print("CPF do hóspede que alugou o quarto: Sem informação!")
	else:	
		print("CPF do hóspede que alugou o quarto:", dQuar[num][7])
	print()
	print("=" * 30)
	print()

def try_exc1():				#BASEADO NO SLIDE DA AULA DA SEMANA 17
	try:
		arq1 = open("./Códigos/PyHotel/dClientes.dat", "rb")
		clientes = pickle.load(arq1)
		arq1.close()
	except:
		arq1 =open("./Códigos/PyHotel/dClientes.dat", "wb")
		arq1.close()
	return clientes				

def try_exc2():				#BASEADO NO SLIDE DA AULA DA SEMANA 17
	try:
		arq1 = open("./Códigos/PyHotel/dQuartos.dat", "rb")
		quartos = pickle.load(arq1)
		arq1.close()
	except:
		arq1 =open("./Códigos/PyHotel/dQuartos.dat", "wb")
		arq1.close()
	return quartos				

def guard_arq1(clientes):			#BASEADO NO SLIDE DA AULA DA SEMANA 17
	arq1 = open("./Códigos/PyHotel/dClientes.dat", "wb")
	clientes.update(clientes)
	pickle.dump(clientes, arq1)
	arq1.close()

def guard_arq2(quartos):			#BASEADO NO SLIDE DA AULA DA SEMANA 17
	arq1 = open("./Códigos/PyHotel/dQuartos.dat", "wb")
	quartos.update(quartos)				#ATUALIZA O DICIONÁRIO COM NOVOS DADOS SE TIVER
	pickle.dump(quartos, arq1)
	arq1.close()
	
def entrada_edit(entrada,dCli,cpf,posicao):
	arq1 = open("./Códigos/PyHotel/dClientes.dat", "wb")
	dCli[cpf][posicao] = entrada
	dCli.update(dCli)
	pickle.dump(dCli, arq1)
	arq1.close()

def entrada_edit2(entrada,dQuar,num,posicao):
	arq1 = open("./Códigos/PyHotel/dQuartos.dat", "wb")
	dQuar[num][posicao] = entrada
	dQuar.update(dQuar)
	pickle.dump(dQuar, arq1)
	arq1.close()

def del_cli(cpf,dCli):
	arq1 = open("./Códigos/PyHotel/dClientes.dat", "wb")
	del dCli[cpf]
	dCli.update(dCli)
	pickle.dump(dCli, arq1)
	arq1.close()

def del_quar(num,dQuar):
	arq1 = open("./Códigos/PyHotel/dQuartos.dat", "wb")
	del dQuar[num]
	dQuar.update(dQuar)
	pickle.dump(dQuar, arq1)
	arq1.close()

def repeat(clientes,cpf,nome):
	print()
	tel = val_tel1()
	print()
	idade = val_idade1()
	clientes[cpf] = [nome, tel, idade]
	guard_arq1(clientes)
	print()
	print("Cliente cadastrado com sucesso!")

def repeat2(quartos,num):
	print()
	hos = val_hos()
	print()
	cama = val_cama()
	print()
	ban = val_ban()
	print()
	det = input("Detalhes do Quarto: ")
	print()
	preco = val_preco()
	quartos[num] = [hos, cama, ban, det, preco, 0, 0, 0]
	guard_arq2(quartos)
	print()
	print("Quarto cadastrado com sucesso!")

def cad_cpf_ger():
	while True:
		cpf = input("CPF do hóspede que alugou o quarto: ")
		cpf = replace(cpf)
		if validar_cpf(cpf): 
			break
		else:
			error()
	clientes2 = try_exc1()	
	if cpf in clientes2:
		print()
		print("Dados cadastrados com sucesso!")
		print()
	else:
		while cpf not in clientes2:
			error2()
			cpf = input("CPF do hóspede que alugou o quarto: ")
			cpf = replace(cpf) 
	return cpf
	
def cad_ger(entrada1,entrada2,entrada3,dQuar,num):
	entrada_edit2(entrada1,dQuar,num,5)
	entrada_edit2(entrada2,dQuar,num,6)
	entrada_edit2(entrada3,dQuar,num,7)

def rel_cli():
	if arq_vazio("./Códigos/PyHotel/dClientes.dat"):
		print()
		print("=" * 17)
		print()
		print("Relatório vazio!")
		print()
		print("=" * 17)
	else:	
		clientes2 = try_exc1()
		print("Nome:                                CPF:")
		print()
		for x in clientes2:
			nome = clientes2[x][0]
			print("%-30s\t %15s"%(nome,x))
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")		

def rel_qua():
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print()
		print("=" * 17)
		print()
		print("Relatório vazio!")
		print()
		print("=" * 17)
	else:
		quartos2 = try_exc2()
		print("Quartos Cadastrados:")
		print()	
		for x in quartos2:
			print("Quarto - %s"%x)
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")		

def replace(x):				#BASEADO NO SLIDE DA AULA DA SEMANA 16
	x = x.replace("(", "")
	x = x.replace(")", "")
	x = x.replace(".", "")
	x = x.replace("-", "")
	x = x.replace(" ", "")
	return x

def arq_vazio(arquivo):				#ABRE O ARQUIVO E FECHA SEM PRECISAR USAR A FUNÇÃO .CLOSE()
    with open(arquivo, 'rb') as arq:
        return not arq.read()			#BASEADO NO SITE: https://www.hashtagtreinamentos.com/estrutura-with-python

##################################################
################# Menus de Menus #################
##################################################

def cad_clientes():
	print("Informe os dados do cliente.")
	print()
	nome = validar_nome()
	print()
	while True:
		cpf = input("CPF: ")
		cpf = replace(cpf)
		if validar_cpf(cpf): 
			break
		else:
			error()	
	if arq_vazio("./Códigos/PyHotel/dClientes.dat"):
		repeat(clientes,cpf,nome)
	else:
		clientes2 = try_exc1()
		if cpf in clientes2:
			os.system("cls || clear")
			print("Já existe um cliente cadastrado utilizando esse CPF!")	
		else:	
			repeat(clientes,cpf,nome)
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def busc_clientes():
	cpf = input("Informe o CPF do cliente: ")
	cpf = replace(cpf)
	print()
	if arq_vazio("./Códigos/PyHotel/dClientes.dat"):
		print("CPF não encontrado!")
		print()
	else:	
		clientes2 = try_exc1()
		if cpf in clientes2:
			print_dados_cli(cpf)
		else:
			print("CPF não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def edit_clientes():
	cpf = input("Informe o CPF do cliente que deseja editar: ")
	cpf = replace(cpf)
	print()
	if arq_vazio("./Códigos/PyHotel/dClientes.dat"):
		print("CPF não encontrado!")
		print()
	else:
		clientes2 = try_exc1()
		if cpf in clientes2:
			dCli = clientes2
			print_edit(dCli,cpf)
			resp = validar_resp()
			if resp == "S":
				os.system("cls || clear")
				print_dados()
				esc = validar_esc()
				if esc in ["1", "2", "3"]:
					os.system("cls || clear") 
					if esc == "1":
						nome = validar_nome2()
						entrada_edit(nome,dCli,cpf,0)
					elif esc == "2":
						tel = val_tel2()
						entrada_edit(tel,dCli,cpf,1)
					elif esc == "3":
						idade = val_idade2()
						entrada_edit(idade,dCli,cpf,2)
					print()	
					print("Dados do cliente editados com sucesso!")
					print()
			elif resp == "N":
				print()
				print("Ok")
				print()
		else:
			print("CPF não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def exc_clientes():
	cpf = input("Informe o CPF do cliente que deseja excluir: ")
	cpf = replace(cpf)
	print()
	if arq_vazio("./Códigos/PyHotel/dClientes.dat"):
		print("CPF não encontrado!")
	else:
		clientes2 = try_exc1()
		if cpf in clientes2:
			dCli = print_exc1(cpf)
			resp = validar_resp2()
			if resp == "S":
				del_cli(cpf,dCli)
				print()
				print("Cliente excluído com sucesso!")
			elif resp == "N":
				print()
				print("Ok")
		else:
			print("CPF não encontrado!")
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

##################################################

def cad_quarto():
	print("Informe os dados do quarto.")
	print()
	num = validar_num()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		repeat2(quartos,num)
	else:
		quartos2 = try_exc2()
		if num in quartos2:
			os.system("cls || clear")
			print("Já existe um quarto cadastrado com esse número!")
		else:	
			repeat2(quartos,num)
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def busc_quarto():
	num = input("Informe o número do quarto: ")
	print()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print("Número do quarto não encontrado!")
		print()
	else:
		quartos2 = try_exc2()
		if num in quartos2:
			print_dados_quar(num)
		else:
			print("Número do quarto não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def edit_quarto():
	num = input("Informe o número do quarto que deseja editar: ")
	print()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print("Número do quarto não encontrado!")
		print()
	else:
		quartos2 = try_exc2()
		if num in quartos2:
			dQuar = quartos2
			print_edit2(dQuar,num)
			resp = val_resp3()
			if resp == "S":
				os.system("cls || clear")
				print_dados2()
				esc = val_esc2()
				if esc in ["1", "2", "3", "4", "5"]:
					os.system("cls || clear") 
					if esc == "1":
						hos = val_hos2()
						entrada_edit2(hos,dQuar,num,0)
					elif esc == "2":
						cama = val_cama2()
						entrada_edit2(cama,dQuar,num,1)
					elif esc == "3":
						ban = val_ban2()
						entrada_edit2(ban,dQuar,num,2)
					elif esc == "4":
						det = input("Digite os novos detalhes: ")
						entrada_edit2(det,dQuar,num,3)
					elif esc == "5":
						preco = val_preco2()
						entrada_edit2(preco,dQuar,num,4)
					print()	
					print("Dados do quarto editados com sucesso!")
					print()
			elif resp == "N":
				print()
				print("Ok")
				print()
		else:
			print("Número do quarto não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def exc_quarto():
	num = input("Informe o número do quarto que deseja excluir: ")
	print()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print("Número do quarto não encontrado!")
	else:
		quartos2 = try_exc2()
		if num in quartos2:
			dQuar = print_exc2(num)
			resp = val_resp2()
			if resp == "S":
				del_quar(num,dQuar)
				print()
				print("Quarto excluído com sucesso!")
			elif resp == "N":
				print()
				print("Ok")
		else:
			print("Número do quarto não encontrado!")
	print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

##################################################

def ger():
	print("Gerenciar Quartos.")
	print()
	num = val_num2()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print()
		print("Número do quarto não encontrado!")
		print()
	else:
		quartos2 = try_exc2()
		if num in quartos2:
			os.system("cls || clear")
			alug = val_alug(num)
			if alug == "S":
				print()
				dias = val_dias(num)
				print()
				cpf = cad_cpf_ger()
			elif alug == "N":
				print()
				print("Então o quarto está livre.")
				print()
				dias = "Nenhum!"
				cpf = "Nenhum!"
			cad_ger(alug,dias,cpf,quartos2,num)
		else:
			print()
			print("Número do quarto não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")

def ver_ger():			
	num = input("Informe o número do quarto que deseja ver: ")
	print()
	if arq_vazio("./Códigos/PyHotel/dQuartos.dat"):
		print("Número do quarto não encontrado!")
		print()
	else:
		clientes2 = try_exc1()
		quartos2 = try_exc2()
		if num in quartos2:
			cpf = quartos2[num][7]
			dados_ver_ger(quartos2,clientes2,num,cpf)
		else:
			print("Número do quarto não encontrado!")
			print()
	input("Tecle ENTER para voltar para o Menu Inicial...")
	
##################################################
############### Programa Principal ###############
##################################################

clientes = {}
quartos = {}

try:			#BASEADO NO SLIDE DA AULA DA SEMANA 17
	arq1 = open("./Códigos/PyHotel/dClientes.dat", "rb")
	clientes = pickle.load(arq1)
	arq1.close()            
except:
	arq1 =open("./Códigos/PyHotel/dClientes.dat", "wb")
	arq1.close()

try:			#BASEADO NO SLIDE DA AULA DA SEMANA 17
	arq1 = open("./Códigos/PyHotel/dQuartos.dat", "rb")
	quartos = pickle.load(arq1)
	arq1.close()            
except:
	arq1 =open("./Códigos/PyHotel/dQuartos.dat", "wb")
	arq1.close()

i = 1
while i >= 0:
	opcao = menu_inicial()
	while opcao not in ["1", "2", "3", "4", "5", "6"]:
		print()
		print("Opção inválida. Por favor, digite novamente.")
		print()
		opcao = input("Digite o número da opção que desejar: ")
	if opcao in ["1", "2", "3", "4", "5", "6"]:
		os.system("cls || clear")
		if opcao == "1":
			opcao2 = menu_clientes()
			while opcao2 not in ["1", "2", "3", "4", "5"]:
				print()
				print("Opção inválida. Por favor, digite novamente.")
				print()
				opcao2 = input("Digite o número da opção que desejar: ")
			if opcao2 in ["1", "2", "3", "4", "5"]:
				os.system("cls || clear")
				if opcao2 == "1":
					cad_clientes()
				elif opcao2 == "2":
					busc_clientes()
				elif opcao2 == "3":
					edit_clientes()
				elif opcao2 == "4":
					exc_clientes()	
				os.system("cls || clear")
			os.system("cls || clear")	
		elif opcao == "2":
			opcao2 = menu_quartos()
			while opcao2 not in ["1", "2", "3", "4", "5"]:
				print()
				print("Opção inválida. Por favor, digite novamente.")
				print()
				opcao2 = input("Digite o número da opção que desejar: ")
			if opcao2 in ["1", "2", "3", "4", "5"]:
				os.system("cls || clear")
				if opcao2 == "1":
					cad_quarto()
				elif opcao2 == "2":
					busc_quarto()
				elif opcao2 == "3":
					edit_quarto()
				elif opcao2 == "4":
					exc_quarto()	
				os.system("cls || clear")
			os.system("cls || clear")
		elif opcao == "3":
			opcao2 = menu_gestao()
			while opcao2 not in ["1", "2", "3"]:
				print()
				print("Opção inválida. Por favor, digite novamente.")
				print()
				opcao2 = input("Digite o número da opção que desejar: ")
			if opcao2 in ["1", "2", "3"]:
				os.system("cls || clear")
				if opcao2 == "1":
					ger()
				elif opcao2 == "2":
					ver_ger()
				os.system("cls || clear")
			os.system("cls || clear")	
		elif opcao == "4":
			opcao2 = relatorio()
			while opcao2 not in ["1", "2", "3"]:
				print()
				print("Opção inválida. Por favor, digite novamente.")
				print()
				opcao2 = input("Digite o número da opção que desejar: ")
			if opcao2 in ["1", "2", "3"]:
				os.system("cls || clear")
				if opcao2 == "1":
					rel_cli()
				elif opcao2 == "2":
					rel_qua()
				os.system("cls || clear")
			os.system("cls || clear")	
		elif opcao == "5":
			creditos()
			os.system("cls || clear")
		elif opcao == "6":
			encerramento()
			break