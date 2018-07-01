class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.solution_set=[]
        def get_solutions(solution_set, candidates, target):
            print (solution_set, target)
            if (target == 0):
                print (solution_set)
                self.solution_set=self.solution_set+solution_set
                # return solution_set

            else:
                for item in candidates:
                    if (target - item >= 0):
                        # print target-item
                        return get_solutions(solution_set+[item], candidates, target - item)
        get_solutions([],candidates,target)
        print(self.solution_set)

if __name__ == '__main__':
    comb_object=Solution()
    candidate=[2,3,6,7]
    target=7
    comb_object.combinationSum(candidate,target)
