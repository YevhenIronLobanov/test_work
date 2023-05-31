class Car:
    '''Модель автомобіля'''
    def __init__(self, model, color, engine_cap):
        '''Ініціалізуємо атрибути '''
        self.model = model
        self.color = color
        self.engine_cap = engine_cap

    def headway(self):
        '''Авто рухається вперед'''
        print(f'{self.model} - рух вперед.')

    def car_back (self):
        '''Авто рухається назад'''
        print(f'{self.model} - рух назад.')

class Avtotruck (Car):
    '''Модель вантажно автомобіля, яка є успадкованою від першої моделі авто'''
    def turn_right (self):
        '''Авто рухається праворуч'''
        print(f'{self.model} - рух праворуч')

    def turn_left (self):
        '''Авто рухається ліворуч'''
        print(f'{self.model} - рух ліворуч')

my_car = Car('BMW M8', 'black', '4.4')
truck = Avtotruck ('Mercedes-Benz Acros', 'white', '12.8')
'''Створено екземпляри класів'''

print(my_car.model, my_car.color, my_car.engine_cap)
print(truck.model, truck.color, truck.engine_cap)
'''Звернення до екземплярів'''

my_car.headway()
my_car.car_back()

truck.headway()
truck.car_back()
truck.turn_right()
truck.turn_left()
'''Визов методів'''
