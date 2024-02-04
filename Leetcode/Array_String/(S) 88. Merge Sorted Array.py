class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        c = nums1[:m]
        while (i < m) and (j < n):
            if c[i] < nums2[j]:
                nums1[i + j] = c[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
        if (i != m):
            nums1[i + j:]=c[i:]
        elif (j != n):
            nums1[i + j:] = nums2[j:]