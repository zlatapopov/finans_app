import json
client_info={}

def load():
    global client_info
    with open("client_info.json", "r", encoding="utf-8") as json_file:
        client_info = json.load(json_file)
def save():
    global client_info
    with open("client_info.json", "w", encoding="utf-8") as out_file:
        json.dump(client_info, out_file)
def show_info():
    print("Информация о счетах")
    for transaction in client_info["transactions"]:
        print("Счёт:", transaction["account"])
        print("Тип:", transaction["type"])
        print("Дата:", transaction["date"]["year"], transaction["date"]["month"])
        print("Cyммa:", transaction["amount"])
        print("Имя:", client_info["name"])
def predict():
    global client_info
    expenses = 0
    income =  0
    months = []  # список месяцев, в которые происходили операции

    for transaction in client_info["transactions"]:
        if transaction["type"] =="списание":
            expenses += transaction["amount"]
        if transaction["type"] == "зачисление":
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])
    print('Предполагаемые расходы в следующем месяце: ', expenses/len(months))
    print('Предполагаемые доходы в следующем месяце: ', income / len(months))
def suggestions():
    f = open("suggestions.txt", "r", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()
def complain():
    with open("complains.txt", "a", encoding="utf-8") as f:
        p = input("Введите текст жалобы: ")
        f.write( p + "\n")
        print("Ваша жалоба будет рассмотрена в скором времени.")
def make_transaction():
    global client_info
    print("Доступные счета:")
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1
    try:
        account_num = int(input("Введите номер счёта: "))
    except:
        print('Ошибка ввода. Прерываю транзакцию...')
        return
    for i in range(len(client_info['accounts'])):

        if i + 1 == account_num:
            account = client_info['accounts'][i]["number"]
            break
    else:
        print('Такого счёта не существует. Прерываю транзакцию...')
        return
    # new_data = {'account':account}
    # print(new_data)
    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = "списание"
    elif transaction_type == "2":
        transaction_type = "зачисление"
    else:
        print("Такого типа не существует. Прерываю транзакцию...")
        return

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")

    if int(year) > 2023 or int(month) > 12 or int(month) < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return
    try:
        amount = int(input("Введите сумму: "))
    except:
        print('Ошибка ввода. Прерываю транзвкцию...')
        return


    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return
    new_data = {"account": account,
                "type": transaction_type,
                "date": {"year": year, "month": month, "amount": amount}}
    print(new_data)
    if transaction_type == "списание":
        client_info["accounts"][account_num - 1]["balance"] -= amount
    elif transaction_type == "зачисление":
        client_info["accounts"][account_num - 1]["balance"] += amount

    client_info["transactions"].append({"account": account,
                                        "type": transaction_type,
                                        "date": {"year": year, "month": month},
                                        "amount": amount})

    print(client_info['transactions'][-1])
    print(f'Транзакция записана. Текущий баланс на счёте: {client_info["accounts"][account_num - 1]["balance"]}')
# load()
# make_transaction()
# save()
# complain()
# suggestions()
# load()
# show_info()
# predict()


