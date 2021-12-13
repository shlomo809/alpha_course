class register:
    def __init__(self):
        self.total_profit = 0
        
    def Check_out_costumer(self,costumer,costumer_debt):
        self.costumer=costumer
        self.costumer_debt=costumer_debt
        self.total_profit+=self.costumer_debt

    def Print_summery(self,register_costumers):
        print("the total profit of this register wasd:",self.total_profit)
        print("the list of the item that this regisret:",register_costumers)