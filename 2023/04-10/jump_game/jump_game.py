import typing as t

def walk(nums):
	for index, el in enumerate(nums):
		if index + 1 == len(nums): # chegou no final
			return True

		if el == 0 and not index + 1 == len(nums): # chegou no 0 e nao esta no ultimo
			return False

		return False

def jump_game(nums):
	first_num = nums[0]
	last_num = nums[-1]

	if len(nums) == 1 and first_num == 0:
		return True

	if first_num == 0:
		return False

	if not 0 in nums:
		return True

	return walk(nums)