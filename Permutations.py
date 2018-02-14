class Solution(object):
    def permute(self, nums):
        res = []
        path = []
        self.recurse(nums,path,res)
        return res

    def recurse(self,nums,path,res):
        if len(nums) == 0:
            res.append(path)
        else:
            for i,n in enumerate(nums):
                #print("nums", nums[:i] + nums[i+1:])
                #print("path", path + [nums[i]])
                #print("res",res)
                self.recurse(nums[:i] + nums[i+1:], path + [nums[i]], res)
