import json
import os
import socket
import random
from Bank_Costumer import bank_costumers
import time

list_of_costumers = {}


class Bank:
    def __init__(self):

        path_json = 'C:/Users/Shlomo/Desktop/alpha_course/bank/costumers'
        json_files = [pos_json for pos_json in os.listdir(
            path_json) if pos_json.endswith('.json')]

        for account_path in json_files:
            costumer_path = "costumers/"+account_path
            costumers = bank_costumers(costumer_path)
            list_of_costumers[costumers.account_number] = costumers

    def start_listen(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((self.HOST, self.PORT))
        my_socket.listen()
        print(self.PORT)
        while(True):

            conn, addr = my_socket.accept()
            json_received = conn.recv(1024).decode('utf-8')
            dict_name = json.loads(json_received)

            if(dict_name['action_code'] == 1):
                account_number = random.randint(1000, 9999)
                dict_name["account_number"] = account_number
                dict_name.pop('action_code', None)

                self.Create_account(
                    dict_name['account_number'], dict_name, conn)
            elif(dict_name['action_code'] == 2):
                dict_name.pop('action_code', None)

                self.withdraw_money(
                    dict_name['account_number'], dict_name['balance'], conn)
            elif(dict_name['action_code'] == 3):
                dict_name.pop('action_code', None)

                self.transfer_Money(
                    dict_name['account_number'], dict_name['recipient_account_number'], dict_name['balance'], conn)
            elif(dict_name['action_code'] == 4):
                dict_name.pop('action_code', None)

                self.deposit_money(
                    dict_name['account_number'], dict_name['balance'], conn)

        my_socket.close()

    def Create_account(self, account_number, create_dict, conn):

        path = f"costumers/{account_number}.json"

        with open(path, "w") as my_file:
            create_dict["path"] = path
            my_file.write(json.dumps(create_dict))
            list_of_costumers[account_number] = create_dict
        data = json.dumps(create_dict)

        conn.sendall(bytes(data, 'utf-8'))

    def withdraw_money(self, account_number, money, conn):

        list_of_costumers[account_number].withdraw_money(money)
        data = json.dumps(list_of_costumers[account_number].costumer_dict)

        conn.sendall(bytes(data, 'utf-8'))

    def deposit_money(self, account_number, money, conn):

        list_of_costumers[account_number].deposit_money(money)
        data = json.dumps(list_of_costumers[account_number].costumer_dict)

        conn.sendall(bytes(data, 'utf-8'))

    def transfer_Money(self, account_number, recipient_account_number, money, conn):

        for find_account in list_of_costumers:

            if(find_account == recipient_account_number):

                list_of_costumers[account_number].withdraw_money(money)
                list_of_costumers[recipient_account_number].deposit_money(
                    money)

                data = json.dumps(
                    list_of_costumers[account_number].costumer_dict)

                conn.sendall(bytes(data, 'utf-8'))
                break
        data = f"account number {recipient_account_number} was not found"

        conn.sendall(bytes(data, 'utf-8'))
