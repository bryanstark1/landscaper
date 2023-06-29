wallet = 5
dayCount = 1
tools = [
    {'name': 'Teeth',
     'earn': 1,
     'cost': 0
    }
]
store = [
    {'name': 'Rusty Scissors',
     'earn': 5,
     'cost': 5
    }
]
use_tool = tools[0]


def day():
    global wallet
    wallet += use_tool['earn']
    global dayCount
    dayCount += 1
    print('Wallet = $' + str(wallet) + '\n')


def shop():
    print('\n***************\nTools Available\n***************\n')
    while len(store) > 0 and store[0]['cost'] <= wallet:
      for tool in store:
          if tool['cost'] <= wallet:
              listNum = 1
              print(str(listNum) + ') ' + tool['name'] + '\n-Cost $' + str(tool['cost']) + '\n-Earn $' + str(tool['earn']) + '\n')
              listNum += 1
      prompt = input('Which number tool would you like to purchase? \nOr press "C" to cancel: ')
      if prompt == 'c' or prompt == 'C':
          break
      prompt = int(prompt) - 1
      cost = store[prompt]['cost']
      if wallet >= cost:
          print('You purchased ' + store[prompt]['name'])
          tools.append(store[prompt])
          del store[prompt]
          print(store)
      else:
          print("You don't have enough money to but that tool!")


def game():
    # https://stackoverflow.com/questions/8653516/search-a-list-of-dictionaries-in-python
    checkStudents = next((item for item in tools if item['name'] == 'Students'), False)
    while wallet < 20 or checkStudents == False:
        # If store has tools and wallet has enough money, prompt user to shop
        if len(store) > 0 and wallet >= store[0]['cost']:
            prompt = input('Do you want to shop for tools? y/n ')
            # Call shop function if user wants to shop
            if prompt == 'y' or prompt == 'Y':
              shop()
        print("Day " + str(dayCount) + " of landscaping. You're using " + use_tool['name'])
        prompt = input('Are you ready to cut grass for the day? y/n: ')
        if prompt == 'y':
            day()


game()
# shop()