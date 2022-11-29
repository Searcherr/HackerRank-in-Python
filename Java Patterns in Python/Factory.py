class Cake():
    def __int__(self):
        pass

    def foodType(self):
        return 'a Dessert'

class Pizza():
    def __int__(self):
        pass

    def foodType(self):
        return 'Fast Food'


class FoodFactory:
    def getFood(self, name):
        if name == 'cake':
            return Cake()
        elif name == 'pizza':
            return Pizza()


menu = ('cake', 'pizza')

client_order = input('Place your order: cake or pizza')
if client_order not in menu:
    print('There is no such a meal in the Menu')
else:
    order = FoodFactory().getFood(client_order)
    class_name = order.__class__.__name__
    print(f"The factory returns class {class_name}")
    print(f"Someone ordered {order.foodType()}")