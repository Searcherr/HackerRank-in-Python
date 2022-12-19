from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class ColdFoodApp:
    def make_order(self):
        print("ColdFoodApp makes an order")

    def ask_for_preparing_and_delivery(self):
        print("ColdFoodApp ask for cooking meals and it's delivery ")

    def withdraw_and_pay_money(self):
        print("ColdFoodApp withdraws money from the client and sends it to the restaurant and the courier")


class ChiefCooker:

    def applied_sauce(self):
        print("")

    def add_topping_to_pizza(self):
        print("")

    def bon_appetit(self):
        print("")

class Courier:
    def pick_up_order(self):
        print("The courier picks up the order")

    def delivery_order(self):
        print("The courier delivers the order")




class PrepareStoveCommand(ICommand):
    """Класс команды для разогрева печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_stove()


class PrepareDoughCommand(ICommand):
    """Класс команды для подготовки теста пиццы"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()


class PrepareToppingCommand(ICommand):
    """Класс команды для нарезки начинки пиццы"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class PrepareSauceCommand(ICommand):
    """Класс команды для приготовления соуса"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.withdraw_and_pay_money()


class CookingPizzaCommand(ICommand):
    """Класс команды для приготовления пиццы в печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()


class MakePizzaBaseCommand(ICommand):
    """Класс команды для приготовления основы для пиццы"""
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_pizza_base()


class AppliedSauceCommand(ICommand):
    """Класс команды для нанесения соуса на пиццу"""
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.applied_sauce()


class AddToppingCommand(ICommand):
    """Класс команды для добавления начинки на пиццу"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()


class BonAppetitCommand(ICommand):
    """Класс команды для пожелания клиенту
       приятного аппетита"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.bon_appetit()


class Pizzeria:
    """Класс агрегации всех команд для приготовления
       пиццы"""
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Не задана очередность выполнения"
                  " команд приготовления пиццы")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = ChiefCooker()
    assistant = ChiefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # формируем последовательность команд для приготовления пиццы
    pizzeria.addCommand(PrepareDoughCommand(assistant))
    pizzeria.addCommand(MakePizzaBaseCommand(chief))
    pizzeria.addCommand(PrepareSauceCommand(assistant))
    pizzeria.addCommand(AppliedSauceCommand(chief))
    pizzeria.addCommand(PrepareStoveCommand(stove))
    pizzeria.addCommand(PrepareToppingCommand(assistant))
    pizzeria.addCommand(AddToppingCommand(chief))
    pizzeria.addCommand(CookingPizzaCommand(stove))
    pizzeria.addCommand(BonAppetitCommand(chief))
    # запускаем процесс приготовления пиццы
    pizzeria.cook()