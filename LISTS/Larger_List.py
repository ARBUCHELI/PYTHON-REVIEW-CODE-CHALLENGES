#Write your function here
def larger_list(list1, list2):
  if len(list1) >= len(list2):
    return list1[-1]
  else:
    return list2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))