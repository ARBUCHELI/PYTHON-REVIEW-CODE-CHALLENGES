#Write your function here
def max_num(nums):
  maximus = nums[0]
  for num in nums:
    if num > maximus:
      maximus = num
  return maximus


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))