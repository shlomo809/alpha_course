import json


class bank_costumers:
    def __init__(self, path):
        self.path = path
        json_data = open(path, "r")
        full_costumer_data = json_data.read()
        self.costumer_dict = json.loads(full_costumer_data)
        self.costumer_dict["path"] = self.path
        self.name = self.costumer_dict["name"]
        self.account_number = self.costumer_dict["account_number"]
        self.balance = self.costumer_dict["balance"]

    def __str__(self):
        return str(self.costumer_dict)

    def withdraw_money(self, money):

        self.balance -= money

        self.costumer_dict["balance"] = self.balance

        with open(self.path, "w") as my_file:
            my_file.write(json.dumps(self.costumer_dict))

    def deposit_money(self, money):

        self.balance += money

        self.costumer_dict["balance"] = self.balance

        with open(self.path, "w") as my_file:
            my_file.write(json.dumps(self.costumer_dict))
