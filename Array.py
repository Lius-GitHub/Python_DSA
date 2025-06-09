# Time Complexity: O(logn)
# Space Complexity: O(1)
704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            # Calculate the middle index using integer division
            middle = left + ((right -left) // 2)
            if nums[middle] == target: 
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else :
                left = middle + 1
        return -1      
# 整数除用 // 
# 注意缩进 indention


# Time Complexity: O(n)
# Space Complexity: O(1)
27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)): # Pythonic for-loop iteration by index
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow



# Time Complexity: O(n)
# Space Complexity: O(n)
977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) -1
        # Initialize the result array with zeros.
        # Python's equivalent of `new Array(length).fill(0)`
        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if(left_square >= right_square):
                res[i] = left_square
                left += 1
            if(left_square < right_square):
                res[i] = right_square
                right -= 1
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Python's way to represent infinity
        min_length = float("inf")
        left = 0
        current_sum = 0
        # showing where the shortest valid subarray *began*
        start_index_of_min_subarray = 0 

        # The 'right' pointer expands the window
        for right in range(len(nums)):
            current_sum += nums[right]
            # the while loop shrinks the window from the left
            # as long as the current sum meets the target
            while current_sum >= target:
                current_window_size = right - left + 1
                # if we found a shorter valid subarray, update min-length
                if current_window_size < min_length:
                    min_length = current_window_size
                    start_index_of_min_subarray = left
                
                # shrink the window by moving the left pointer
                current_sum -= nums[left]
                left += 1

        # If min_length is still infinity, no such subarray was found.
        # Otherwise, return the min_length found.
        return 0 if min_length == float("inf") else min_length

# Time Complexity: O(n**2)
# Space Complexity: O(n**2)
59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        nums = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        while left <= right and top <= bottom:
            # 1 Traverse from left to right along the "top" raw
            for i in range(left, right+1):
                output[top][i] = nums
                nums += 1
            top += 1
            if top > bottom:
                break
            
            # 2 Traverse from the top to bottom along the "right" column
            for i in range(top, bottom + 1):
                output[i][right] = nums
                nums += 1
            right -= 1
            if right < left:
                break

            # 3 Traverse form right to left along the "bottom" raw
            for i in range(right, left -1, -1):
                output[bottom][i] = nums
                nums += 1
            bottom -= 1
            if bottom < top:
                break

            # 4 Traverse from bottom to top along the "left" column
            for i in range(bottom, top -1, -1):
                output[i] [left] = nums
                nums += 1
            left += 1
            if left > right:
                break
        return output

# Python's 2D list indexing is output[row_index][column_index].
# Think of it as output[vertical_position][horizontal_position].


# Time Complexity: O(n)
# Space Complexity: O(1)
167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum = 0
        left = 0
        right = len(numbers) -1

        while left < right :
            sum = numbers[left] + numbers[right]
            if sum == target:
                return[left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
541. Reverse String II          
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_len = len(s)
        res_list = list(s)
        # Iterate through the string in chunks of 2k characters
        for i in range(0, s_len, 2*k):
            # 'left' pointer for the current chunk's reversal start
            left = i
            # 'right' does not go beyond the string's actual end (s_len - 1)
            right = min(i+k-1, s_len-1)
            while left < right:
                # reversing
                res_list[left], res_list[right] = res_list[right], res_list[left]
                left += 1
                right -= 1
        # Join the list of characters into a single string
        return "".join(res_list)
