from pyspark.sql import SparkSession
import smbclient
import urllib
from smb.SMBHandler import SMBHandler
import base64
import shutil
from smb.SMBConnection import SMBConnection
import subprocess
from io import BytesIO


#pega os dados do arquivo conectado por samba
opener = urllib.request.build_opener(SMBHandler)
fh = opener.open('smb://192.168.1.115/home/pokedexM2')
data = fh.read()

#local onde sera armazenado os dados do arquivo
local_dest = "/home/temp.txt"


#armazena os dados no arquivo da maquina mestre
with open(local_dest, "wb") as local_file:
    local_file.write(data)
 

#recupera o arquivo salvo na maquina e o pega para realizar verificacoes
arq = open("/home/temp.txt", "r")
conteudo = arq.read()

vetor0 = ["1","2","3","4","5","6","7","8","9"]
vetor = []

for line in conteudo:
    if (line >= "1" and line <= "9"):
       vetor.append(line)

ordenado = vetor == sorted(vetor0)

if(ordenado):
  print("Arquivo com sequencia correta!")
  fh.close()
else:
  print("Sequencia Incorreta.")
 
  #fecha o arquivo fh
  fh.close()


  #abrindo o arquivo que contem a ordem correta
  arq = open("/home/codigo.py", 'rb')
  arqC = arq.read()
  arquivoC = BytesIO(arqC)


  #realiza a escrita dos dados na ordem correta no arquivo da maquina do cluster
  opener = urllib.request.build_opener(SMBHandler)
  fh2 = opener.open('smb://192.168.1.115/home/pokedexM2', data=arquivoC)

  #fecha o arquivo fh2
  fh2.close()

  print("Alteracao Realizada!")
