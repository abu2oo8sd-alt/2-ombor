
from collections import Counter

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    frequency = Counter(nums)

    result = sorted(
        nums,
        key=lambda x: (-frequency[x], x)
    )

    return result


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
print(rearrange_by_frequency([1, 1, 2, 2, 3]))
