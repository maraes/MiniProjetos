import os
import shutil
import unidecode

path = r'.'
cont = 0

lista = []
for root, dirs , arquivos in os.walk('.'):
	
	for diretorio in dirs:
		lista.append(diretorio)
	


while 1:
		
	classe = input('Digite a classe: ')
	if not os.path.exists(classe):
		new_path = os.makedirs(classe)


	for root , dirs , arquivos in os.walk(path):
		
		for arquivo in arquivos:
			if arquivo.endswith('.pdf'):
				arquivo = unidecode.unidecode(arquivo)
				classe = unidecode.unidecode(classe)
								
				
				if classe.lower() in arquivo.lower():
						
					old  = os.path.join(root,arquivo)
					for diretorio in lista:
						if diretorio == classe:
							new  = os.path.join(classe,arquivo)
					
							shutil.move(old , new)
							cont = cont + 1
							print(f'Copiados: {cont}')
		else:
			try:
				os.rmdir(classe)
			except:
				pass		
			


