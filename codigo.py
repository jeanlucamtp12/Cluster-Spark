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


