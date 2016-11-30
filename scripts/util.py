import datetime

def POST_GenData():
    data = {}
    # Leitura dos dados da vaga
    print("INFORMACOES DA VAGA")
    data["id"] = numeric_input(0, "id <- ")
    data["title"] = input("title <- ")
    data["description"] = input("description <- ")
    data["created_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["is_contact_available"] = True if (input("is_contact_available? [y/n] <- ") == "y") else False
    data["is_active"] = True if (input("is_active? [y/n] <- ") == "y") else False

    # Leitura dos dados do empregador
    print("\nINFORMACOES DO EMPREGADOR")
    hirer = {}
    hirer["id"] = numeric_input(0, "id <- ")
    hirer["name"] = input("name <- ")
    hirer["account_type"] = input("account_type <- ")
    hirer["cnpj"] = numeric_input(0, "cnpj <- ")
    hirer["company_contact_name"] = input("company_contact_name <- ")
    hirer["phone"] = input("phone <- ")
    hirer["email"] = input("email <- ")
    hirer["mobile_phone"] = input("mobile_phone <- ")
    hirer["is_plan_active"] = True if (input("is_plan_active? [y/n] <- ") == "y") else False
    data["hirer"] = hirer

    # Leitura dos dados do local referente à vaga
    print("\nINFORMACOES DO LOCAL")
    location = {}
    location["neighborhood"] = input("neighborhood <- ")
    location["address"] = input("address <- ")
    location["address_type"] = input("address_type <- ")
    location["latitude"] = numeric_input(1, "latitude <- ")
    location["longitude"] = numeric_input(1, "longitude <- ")
    location["city_id"] = input("city_id <- ")
    location["city"] = input("city <- ")
    location["zipcode"] = input("zipcode <- ")
    location["state"] = input("state <- ")
    data["location"] = location

    # Leitura de dados extra sobre a vaga
    print("\nETC")
    data["frequency"] = input("frequency <- ")
    data["is_automatic"] = True if (input("is_automatic? [y/n] <- ") == "y") else False
    data["score"] = numeric_input(0, "score <- ")
    category = {}
    category["id"] = numeric_input(0, "category id <- ")
    category["name"] = input("category name <- ")
    data["category"] = category
    data["salary_requirements"] = numeric_input(0, "salary_requirements <- ")
    data["characteristics"] = []
    data["starts"] = input("starts <- ")
    data["amount_candidates"] = numeric_input(0, "amount_candidates <- ")
    data["amount_visualizations"] = numeric_input(0, "amount_visualizations <- ")
    data["feedback"] = input("feedback <- ")
    data["salary_research"] = input("salary_research <- ")
    data["relevancy"] = input("relevancy <- ")
    return data

# Lê um input e o converte para um tipo numérico
#   0 = int
#   1 = float
def numeric_input(cast, prompt):
    value = input(prompt)

    try:
        if   cast == 0: return int(value)
        elif cast == 1: return float(value)
        else: return None
    except:
        return None