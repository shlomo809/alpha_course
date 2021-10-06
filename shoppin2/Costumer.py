class costumer:
    def __init__(self,costumer_name,costumer_shopping_list,costumer_total_buy):
        self.costumer_name=costumer_name
        self.costumer_shopping_list=costumer_shopping_list
        self.costumer_total_buy=costumer_total_buy
    def add_product(self):
        prodact_name = input(
                "what is the name of the prodact thet you want?\n")
        prodact_price = int(input("what is the price?\n"))
        prodact_amount = int(input("how much do you want from it?\n"))
        if (prodact_name in self.costumer_shopping_list):
                print("this prodact is alredy Exists\n")
                self.costumer_shopping_list[prodact_name]["amount"] += prodact_amount
                self.costumer_total_buy=self.costumer_shopping_list[prodact_name]["amount"]*self.costumer_shopping_list[prodact_name]["price"]

        else:
            self.costumer_shopping_list[prodact_name] = {"price": prodact_price, "amount": prodact_amount}
            self.costumer_total_buy+=self.costumer_shopping_list[prodact_name]["amount"]*self.costumer_shopping_list[prodact_name]["price"]
            print(self.costumer_shopping_list)
          
    def remove_product(self):
            print( self.costumer_shopping_list)
            if( self.costumer_shopping_list == {}):
                print("you have no item in your cart plz buy somthing")
                

            prodact_name_remove = input("what prodect you want to remove?\n")
            if (prodact_name_remove in self.costumer_shopping_list):
                prodact_amount_remove = int(input("how meny item you want to remove from it?\n"))
                if(prodact_amount_remove<0):
                    print("you put an invalid number(negative)plz enter a notmal number")
                elif(prodact_amount_remove >=  self.costumer_shopping_list[prodact_name_remove]["amount"]):
                    self.costumer_total_buy-= self.costumer_shopping_list[prodact_name_remove]["amount"]* self.costumer_shopping_list[prodact_name_remove]["price"]
                    del  self.costumer_shopping_list[prodact_name_remove]
                    print( self.costumer_shopping_list)
                else:
                    self.costumer_shopping_list[prodact_name_remove]["amount"] -= prodact_amount_remove
                    self.costumer_total_buy-= self.costumer_shopping_list[prodact_name_remove]["amount"]* self.costumer_shopping_list[prodact_name_remove]["price"]
                    print( self.costumer_shopping_list)
            else:
                print("this prodact is not in the shopping list,this is what you have:")

                print( self.costumer_shopping_list) 