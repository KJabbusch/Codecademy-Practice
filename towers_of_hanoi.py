from basic_stack import Stack
import sys

print("\nLet's play Towers of Hanoi!!\n")
print("Type Q at any time to quit game.")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
while True:
  num_disks = input("\nHow many disks do you want to play with?\n")
  if num_disks.isdigit():
    num_disks = int(num_disks)
    break
  else:
    if num_disks == "q":
      sys.exit()
    else:
      print("Invalid response. Try again.")


while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3:\n"))

for x in range(num_disks, 0, -1):
  left_stack.push(x)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves.\n".format(num_optimal_moves))

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )

def get_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

if num_disks >= 10:
  print("Just so you are aware, if you solved this game using the minimum moves and each move took you 1 second to complete, it would take you", get_time(num_optimal_moves), "to complete.")
while True:
  keep_going = input("Do you wish to continue? Y/N\n").lower().strip()
  if keep_going == "y":
    break
  elif keep_going == "n":
    sys.exit()
  else:
    print("Invalid response. Please type Y or N.")

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}:".format(letter, name))
    user_input = input("").upper().strip()
    if user_input == "Q":
      print("Thanks for playing. Goodbye!")
      sys.exit()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]  
#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current stacks...\n")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move FROM?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move TO?")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid move. Try again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("Invalid move. Try again.")
print("\n\n You completed the game in {0} moves, and the optimal number of moves is {1}.".format(num_user_moves, num_optimal_moves))
