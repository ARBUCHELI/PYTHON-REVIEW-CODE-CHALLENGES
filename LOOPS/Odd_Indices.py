#Write your function here
def odd_indices(lst):
  new_list = []
  for num in lst:
    if lst.index(num) % 2 != 0:
      new_list.append(num)
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))