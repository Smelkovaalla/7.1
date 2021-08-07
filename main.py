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
  amount = {}

  for product in products_list:   
    name = product['ingredient_name']
    if name in products_dict.keys():  
      amount[name] += 1 
    else:
      amount[name] = 1
      products_dict[name] = product

  print(amount)
  print()

  for ing, pro in products_dict.items():
    del pro['ingredient_name']
    pro['quantity'] = int(pro['quantity']) * int(amount[ing]) * person_count 

  pprint(f'products_dict на {person_count} персоны:')
  return products_dict

pprint(get_shop_list_by_dishes(['Фахитос', 'Фахитос', 'Фахитос', 'Омлет'], 2))

