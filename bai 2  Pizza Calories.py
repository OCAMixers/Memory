# Tính tổng lượng calo của pizza
class Toppings:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    def get_topping_type(self):
        return self.__topping_type

    def set_topping_type(self, topping_type):
        self.__topping_type = topping_type

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    def get_flour_type(self):
        return self.__flour_type

    def set_flour_type(self, flour_type):
        self.__flour_type = flour_type

    def get_baking_technique(self):
        return self.__baking_technique

    def set_baking_technique(self, baking_technique):
        self.__baking_technique = baking_technique

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dough(self):
        return self.__dough

    def set_dough(self, dough):
        self.__dough = dough

    def get_toppings(self):
        return self.__toppings

    def get_toppings_capacity(self):
        return self.__toppings_capacity

    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping):
        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        
        topping_type = topping.get_topping_type()
        topping_weight = topping.get_weight()

        if topping_type in self.__toppings:
            self.__toppings[topping_type] += topping_weight
        else:
            self.__toppings[topping_type] = topping_weight

    def calculate_total_weight(self):
        total_weight = self.__dough.get_weight() + sum(self.__toppings.values())
        return total_weight


# Sửa lỗi trong đoạn mã dưới đây
pizza = Pizza("Margherita", Dough("Wheat", "Baked", 200), 5)
pizza.add_topping(Toppings("Cheese", 50))
pizza.add_topping(Toppings("Tomato", 30))
print(pizza.calculate_total_weight())  # Tính tổng trọng lượng của pizza

