import re
from Product import product
class costumer:
    def __init__(self,costumer_name,costumer_shopping_list,costumer_total_buy):
        self.costumer_name=costumer_name
        self.costumer_shopping_list=costumer_shopping_list
        self.costumer_total_buy=costumer_total_buy
    def add_product(self):
        product_name = input(
                "what is the name of the product thet you want?\n")
        product_price = input("what is the price?\n")
        product_amount = input("how much do you want from it?\n")
        while(not(re.fullmatch("[0-9]+(\.[0-9])?",product_amount) and (re.fullmatch("[0-9]+(\.[0-9])?",product_price ))) ):
            print("please inpute a number")
            product_price = input("what is the price?\n")
            product_amount = input("how much do you want from it?\n")   
        product_price=float(product_price)
        product_amount=float(product_amount)
        if (product_name in self.costumer_shopping_list):
                print("this product is already Exists\n")
                self.costumer_shopping_list[product_name]["amount"] += product_amount
                self.costumer_total_buy=self.costumer_shopping_list[product_name]["amount"]*self.costumer_shopping_list[product_name]["price"]

        else:
            product_name = product(product_name,product_price,product_amount)
            self.costumer_shopping_list[product_name.product_name] = {"price": product_price, "amount": product_amount}
            self.costumer_total_buy+=product_name.cost()
            print(self.costumer_shopping_list)
          
    def remove_product(self):
            print( self.costumer_shopping_list)
            if( self.costumer_shopping_list == {}):
                print("you have no item in your cart plz buy somthing")
                

            product_name_remove = input("what product you want to remove?\n")
            if (product_name_remove in self.costumer_shopping_list):
                product_amount_remove = int(input("how meny item you want to remove from it?\n"))
                if(product_amount_remove<0):
                    print("you put an invalid number(negative)plz enter a notmal number")
                elif(product_amount_remove >=  self.costumer_shopping_list[product_name_remove.product_name_remove]["amount"]):
                    self.costumer_total_buy-= product_name_remove.cost()
                    del  self.costumer_shopping_list[product_name_remove.product_name_remove]
                    print( self.costumer_shopping_list)
                else:
                    self.costumer_shopping_list[product_name_remove.product_name_remove]["amount"] -= product_amount_remove
                    self.costumer_total_buy-= product_name_remove.cost()
                    print( self.costumer_shopping_list)
            else:
                print("this product is not in the shopping list,this is what you have:")

                print( self.costumer_shopping_list) 