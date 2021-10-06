from Costumer import costumer
import Prodact
from Register import register
import json


def main():
    costumers = {}
    shopping = {}
    store_open = True
    print("hello there lets crate you a new account\n")
    open_register = 't'
    while(store_open):
        name = input("plz enter your name\n")
        end_of_purchase = True
        new_costumer = costumer(name, shopping, 0)
        costumers[name] = new_costumer.costumer_shopping_list
        if(open_register == 't'):
            new_register = register()
            costumers = {}
        while(end_of_purchase):
            option = (input("add 1 remove 2 or 3 for checkout"))
            if(option == '1'):
                new_costumer.add_product()
            elif(option == '2'):
                new_costumer.remove_product()
            elif (option == '3'):
                end_of_purchase = False
        for key in shopping:
            print(shopping[key]["price"])
            with open("./item/"+key+".json", "w")as my_file:
                my_file.write(json.dumps(shopping))

        new_register.Check_out_costumer(
            new_costumer.costumer_shopping_list, new_costumer.costumer_total_buy)
        costumers[name] = new_costumer.costumer_shopping_list
        shopping = {}
        new_register.Print_summery(costumers)
        store_open = (
            input("dose the store empty?(0 for yes, anything else for no)"))
        if(store_open == '0'):
            store_open = False
        else:
            print("hello there lets crate you a new account\n")
            open_register = input("do you want to go to another register or stay in this one?(t for yes n for no)")


if(__name__ == "__main__"):
    main()
