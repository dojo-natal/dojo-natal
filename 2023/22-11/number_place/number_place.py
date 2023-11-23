def number_place_3x3(nums):
	def verify(row):
		return len(set(row)) == len(row)


	group = []
	for ki in range(3):
		for kj in range(3):
			group.append(nums[ki][kj])
	if not verify(group):
		return False
	return True


def number_place_9x9(nums):
	def verify(row):
		return len(set(row)) == len(row)

	for ind, row in enumerate(nums):
		if not verify(row):
			return False

		col = [num[ind] for num in nums]
		if not verify(col):
			return False

	for i in range(3):
		for j in range(3):
			sub_grid = [[0]*3 for _ in range(3)]
			
			for ki in range(3):
				for kj in range(3):
					sub_grid[ki][kj] = nums[i*3 + ki][j*3 + kj]

			if not number_place_3x3(sub_grid):
				return False

	return True