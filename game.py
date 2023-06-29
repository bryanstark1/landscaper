wallet = 0
day = 1
tools = [
    {'name': 'teeth',
     'earn': 1,
     'cost': 0
     }
]
use_tool = tools[0]

def game():
      print("Day " + str(day) + " of landscaping. You're using " + use_tool['name'])
      global wallet
      wallet += use_tool['earn']
      print(wallet)

game()