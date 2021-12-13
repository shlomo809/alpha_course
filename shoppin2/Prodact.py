class Product:
    def __init__(self,product_name,product_price,product_amount):
        self.product_name=product_name
        self.product_price=product_price
        self.product_amount=product_amount

    def cost(self):    
        total_cost=self.product_price*self.product_amount
        return total_cost
