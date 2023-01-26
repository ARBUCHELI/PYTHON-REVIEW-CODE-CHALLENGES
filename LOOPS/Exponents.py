#Write your function here
def exponents(bases, powers):
  answer = []
  for base in bases:
    for power in powers:
      answer.append(base ** power)
  return answer



#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))