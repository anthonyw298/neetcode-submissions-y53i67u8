class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols, rows = len(matrix) - 1, len(matrix[0]) - 1
        l, r = 0, cols
        while l < r:
            mid = (r + l) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][rows]:
                l = mid
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][rows] < target:
                l = mid + 1
        if l > r:
            return False
        nums = matrix[l]
        print(nums)
        l, r = 0 , rows
        while l <= r:
            print(l,r)
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return True
        return False
