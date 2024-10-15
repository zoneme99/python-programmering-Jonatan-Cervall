nums = {'a' : 2, 'b' : 2, 'c' : 3, 'd' : 1}

print(min(nums, key = nums.get))
print(min(nums, key = nums.values))

#print(nums.get('a'))

#print(min(nums))