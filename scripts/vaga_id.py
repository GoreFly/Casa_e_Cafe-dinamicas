"""
Nov 11 2016 11:15PM

@author: Pedro Garcia
@args: ID do usuário consultado
@return: número de vagas para o usuário com o ID informado
"""


import json
import requests
import sys

try:
    # monta a url correta com o id de usuário fornecido para fazer a consulta
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/" + sys.argv[1] + "/opportunities"
    response = requests.get(url)
    data = response.json()
    # imprime no console o número de entradas para o usuário, sendo cada entrada uma vaga
    print (len(data))

except IndexError:
    # verifica se o id do usuário foi fornecido
    print("ERRO: ID do usuario nao fornecido. Por favor, forneça o ID do usuario como parametro.")
    print("\tpython vaga_id.py [ID]")