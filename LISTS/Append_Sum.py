#Write your function here
def append_sum(lst):
  for temp in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))