def main():
    sum_of_buy = 0
    shopping = {}
    x = 0
    price_so_far = 0
    while(x == 0):

        number = int(input(
            "Enter 1 for buing stuff, 2 for removing them or 3 if you are done with the shopping:"))
        if(number == 3):
            x = 1
            print("thank you for buing the total cost is:", price_so_far)

        if(number == 1):

            prodact_name = input(
                "what is the name of the prodact thet you want?\n")
            prodact_price = int(input("what is the price?\n"))
            prodact_amount = int(input("how much do you want from it?\n"))
            if (prodact_name in shopping):
                print("this prodact is alredy Exists\n")
                shopping[prodact_name]["amount"] += prodact_price

            else:
                shopping[prodact_name] = {
                    "price": prodact_price, "amount": prodact_amount}

        elif(number == 2):
            if(shopping == {}):
                print("you have no item in your cart plz buy somthing")
                continue

            prodact_name_remove = input("what prodect you want to remove?\n")
            if (prodact_name_remove in shopping):
                prodact_amount_remove = int(
                    input("hoe meny item you want to remove from it?\n"))
                if(prodact_amount_remove >= shopping[prodact_name_remove]["amount"]):
                    del shopping[prodact_name_remove]

                else:
                    shopping[prodact_name_remove]["amount"] -= prodact_amount_remove

            else:
                print("this prodact is not in the shopping list,this is what you have:")

                print(shopping)
        else:
            print("plese enter a valid number")
        price_so_far = 0
        for value_list in shopping:
            price_so_far += shopping[value_list]["price"] * \
                shopping[value_list]["amount"]
            print("the price so far is:", price_so_far)


if (__name__ == "__main__"):
    main()
