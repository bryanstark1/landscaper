wallet = 0
dayCount = 1
tools = [
    {'name': 'teeth',
     'earn': 1,
     'cost': 0
     },
]
use_tool = tools[0]

def day():
    global wallet
    wallet += use_tool['earn']
    global dayCount
    dayCount += 1
    print('Wallet = $' + str(wallet) + '\n')

def game():
    checkStudents = next((item for item in tools if item['name'] == 'students'), False)
    while wallet < 10 or checkStudents == False:
      print("Day " + str(dayCount) + " of landscaping. You're using " + use_tool['name'])
      prompt = input('Are you ready to cut grass for the day? y/n: ')
      if prompt == 'y':
        day()

game()