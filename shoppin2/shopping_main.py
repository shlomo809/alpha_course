from Costumer import costumer
from Register import register
import json


def main():
    costumers = {}
    shopping = {}
    store_open = True
    print("hello there lets crate you a new account\n")
    open_register = 't'
    while(store_open):
        name = input("please enter your name\n")
        end_of_purchase = True
        if(open_register == 't'):
            new_register = register()
            costumers={}
        if(name not in costumers):
            shopping = {}
            new_costumer = costumer(name, shopping, 0)
            costumers[name] = new_costumer.costumer_shopping_list
            
        
            
        while(end_of_purchase):
            option = (input("add 1 remove 2 or 3 for checkout"))
            if(option == '1'):
                new_costumer.add_product()
            elif(option == '2'):
                new_costumer.remove_product()
            elif (option == '3'):
                end_of_purchase = False
            else:
                print("your inpute is invaild")    
        for key in shopping:
            print(shopping[key]["price"])
            with open("./item/"+key+".json", "w")as my_file:
                my_file.write(json.dumps(shopping))

        new_register.Check_out_costumer(
            new_costumer.costumer_shopping_list, new_costumer.costumer_total_buy)
        
        
        new_register.Print_summery(costumers)
        store_open = (
            input("dose the store empty?(0 for yes, anything else for no)\n"))
        if(store_open == '0'):
            store_open = False
        else:
            print("hello there lets crate you a new account\n")
            open_register = input("do you want to go to another register or stay in this one?(true for yes n for no)\n")


if(__name__ == "__main__"):
    main()
