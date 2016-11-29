"""
Nov 11 2016 11:15PM

@author:    Pedro Garcia
@args:      [1] Função desejada (GET ou POST)
            [2] ID do usuário
@return:    201 (POST SUCCESS) ou número de vagas para o usuário com o ID informado (GET SUCCESS)
"""


import json
import requests
import sys

def GET(id):
    try:
        # monta a url correta com o id de usuário fornecido para fazer a consulta
        url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/" + id + "/opportunities"
        response = requests.get(url)
        data = response.json()
        # imprime no console o número de entradas para o usuário, sendo cada entrada uma vaga
        print (len(data))

    except IndexError:
        # verifica se o id do usuário foi fornecido
        print("ERRO: ID do usuario nao fornecido. Por favor, forneça o ID do usuario como parametro.")
        print("\tpython rest_api.py GET [ID]")


def POST():
    # monta a url correta com o id de usuário fornecido para fazer a consulta
    url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/opportunities"
    data = POST_GenData()
    request = requests.post(url, data)
    print (request.status_code, request.reason)
    print (request.text[:500])

def POST_GenData():
    data = {}
    print("INFORMACOES DA VAGA")
    data["id"] = input("id <- ")
    data["title"] = input("title <- ")
    data["description"] = input("description <- ")
    data["created_at"] = input("created_at <- ")
    data["is_contact_available"] = "true" if (input("is_contact_available? [y/n] <- ") == "y") else "false"
    data["is_active"] = "true" if (input("is_active? [y/n] <- ") == "y") else "false"
    print("\nINFORMACOES DO EMPREGADOR")
    hirer = {}
    hirer["id"] = input("id <- ")
    hirer["name"] = input("name <- ")
    hirer["account_type"] = input("account_type <- ")
    hirer["cnpj"] = input("cnpj <- ")
    hirer["company_contact_name"] = input("company_contact_name <- ")
    hirer["phone"] = input("phone <- ")
    hirer["email"] = input("email <- ")
    hirer["mobile_phone"] = input("mobile_phone <- ")
    hirer["is_plan_active"] = "true" if (input("is_plan_active? [y/n] <- ") == "y") else "false"
    data["hirer"] = hirer
    print("\nINFORMACOES DO LOCAL")
    location = {}
    location["neighborhood"] = input("neighborhood <- ")
    location["address"] = input("address <- ")
    location["address_type"] = input("address_type <- ")
    location["latitude"] = input("latitude <- ")
    location["longitude"] = input("longitude <- ")
    location["city_id"] = input("city_id <- ")
    location["city"] = input("city <- ")
    location["zipcode"] = input("zipcode <- ")
    location["state"] = input("state <- ")
    data["location"] = location
    print("\nETC")
    data["frequency"] = input("frequency <- ")
    data["is_automatic"] = "true" if (input("is_automatic? [y/n] <- ") == "y") else "false"
    data["score"] = input("score <- ")
    category = {}
    category["id"] = input("category id <- ")
    category["name"] = input("category name <- ")
    data["category"] = category
    data["salary_requirements"] = input("salary_requirements <- ")
    data["characteristics"] = []
    data["starts"] = input("starts <- ")
    data["amount_candidates"] = input("amount_candidates <- ")
    data["amount_visualizations"] = input("amount_visualizations <- ")
    data["feedback"] = input("feedback <- ")
    data["salary_research"] = input("salary_research <- ")
    data["relevancy"] = input("relevancy <- ")
    return data


POST()