#Write your function here
def remove_middle(lst, start, end):
  result = []
  forbidden_indexes = list(range(start, end + 1, 1))
  for index in forbidden_indexes:
    result.append(lst[index])
  for number in result:
    lst.remove(number)
  return lst
  

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))