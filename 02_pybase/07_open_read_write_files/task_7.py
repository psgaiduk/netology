def get_cook_book(file_recipies):

    cook_book = {}

    with open(file_recipies, encoding='utf-8') as f:
        while True:
            grade = f.readline().rstrip()
            if not grade:
                break
            f.readline()
            vocabulary = []
            for line in f:
                
                if line != '\n':
                    value = line.split('|')
                    vocabulary.append({'ingredient_name': value[0], 'quantity': int(value[1]), 'measure': value[2].rstrip()})
                else:
                    break      
                cook_book[grade] = vocabulary

    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    new_ingredient = {}

    
    if type(dishes) == list:
        dishes_list = dishes
    else:
        dishes_list = []
        dishes_list.append(dishes)


    cook_book = get_cook_book('files/recipes.txt')
    count_dish = 0

    for dish in dishes_list:
        count_dish = dishes.count(dish)
        if dish in cook_book:
            for ingredien in cook_book[dish]:
                new_ingredient[ingredien['ingredient_name']]={'measure': ingredien['measure'], 'quantity': ingredien['quantity'] * person_count * count_dish}
    print(new_ingredient)

get_shop_list_by_dishes('Омлет', 2)

