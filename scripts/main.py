"""
Nov 11 2016 11:15PM

@author:    Pedro Garcia
@args:      [1] Função desejada (GET ou POST)
            [2] ID do usuário
@return:    Número de status do POST ou número de vagas para o usuário com o ID informado
"""

from rest_api import GET, POST
import sys

if sys.argv[1] == "GET":
    try:
        print(GET(sys.argv[2]))
    except IndexError:
        print("ERRO: ID do usuário não inserido. Por favor, insira o ID.")
        print("\t\tpython main.py GET [userID]")
elif sys.argv[1] == "POST":
    print(POST())
else:
    print("ERRO: " + sys.argv[1] + "nao reconhecido. Use GET ou POST.")