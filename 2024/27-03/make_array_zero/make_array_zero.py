 def remove_zeros(nums):
    return [n for n in nums if n != 0]

def make_array_zero(nums):
    count = 0
    nums_sem_zeros = remove_zeros(nums)

    while remove_zeros(nums_sem_zeros):
        nums_sem_zeros = remove_zeros(nums_sem_zeros)
        small = min(nums_sem_zeros)
        count += 1
        for i, v in  enumerate(nums_sem_zeros):
            nums_sem_zeros[i] -= small
    return count