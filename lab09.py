# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline:
    # 1. Restate: Find indices [i, j] with i < j of two numbers in `nums` that sum to `target`.
    # 2. Example: nums = [2, 7, 11, 15], target = 9
    #    - Index 0, val 2: complement is 9 - 2 = 7. Not in map, store {2: 0}.
    #    - Index 1, val 7: complement is 9 - 7 = 2. Found in map at index 0. Return [0, 1].
    # 3. Approach:
    #    - Maintain a dictionary mapping number -> index.
    #    - For each index j and value num in nums:
    #      - Check if complement (target - num) is in dictionary.
    #      - If found, return [seen[complement], j].
    #      - Otherwise, record seen[num] = j.
    seen = {}
    for j, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], j]
        seen[num] = j
    return []


def max_profit(prices):
    # Outline:
    # 1. Restate: Find maximum difference prices[j] - prices[i] where j > i. Return 0 if no profit.
    # 2. Example: prices = [7, 1, 5, 3, 6, 4]
    #    - Day 0 (7): min_price = 7, profit = 0
    #    - Day 1 (1): min_price = 1, profit = 0
    #    - Day 2 (5): profit = max(0, 5 - 1) = 4
    #    - Day 3 (3): profit = max(4, 3 - 1) = 4
    #    - Day 4 (6): profit = max(4, 6 - 1) = 5
    #    - Day 5 (4): profit = max(5, 4 - 1) = 5 -> return 5
    # 3. Approach:
    #    - Handle empty prices by returning 0.
    #    - Track minimum price seen so far (min_price) and maximum profit so far (max_prof = 0).
    #    - Iterate over each price, updating max_prof and min_price.
    if not prices:
        return 0

    min_price = prices[0]
    max_prof = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_prof:
                max_prof = profit
    return max_prof


def max_subarray(nums):
    # Outline:
    # 1. Restate: Find the contiguous slice of `nums` that has the maximum sum.
    # 2. Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #    - Using Kadane's algorithm: at each element, decide whether to continue the current
    #      subarray sum or start a new subarray at the current element.
    # 3. Approach:
    #    - Initialize current_sum = nums[0] and max_sum = nums[0].
    #    - For each num in nums[1:]:
    #      - current_sum = max(num, current_sum + num)
    #      - max_sum = max(max_sum, current_sum)
    #    - Return max_sum.
    if not nums:
        return 0

    current_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # 1. Restate: Determine if all parentheses, brackets, and braces in `s` match and close in order.
    # 2. Example: "{[]}"
    #    - '{' -> stack = ['{']
    #    - '[' -> stack = ['{', '[']
    #    - ']' -> matches top '[' -> pop -> stack = ['{']
    #    - '}' -> matches top '{' -> pop -> stack = []
    #    - Result is True because stack is empty at end.
    # 3. Approach:
    #    - Use a list as a stack.
    #    - Map each closing bracket to its corresponding opening bracket.
    #    - Iterate through characters in string:
    #      - If opening bracket, push to stack.
    #      - If closing bracket, check if top of stack matches; if not or stack empty, return False.
    #      - Pop matching opening bracket from stack.
    #    - Return True if stack is empty, False otherwise.
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening = set(bracket_map.values())
    stack = []

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print("two_sum:", two_sum([2, 7, 11, 15], 9))
    print("max_profit:", max_profit([7, 1, 5, 3, 6, 4]))
    print("max_subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("is_balanced:", is_balanced("{[]}"))


if __name__ == "__main__":
    main()
