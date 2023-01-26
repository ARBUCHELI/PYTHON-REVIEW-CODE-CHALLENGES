#Write your function here
def every_three_nums(start):
  result = [start]
  if start > 100:
    return []
  else:
    while result[-1] != 100:
      start += 3
      result.append(start)
  return result

#Uncomment the line below when your function is done
print(every_three_nums(91))