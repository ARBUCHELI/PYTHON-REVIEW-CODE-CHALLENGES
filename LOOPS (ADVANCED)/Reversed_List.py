#Write your function here
def reversed_list(lst1, lst2):
  reversed_index = len(lst2) -1
  counting_matches = 0
  for i in range(len(lst1)):
    if lst1[i] == lst2[reversed_index]:
      counting_matches += 1
      reversed_index -= 1
  if counting_matches == len(lst2):
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))