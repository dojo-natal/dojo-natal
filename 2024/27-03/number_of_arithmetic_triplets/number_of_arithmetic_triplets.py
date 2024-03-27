def is_triplet(ni, nj, nk, diff):
    if (
        (nj - ni == diff) and
        (nk - nj == diff)
    ):
        return True
    return False


def number_of_arithmetic_triplets(nums, diff):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if (is_triplet(nums[i], nums[j], nums[k], diff)):
                    count += 1

    return count
                    
