#Write your function here
def middle_element(lst):
  longi = len(lst)
  odd_index = int(longi/2 - 1/2)
  even_answer = (lst[int(longi/2 - 1)] + lst[int(longi/2)]) / 2
  if longi % 2 != 0:
    return lst[odd_index]
  if longi % 2 == 0:
    return even_answer
  


#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))