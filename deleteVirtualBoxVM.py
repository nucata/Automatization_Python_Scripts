import os

def findVirtualBoxToDelete():
	'''
	Archivo en el que se guardarán todas las 
	 url's que contengan 
	 "virtualbox"
	'''
	os.system('sudo find / -name virtualbox* >> virtualboxToDelete.txt')

	'''
	Almaceno el texto en un string
	'''
	with open('virtualboxToDelete.txt', 'r') as f:
		fileContent = f.read()


	'''
	Creo una lista con cada una de las url's
	 por separado y posteriormente 
	 las borro
	'''
	urlList = fileContent.split('\n')
	i = 0
	for url in urlList:
		if 'virtualbox' in url:
			os.system(f'rm -r {url}')

findVirtualBoxToDelete()