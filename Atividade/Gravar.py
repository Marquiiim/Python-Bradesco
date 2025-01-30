arquivo = open('arqText.txt', 'w')

arquivo.write('Curso de Python \n')
arquivo.write('Aula Prática')
arquivo.close()




leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()