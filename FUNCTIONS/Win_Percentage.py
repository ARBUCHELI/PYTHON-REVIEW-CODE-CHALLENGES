# Write your win_percentage function here:
def win_percentage(wins, losses):
  total = wins + losses
  radio_of_winning = wins / total
  return int(radio_of_winning * 100)

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100