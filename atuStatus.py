import csv
import os

resultado = []

listaDePDFs = os.listdir("Arquivos")
listaDePDFsAux = []

for item in listaDePDFs:

    listaDePDFsAux.append(item.replace(".pdf",""))

listaDePDFs = listaDePDFsAux

Leitura = open("Novo CODEC (Controle) - TOTVS IP.csv", 'r')

reader = csv.reader(Leitura,delimiter=';')


for linha in reader:
    
    if(linha[2] in listaDePDFs):

        linha[9] = "Concluido"

        resultado.append(linha)
    else:

        resultado.append(linha)

Escrita = open("Resultado.csv", 'a')

escrever = csv.writer(Escrita,delimiter=';', lineterminator="\n")

for item in resultado:

    escrever.writerow(item)