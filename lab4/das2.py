class GroceryStore:
    def __init__(delgvvr, name, apples_jijiglen, apple_price, oranges_jijjiglen, orange_price):
        delgvvr.name = name
        delgvvr.apples_sold = apples_jijiglen
        delgvvr.apple_price = apple_price
        delgvvr.oranges_sold = oranges_jijjiglen
        delgvvr.orange_price = orange_price


    def calculate(delgvvr):
        apple = delgvvr.apples_jijiglen * delgvvr.apple_price
        orange = delgvvr.oranges_jijiglen * delgvvr.orange_price
        total = apple + orange
        return total




bambaruush = GroceryStore("Bambaruush", 534, 5000, 487, 10000)
jimshen = GroceryStore("Jimshen", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)


print(f"{bambaruush.name} orlogo: {bambaruush.calculat()}")
print(f"{jimshen.name} orlogo: {jimshen.calculate()} ")
print(f"{fruits.name} orlogo: {fruits.calculate()} ")
