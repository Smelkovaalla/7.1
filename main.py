cook_book = {}
ingredient = {}
reciept = []

with open('recipes.txt') as file:
  for line in file:
    dish = line.strip()
    print(dish)
    cook_book[dish] = ''
    num = int(file.readline().strip())

    for i in range(num):
      ingredient_list = file.readline().strip().split('|')
      print(ingredient_list)

      ingredient['ingredient_name'] = ingredient_list[0]
      ingredient['quantity'] = ingredient_list[1]
      ingredient['measure'] = ingredient_list[2]
      reciept.append(ingredient)
      ingredient = {}
    
    cook_book[dish] = reciept
    reciept = []
    file.readline()
    print()
      


print(cook_book)

# get_shop_list_by_dishes(dishes, person_count)

dishes = ['Запеченный картофель', 'Омлет'] 
person_count = 2

