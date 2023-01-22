class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        answer_temp = []

        for num in arr:
            if num == 0:
                answer_temp.append(num)
            answer_temp.append(num)

        answer_temp = answer_temp[:len(arr)]

        for i in range(len(arr)):
            arr[i] = answer_temp[i]