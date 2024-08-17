
class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.number_of_floors_max = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors_max or new_floor < 1:
            print('Такого этажа не существует')
        else:
            self.number_of_floors = new_floor
            print(f'Вы в доме {self.name}, на {self.number_of_floors} этаже')

h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Альбатрос', 10)

print(f'В доме {h1.name}, {h1.number_of_floors} этажей')

h1.go_to(3)
h1.go_to(20)
h1.go_to(-1)
h1.go_to(32)

print(f'В доме {h2.name}, {h2.number_of_floors} этажей\n')

h2.go_to(2)
h2.go_to(9)
h2.go_to(-1)
h2.go_to(16)
