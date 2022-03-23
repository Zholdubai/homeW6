def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:


    def find_target(self, list, target):
        left_limit = 0
        right_limit = len(list)
        q=0
        while left_limit <= right_limit:
            q+=1
            middle_index = (left_limit + right_limit) // 2
            if list[middle_index] < target:
                left_limit = middle_index + 1
            elif list[middle_index] > target:
                right_limit = middle_index - 1
            else:
                return q


print(Solution().find_target(get_list(), 50000))
