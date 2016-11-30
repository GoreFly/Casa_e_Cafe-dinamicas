"""
Nov 11 2016 11:15PM

@author:    Pedro Garcia
@args:      [1] Função desejada (GET ou POST)
            [2] ID do usuário
@return:    201 (POST SUCCESS) ou número de vagas para o usuário com o ID informado (GET SUCCESS)
"""

from rest_api import GET, POST
import sys

if sys.argv[1] == "GET":
    print(GET(sys.argv[2]))
elif sys.argv[1] == "POST":
    print(POST())
else:
    print("ERRO: " + sys.argv[1] + "nao reconhecido. Use GET ou POST.")
