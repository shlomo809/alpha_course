def main():
    shopping = {}
    x = 0
    price_so_far = 0
    while(x == 0):
        number = input("Enter 1 for buying stuff, 2 for removing them or 3 if you are done with the shopping:")
        if(number.isalpha()):
            print("please enter a number\n")
            continue
        number=int(number)
        if(number == 3):
            x = 1
            print("thank you for buying the total cost is:", price_so_far)

        elif(number == 1):
            print(shopping)
            prodact_name = input("what is the name of the prodact thet you want?\n")
            prodact_price = int(input("what is the price?\n"))
            prodact_amount = int(input("how much do you want from it?\n"))
            if (prodact_name in shopping):
                print("this prodact is alredy Exists\n")
                shopping[prodact_name]["amount"] += prodact_amount
                price_so_far=shopping[prodact_name]["amount"]*shopping[prodact_name]["price"]

            else:
                shopping[prodact_name] = {"price": prodact_price, "amount": prodact_amount}
                price_so_far+=shopping[prodact_name]["amount"]*shopping[prodact_name]["price"]

        elif(number == 2):
            print(shopping)
            if(shopping == {}):
                print("you have no item in your cart plz buy somthing")
                continue

            prodact_name_remove = input("what prodect you want to remove?\n")
            if (prodact_name_remove in shopping):
                prodact_amount_remove = int(input("how meny item you want to remove from it?\n"))
                if(prodact_amount_remove<0):
                    print("you put an invalid number(negative)plz enter a notmal number")
                elif(prodact_amount_remove >= shopping[prodact_name_remove]["amount"]):
                    price_so_far-=shopping[prodact_name_remove]["amount"]*shopping[prodact_name_remove]["price"]
                    del shopping[prodact_name_remove]
                    print(shopping)
                else:
                    shopping[prodact_name_remove]["amount"] -= prodact_amount_remove
                    price_so_far-=shopping[prodact_name_remove]["amount"]*shopping[prodact_name_remove]["price"]
                    print(shopping)
            else:
                print("this prodact is not in the shopping list,this is what you have:")

                print(shopping)
        else:
            print("plese enter a valid number")
        print("the price so far is:", price_so_far)


if (__name__ == "__main__"):
    main()
