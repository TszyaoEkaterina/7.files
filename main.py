with open('recipes.txt', 'rt', encoding='utf-8') as recipes:
    cook_book = {}
    while True:
        dish = recipes.readline().strip()
        if dish == '':
            break
        ingredient_number = int(recipes.readline().strip())
        ingredients = []
        i = 0
        while i < ingredient_number:
            ingredient = recipes.readline().split(' | ')
            ingredients.append({'ingredient_name': ingredient[0],
                                'quantity': ingredient[1], 'measure': ingredient[2].strip()})
            i += 1
        cook_book[dish] = ingredients
        recipes.readline()

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for __dish in dishes:
        if __dish not in cook_book:
            return f"cook book doesn't have dish {__dish}"
        for __ingredient in cook_book[__dish]:
            ingredient_name = __ingredient['ingredient_name']
            if ingredient_name not in res:
                res[ingredient_name] = {'measure': __ingredient['measure'],
                                        'quantity': int(__ingredient['quantity']) * person_count}
            else:
                res[ingredient_name]['quantity'] += int(__ingredient['quantity']) * person_count
    return res


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1))
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open('1.txt', encoding='utf-8') as file1:
    data1 = file1.read()
    len1 = len(data1.split('\n'))

with open('2.txt', encoding='utf-8') as file2:
    data2 = file2.read()
    len2 = len(data2.split('\n'))

with open('3.txt', encoding='utf-8') as file3:
    data3 = file3.read()
    len3 = len(data3.split('\n'))

files = {'1.txt': [data1, len1], '2.txt': [data2, len2], '3.txt': [data3, len3]}
files = dict(sorted(files.items(), key=lambda x: x[1], reverse=True))
with open('result.txt', 'w', encoding='utf-8') as res_file:
    for file_name, values in files.items():
        res_file.write(f'{file_name}\n')
        res_file.write(f'{str(values[1])}\n')
        res_file.write(f'{values[0]}\n')
