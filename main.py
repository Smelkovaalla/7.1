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

  # dishes = ['Фахитос', 'Омлет'] 
  # person_count = 2
  products_list = []

  for dish_2 in dishes:
    if dish_2 in cook_book.keys():
      # print(dish_2)
      products_list.append(cook_book[dish_2])

  products_dict = {}
  quantity_dict = {}


  for product in products_list:
    for quantity_dict in product:
      name = quantity_dict.get('ingredient_name')
      if name in products_dict.keys(): 
        quantity_dict['quantity'] = int(quantity_dict['quantity']) * person_count + int(products_dict[name]['quantity'])
        del quantity_dict['ingredient_name']
        products_dict[name] = quantity_dict
      else:
        products_dict[name]= ''
        quantity_dict['quantity'] = int(quantity_dict['quantity']) * person_count
        del quantity_dict['ingredient_name']
        products_dict[name] = quantity_dict
  return products_dict

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

