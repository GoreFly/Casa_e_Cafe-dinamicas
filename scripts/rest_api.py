import requests
from util import POST_GenData


def GET(id):
    try:
        # monta a url correta com o id de usuário fornecido para fazer a consulta
        url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/" + str(id) + "/opportunities"
        response = requests.get(url)
        data = response.json()
        # imprime no console o número de entradas para o usuário, sendo cada entrada uma vaga
        return (len(data))

    except IndexError:
        # verifica se o id do usuário foi fornecido
        print("ERRO: ID do usuario nao fornecido. Por favor, forneça o ID do usuario como parametro.")
        print("\tpython rest_api.py GET [ID]")
        return (-1)


def POST():
    # monta a url correta com o id de usuário fornecido para fazer a consulta
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/opportunities"
    data = POST_GenData()
    request = requests.post(url, json=data)
    return (request.status_code, request.reason)
