# product store problem practice
# 1.create and design an online store for products(name,price).
# 2.track total products being created
# 3.create a static method to calculate discount on each product based on a % parameter

class product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count += 1

    @classmethod
    def get_count(cls):
        print(f"count is: {cls.count}")


    def get_product_info(self):
            print(f"product name is: {self.name} and price is: {self.price}")

    @staticmethod
    def calculate_discount(price,discount):
        final_price = price -(discount*price/100)
        print(f"final price is: {final_price}")


p1 = product("laptop",50_000)
p2 = product("phone",10_000)
p1.get_product_info()
product.get_count()
product.calculate_discount(p1.price,10)
    
