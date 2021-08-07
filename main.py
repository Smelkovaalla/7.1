from pprint import pprint
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
      


pprint(cook_book)
print()

def get_shop_list_by_dishes(dishes, person_count):
  products_list = []
  for dish in dishes:
    i = 0
    while i < len(cook_book[dish]):
      products_list.append(cook_book[dish][i])
      i += 1

  pprint('products_list:')
  pprint(products_list)
  print()
  products_dict = {}
  quantity_dict = {}


  for product in products_list:
    name = product['ingredient_name']
    if name in products_dict.keys():  
      products_dict[name]['quantity'] = int(products_dict[name]['quantity']) + int(product['quantity'])
    else:
      products_dict[name] = product

  for pro in products_dict.values():
    del pro['ingredient_name']
    pro['quantity'] = int(pro['quantity']) * person_count

  pprint(f'products_dict на {person_count} персоны:')
  return products_dict


pprint(get_shop_list_by_dishes(['Фахитос', 'Фахитос', 'Омлет'], 2))

