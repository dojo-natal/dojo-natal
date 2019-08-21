from functools import lru_cache


def common_child(str_a, str_b):

	@lru_cache(maxsize=64)
	def solve(idx1, idx2, ans):
		if idx1 == len(str_a) or idx2 == len(str_b):
			return ans
		if str_a[idx1] == str_b[idx2]:
			ans = max(ans, solve(idx1+1, idx2+1, ans+1))
		else:
			ans = max(
				ans,
				solve(idx1+1, idx2+1, ans),
				solve(idx1+1, idx2, ans),
				solve(idx1, idx2+1, ans) 
			)
		return ans
	
	ans = solve(0, 0, 0)
	return ans