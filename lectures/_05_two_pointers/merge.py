"""Description:
Даны две отсортированные последовательности чисел (длиной N и M
соответственно). Необходимо слить их в одну отсортированную последовательность
"""


def merge (nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] < nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    return merged


num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
print(merge(num1, num2))
