# Cluster Spark

O Apache Spark é um framework de processamento distribuído projetado para lidar com grandes volumes de dados. Essa aplicação é conhecida por ser fortemente escalável e pelo alto desempenho para processamento e análise de dados em tempo real ou em lote.

Usando o Spark é possível trabalhar com processamento de dados em lote, machine learning, processamento de dados em tempo real, processamento de grafos, processamento de dados SQL, e etc.

O objetivo do projeto é acessar um arquivo de texto numerado de forma desordenada de 1 a 9 em um nó de trabalho presente em um cluster construído a partir do Spark. A máquina mestre do cluster possui um arquivo de backup com a ordem correta dos dados do arquivo. Ao acessar o arquivo no nó de trabalho do cluster, a máquina mestre verifica se o arquivo está ordenado corretamente, caso esteja desordenado, ela realiza a cópia do arquivo correto para a máquina com o arquivo desordenado, substituindo os dados do arquivo incorreto.

## **Ambiente virtual**

Este tutorial apresenta os passos necessários para criar um cluster utilizando Spark. Primeiramente é necessário preparar o ambiente onde serão projetadas as máquinas virtuais para a elaboração do projeto. Neste tutorial optou-se por utilizar o virtualbox para criar as máquinas virtuais do cluster.

O virtualbox pode ser baixado por aqui: <https://www.virtualbox.org/>

##  **Sistema operacional das máquinas virtuais**



No cluster Spark proposto foram projetadas duas máquinas virtuais, onde a primeira delas utiliza o ubuntu server 20.04 LTS: <https://ubuntu.com/download/server>[ ](https://ubuntu.com/download/server), sendo esta a máquina mestre do servidor. 

Já a segunda máquina utiliza o Lubuntu 20.04 LTS como sistema operacional: <https://lubuntu.me/focal-released/>[ ](https://lubuntu.me/focal-released/). A escolha dos sistemas operacionais ficam a cargo do usuário.

Logo após criar as máquinas virtuais e instalar os sistemas operacionais, será necessário realizar a instalação dos softwares que serão necessários para construir o cluster.

##  **Spark**

Para instalar o Spark é necessário possuir o Java e o Scala instalados em ambas as máquinas, é possível realizar a instalação pelos comandos:

>  sudo apt update

>  sudo apt install default-jre

>  sudo apt search scala

>  sudo apt install scala

Para instalar o Spark, pode se usar os seguintes comandos para baixa-lo, extraí-lo e movê lo ao diretório /opt/spark:

>wget **https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz**

>tar -xvzf spark-3.4.0-bin-hadoop3.tgz

>sudo mv spark-3.4.0-bin-hadoop3 /opt/spark

Após concluir a instalação é necessário definir algumas configurações, usando os comandos abaixo:

> echo "export SPARK\_HOME=/opt/spark" >> ~/.profile

> echo "export PATH=$PATH:/opt/spark/bin:/opt/spark/sbin" >> ~/.profile

> echo "export PYSPARK\_PYTHON=/usr/bin/python3" >> ~/.profile



Para garantir que essas novas variáveis de ambiente sejam acessíveis no shell e disponíveis para o Apache Spark, também é obrigatório executar o seguinte comando para que as alterações recentes entrem em vigor.

> source ~/.profile

Seguindo esses passos, já será possível acessar os serviços do Spark por:

> start-master.sh

> start-workers.sh spark://localhost:7077

Sendo o primeiro responsável por abrir a conexão mestre e o segundo a conexão dos nós de trabalho. É possível verificar se o serviço foi iniciado corretamente acessando: <http://localhost:8080/>[ ](http://localhost:8080/). Caso tenha iniciado corretamente, você verá a tela do Spark apresentada abaixo:

![Maquinas Conectadas](/medias/maquinasconectadas.png)

##  **Samba e PySpark**

Além do Spark é necessário instalar os utilitários Samba e PySpark. O Samba é um software de código aberto que implementa o protocolo SMB/CIFS, para integrar a conexão entre a máquina mestre e os demais nós da rede. Para instalá-lo, basta utilizar os comando abaixo, ele deve ser instalado em ambas as máquinas:

> sudo apt install samba

Após a instalação é necessário realizar algumas configurações em ambas as máquinas, acessando o arquivo de configuração do Samba:

> sudo nano /etc/samba/smb.conf

Dentro do arquivo, você pode definir suas configurações de compartilhamento de diretórios e permissões. Por exemplo, você pode adicionar o seguinte bloco no final do arquivo para compartilhar uma pasta chamada "compartilhamento". 

![](/medias/1.png)


No código disponibilizado o caminho escolhido para a pasta compartilhada, foi a pasta “home”, tanto na máquina mestre quanto na outra máquina. Além disso os arquivos que serão escritos e copiados também foram colocados nessa pasta.

Salve o arquivo e saia do editor de texto e reinicie o serviço Samba:

> sudo service smbd restart

Na pasta home da máquina mestre foram criados os seguintes arquivos de texto:


> pokedex\_original: que contém a ordenação correta dos nomes, numerados de 1 a 9.

> temp.txt: que será utilizado como arquivo temporário para armazenar o texto do arquivo incorreto que está na segunda máquina do cluster

Na pasta home da segunda máquina foram criados os seguintes arquivos de texto:

> pokedexM2: que contém a ordenação incorreta dos nomes, numerados de forma aleatória de 1 a 9.

Crie os arquivos nestes locais e os modifique de acordo com a ideia do seu projeto.

**Obs:** Ao tentar utilizar o samba, o sistema pode solicitar o uso do smbclient, ele pode ser instalado pelo comando:

> sudo apt install smbclient

Para instalar o PySpark, utilize o comando:

> pip install pyspark

Ao realizar todos os passos anteriores, será possível iniciar o PySpark e abrir o código disponibilizado neste servidor:

> pyspark


Seguindo esses passos, será possivel realizar o uso da aplicação de ordenação de arquivos. O seguinte link apresenta um vídeo com o funcionamento da aplicação: https://github.com/jeanlucamtp12/Cluster-Spark/blob/main/medias/video.mp4

