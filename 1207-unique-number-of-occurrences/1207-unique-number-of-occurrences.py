class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        # Count the occurrences of each number
        for num in arr:
            count[num] = count.get(num, 0) + 1

        # Check if all occurrence counts are unique
        return len(count.values()) == len(set(count.values()))       