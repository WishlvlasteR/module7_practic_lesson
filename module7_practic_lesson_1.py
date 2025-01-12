class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """Считывает информацию из файла и возвращает содержимое как строку."""
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        """Добавляет новые продукты в файл, если их ещё нет."""
        current_products = self.get_products()

        file = open(self.__file_name, 'a')
        for product in products:
            if f"{product.name}, " in current_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file.write(str(product) + '\n')
        file.close()


# Пример результата выполнения программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())