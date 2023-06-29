wallet = 5
dayCount = 1
checkStudents = False
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
    },
    {'name': 'Push Mower',
     'earn': 50,
     'cost': 25
    },
    {'name': 'Fancy Mower',
     'earn': 100,
     'cost': 250
    },
    {'name': 'Students',
     'earn': 250,
     'cost': 500
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
    global wallet
    print('\n****************************\nTools Available for Purchase\n****************************\n')
    while len(store) > 0 and store[0]['cost'] <= wallet:
      listNum = 1
      for tool in store:
          if tool['cost'] <= wallet:
              print(str(listNum) + ') ' + tool['name'] + '\n-Cost $' + str(tool['cost']) + '\n-Earn $' + str(tool['earn']) + '\n')
              listNum += 1
      prompt = input('Which number tool would you like to purchase? \nOr press "x" to exit the store: ')
      if prompt == 'x':
          break
      if int(prompt) <= len(store):
          prompt = int(prompt) - 1
          cost = store[prompt]['cost']
          if wallet >= cost:
              wallet -= store[prompt]['cost']
              print('\nYou purchased ' + store[prompt]['name'] + '\n')
              tools.append(store[prompt])
              del store[prompt]
          else:
              print("You don't have enough money to but that tool!")


def chooseTool():
    print('\n***************\nTools Available\n***************\n')
    listNum = 1
    for tool in tools:
        print(str(listNum) + ') ' + tool['name'] + '\n-Earn $' + str(tool['earn']) + '\n')
        listNum = int(listNum) + 1
    prompt = input('Which number tool do you want to use? ')
    while int(prompt) > len(tools):
        print('That is not an option, please choose again.')
        prompt = input('Which number tool do you want to use? ')
    if int(prompt) <= len(tools):
        prompt = int(prompt) - 1
        global use_tool
        use_tool = tools[prompt]
    else:
        print('That is not an option, please choose again.')


def game():
    print('\n*************************************************************\n*****************  Welcome to Landscaper!  ******************\n*  Your starting tool is teeth, which earns you $1 per day  *\n*************************************************************\n')
    # https://stackoverflow.com/questions/8653516/search-a-list-of-dictionaries-in-python
    while wallet < 1000 or checkStudents == False:
        # If store has tools and wallet has enough money, prompt user to shop
        if len(store) > 0 and wallet >= store[0]['cost']:
            prompt = input('Do you want to shop for tools? y/n ')
            # Call shop function if user wants to shop
            prompt.lower()
            if prompt == 'y':
              shop()
        if len(tools) > 0:
            prompt = input('\nDo you want to change tools? y/n ')
            if prompt == 'y':
              chooseTool()
        print("\nDay " + str(dayCount) + " of landscaping. You're using " + use_tool['name'])
        checkStudents = next((item for item in tools if item['name'] == 'Students'), False)
        prompt = input('\nAre you ready to cut grass for the day? y/n: ')
        if prompt == 'y':
            day()
    print('******************* CONGRATULATIONS! *********************\n* You acquired the Student landscapers and earned $1000! *\n*********************** YOU WIN! *************************\n')


game()
# shop()