data = {
    'food' : [],
    'transport' : [],
    'entertainment' : [],
}
try:
  while True:
    for i, k in enumerate(data.keys()):
      if i == 0:
        print(f'''Please select the category of your expense or enter if it doesn't exist:\n{i+1}) {k.capitalize()}''')
      else:
        print(f'{i+1}) {k.capitalize()}')
      
    category = input('Your choice: ').lower()

    if category in ['food', 'transport','entertainment', 1,2,3]:
      amount = float(input(f'Enter the amount of {category} expense: '))
      data[category].append(amount)

    else:
      if category not in data and category.str():
        data[category] = []
      amount = float(input(f'Enter the amount of {category} expense: '))
      data[category].append(amount)

    user_input = input("Type Y/N if you want or don't to continue: ").lower()

    if user_input == 'n':
      break

except ValueError:
  print('You entered incorrect value.')

for k,v in data.items():
  print(f"You spent total {int(sum(v))} for {k}.")
