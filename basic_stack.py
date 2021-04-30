from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the stack!".format(value))
    else:
      print("No room in stack for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      top_item_value = item_to_remove.get_value()
      self.size -= 1
      print("{} has been popped from the stack.".format(top_item_value))
      return item_to_remove.get_value()
    print("Nothing remains in the stack.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing currently in the stack.")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0

# Testing the stack class
bts_members = Stack()
members = ["Yoongi", "Taehyung", "Namjoon", "Jungkook", "Hoseok", "Jin", "Jimin", "Bang PD"]

for member in members:
    bts_members.push(member)

bts_members.pop()