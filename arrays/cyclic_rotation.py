# An array A consisting of N integers is given. Rotation of the array means that each element is
# shifted right by one index, and the last element of the array is moved to the first place.
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are
# shifted right by one index and 6 is moved to the first place).

from typing import List

def solution(a: List, k: int):
    for i in range(k):
        a = a[-1:] + a[:-1]
    return a

print(solution([1, 2, 3, 4], 4))
