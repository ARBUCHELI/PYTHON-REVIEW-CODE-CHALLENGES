#Write your function here
def over_nine_thousand(lst):
  elements_sum = 0
  answer = 0
  if len(lst) == 0:
    return 0
  for num in lst:
    elements_sum += num
    if elements_sum > 0 and elements_sum <= 9000:
      answer = elements_sum
    if elements_sum > 9000:
      break
  return elements_sum
      


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))