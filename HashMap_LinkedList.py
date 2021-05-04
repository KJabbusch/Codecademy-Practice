from linked_list_CA import Node, LinkedList
from sample_cities_countries import cities

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for x in range(size)]

  def hash(self, key):
    hash_num = []
    for i, v in enumerate(key):
      hash_num.append(ord(v))
    return sum(hash_num)

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
        if item[0] == key:
            item[1] == value
            return
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None

city_map = HashMap(len(cities))
for city in cities:
  city_map.assign(city, cities[city])

city = city_map.retrieve('ZA')
print(city)