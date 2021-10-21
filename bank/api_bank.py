import socket
import json



class Actions:
    CREATE_ACCOUNT = 1
    Withdraw_Money = 2
    transfer_Money = 3
    Deposit_Money = 4


HOST = "127.0.0.1"
PORT = 23456
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((HOST, PORT))


def Create_account(name, firse_balance):

    client = {"action_code": Actions.CREATE_ACCOUNT,
              "name": name, "balance": firse_balance}
    jj = json.dumps(client)
    my_socket.sendall(bytes(jj, 'utf-8'))
    datd = my_socket.recv(1024)

    print(str(datd))

def withdraw_money(name, account_number, money):
    client = {"action_code": Actions.Withdraw_Money, "name": name,
              "balance": money, "account_number": account_number}
    jj = json.dumps(client)
    my_socket.sendall(bytes(jj, 'utf-8'))
    datd = my_socket.recv(1024)

    print(str(datd))

def transfer_Money(name, account_number, money, recipient_account_number):
    client = {"action_code": Actions.transfer_Money, "name": name, "balance": money,
              "account_number": account_number, 'recipient_account_number': recipient_account_number}
    jj = json.dumps(client)
    my_socket.sendall(bytes(jj, 'utf-8'))
    datd = my_socket.recv(1024)

    print(str(datd))

def deposit_money(name, account_number, money):
    client = {"action_code": Actions.Deposit_Money, "name": name,
              "balance": money, "account_number": account_number}
    jj = json.dumps(client)
    my_socket.sendall(bytes(jj, 'utf-8'))
    datd = my_socket.recv(1024)
    print(str(datd))



