#Write your function here
def combine_sort(lst1, lst2):
  combined_list = lst1 + lst2
  combined_list.sort()
  return combined_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))