

class Animal:
    action = 'Накормить'
    info = []

    def __init__(self, weight, name):
        self.name = name
        self.weight = weight
        Animal.info.append([self.name, self.weight, self.type_animal])

    def action_animal(self):
        print(self.action + ' и ' + self.act)

class Duck(Animal):
    type_animal = 'Утка'
    act = 'собрать яйца'
    say = 'Кря-кря'

class Cow(Animal):
    type_animal = 'Корова'
    act = 'подоить'
    say = 'Мууу'

class Sheep(Animal):
    type_animal = 'Овца'
    act = 'подстричь'
    say = 'Бееее'

class Chicken(Animal):
    type_animal = 'Курица'
    act = 'собрать яйца'
    say = 'Кудахчет'

class Goat(Animal):
    type_animal = 'Коза'
    act = 'подстричь'
    say = 'Беее'

class Goose(Animal):
    type_animal = 'Гусь'
    act = 'собрать яйца'
    say = 'Га-га'

def sum_weight():
    sum_weight = 0
    print('Считаем вес всех животных')
    input_type_animal = input('Введите вид животного (all - для веса всех животных): ')
    for weight in Animal.info:
        if input_type_animal.lower() == 'all':
            sum_weight += weight[1]
        else:
            if weight[2].lower() == input_type_animal.lower():
                sum_weight += weight[1]
    return(f'Cуммарный вес составляет: {sum_weight}кг')

def max_weight():
    print('Ищем самое тяжелое животное')
    max_weight = 0
    name_max_weight = ''
    type_animal_max_weight = ''
    input_type_animal = input('Введите вид животного (all - для веса всех животных): ')
    for weight in Animal.info:
        if input_type_animal.lower() == 'all':
            if weight[1] > max_weight:
                max_weight = weight[1]
                type_animal_max_weight = weight[2]
                name_max_weight = weight[0]
        else:
            if input_type_animal.lower() == weight[2].lower():
                if weight[1] > max_weight:
                    max_weight = weight[1]
                    type_animal_max_weight = weight[2]
                    name_max_weight = weight[0]
    return(f'Больше всех весит {type_animal_max_weight.lower()} по имени {name_max_weight}, её вес составляет {max_weight}кг')

grey_goose = Goose(8, 'Серый')
white_goose = Goose(7, 'Белый')
cow_manka = Cow(140, 'Манька')
sheep_barasher = Sheep(50, 'Барашек')
sheep_kudryavii = Sheep(45, 'Кудрявый')
cheeken_coco = Chicken(2, 'Ко-ко')
cheeken_kukareku = Chicken(2, 'Кукареку')
goat_roga = Goat(22, 'Рога')
goat_kopita = Goat(25, 'Копыта')
duck_kryarva = Duck(5, 'Кряква')




print(sum_weight())
print(max_weight())


