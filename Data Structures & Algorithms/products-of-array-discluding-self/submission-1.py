class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        check_self = []

        for idx in range(len(nums)):

            if idx == 0:

                check_self.append(False)

            else:

                check_self.append(True)

        self_idx = 0
        calc_val = 1

        pos = len(nums) - 1
        restart = pos

        while (len(result) != len(nums)):
            if (pos == 0):
                if (pos != self_idx):
                    calc_val *= nums[pos]
                result.append(calc_val)
                pos = restart
                calc_val = 1
                self_idx += 1
            elif (pos == self_idx):
                pos -= 1
            else:
                calc_val *= nums[pos]
                pos -= 1

        return result