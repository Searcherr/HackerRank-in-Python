from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Executors' classes
class ColdFoodApp:
    def make_order(self):
        print("ColdFoodApp makes an order")

    def ask_for_preparing_and_delivery(self):
        print("ColdFoodApp ask for cooking meals and it's delivery ")

    def withdraw_and_pay_money(self):
        print("ColdFoodApp withdraws money from the client "
              "and sends it to the restaurant and the courier")


class Restaurant:
    def get_order(self):
        print("The restaurant receives an order through the app")

    def cook_meals(self):
        print("The restaurant cooks ordered meals")

    def hand_ordet_to_courier(self):
        print("The restaurant hands meals to the courier")


class Courier:
    def pick_up_order(self):
        print("The courier picks up the order")

    def delivery_order(self):
        print("The courier delivers the order")


# ColdFoodApp commands
class MakeOrderAppCommand(ICommand):
    def __init__(self, executor: ColdFoodApp):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_order()


class AskPrepareDeliveryCommand(ICommand):
    def __init__(self, executor: ColdFoodApp):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.ask_for_preparing_and_delivery()


class WithdrawAndPayCommand(ICommand):
    def __init__(self, executor: ColdFoodApp):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.withdraw_and_pay_money()


# Restaurant commands
class GetOrderCommand(ICommand):
    def __init__(self, executor: Restaurant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.get_order()


class CookMealsCommand(ICommand):
    def __init__(self, executor: Restaurant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cook_meals()


class HandOrderToCourierCommand(ICommand):
    def __init__(self, executor: Restaurant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.hand_ordet_to_courier()


# Courier commands
class PickUpCommand(ICommand):
    def __init__(self, executor: Courier):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.pick_up_order()


class DeliveryCommand(ICommand):
    def __init__(self, executor: Courier):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.delivery_order()


# Class of ColdFood's delivery meals system
class ColdFoodSystem:
    def __init__(self):
        self.history: List[ICommand] = []

    def add_command(self, command: ICommand) -> None:
        self.history.append(command)

    def make_money(self) -> None:
        if not self.history:
            print("The sequence of commands is empty")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    cold_food_app = ColdFoodApp()
    restaurant = Restaurant()
    courier = Courier()
    cold_food_system = ColdFoodSystem()
    # Creating a sequence of commands
    cold_food_system.add_command(MakeOrderAppCommand(cold_food_app))
    cold_food_system.add_command(AskPrepareDeliveryCommand(cold_food_app))
    cold_food_system.add_command(GetOrderCommand(restaurant))
    cold_food_system.add_command(CookMealsCommand(restaurant))
    cold_food_system.add_command(HandOrderToCourierCommand(restaurant))
    cold_food_system.add_command(PickUpCommand(courier))
    cold_food_system.add_command(DeliveryCommand(courier))
    cold_food_system.add_command(WithdrawAndPayCommand(cold_food_app))
    # Let's make some money
    cold_food_system.make_money()