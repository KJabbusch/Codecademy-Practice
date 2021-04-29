def sparse_search(data, search_val):
  # Printing out the data set
  print("Data: " + str(data))
  # Printing out what we are looking for
  print("Search Value: " + str(search_val))
  
  # Create two variables. first being the start index and last being end index.
  first = 0
  last = len(data) - 1

  # Continuous loop until condition is met
  while first <= last:
    # Determining the middle index
    mid = (first+last)//2
    # If nothing exists at middle index, we check to the left and right
    # moving one step at a time
    if not data[mid]:
      left = mid - 1
      right = mid + 1
      # Continuously looking left and right until a value found
      while True:
        # Making sure we stop when we reach the upper and lower bounds of list
        if left < first and right > last:
          print("{0} is not in the dataset.".format(search_val))
          return
        # If we find any value on right side, establish new mid
        elif right <= last and data[right]:
          mid = right
          break
        # If we find any value on left side, establish new mid
        elif left >= first and data[left]:
          mid = left
          break
        left -= 1
        right += 1
    # Once we find data, we check if the data is what we are looking for
    if data[mid] == search_val:
      print("{0} is found at position {1}".format(search_val, mid))
      return
    # Cut off the right side of list 
    elif search_val < data[mid]:
      last = mid - 1
    # Cut off the left side of list
    elif search_val > data[mid]:
      first = mid + 1
  print("{0} is not in the dataset".format(search_val))






  