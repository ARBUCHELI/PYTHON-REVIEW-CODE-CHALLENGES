#Write your function here
def double_index(lst, index):
  if index > len(lst) - 1:
    return lst 
  else:
    return lst[:index] + [lst[index] * 2] + lst[index+1:]
  
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))