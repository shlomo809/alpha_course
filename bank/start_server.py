from bank import Bank
import socket

def main():
    HOST = "127.0.0.1"
    PORT = 23456
    
    costimer = Bank()
    costimer.start_listen(HOST,PORT)

if(__name__=="__main__"):
    main()
