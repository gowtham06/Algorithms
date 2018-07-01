class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        counter = 1

        def check_condition(item, pos):

            if (item % pos == 0):
                print(True)
                return True
            elif (pos % item == 0):
                print(True)
                return True
            else:
                print(False)
                return False

        output_count = 0

        def back_track(available, used, sol_array, pos):
            # print(available,used)
            if (len(sol_array) == N):
                # print(sol_array)
                yield sol_array
            else:
                for index, item in enumerate(available):
                    print(item)
                    if (check_condition(item, pos + 1)):
                        # print(available[0:index]+available[index+1:],used+[item],sol_array+[item])
                        yield back_track(available[0:index] + available[index + 1:], used + [item],
                                   sol_array + [item], pos + 1)
                    # print(available,used)

        used = []
        available = list(range(1, N + 1))
        sol_array = []
        solutions = back_track(available, used, sol_array, 0)
        return sum(1 for _ in solutions)
if __name__ == '__main__':
    solObject=Solution()
    print solObject.countArrangement(4)
