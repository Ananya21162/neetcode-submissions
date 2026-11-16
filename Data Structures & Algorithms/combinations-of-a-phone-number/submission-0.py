class Solution:
    def generate(self,digits,res,sub,i,dict_map):
        if i == len(digits):
            if len(sub)>0:
                res.append("".join(sub[:]))
            return
        
        for j in range(len(dict_map[digits[i]])):
            sub.append(dict_map[digits[i]][j])
            self.generate(digits,res,sub,i+1,dict_map)
            sub.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        dict_map = {'2':"abc",'3':'def','4':'ghi','5':'jkl','6':'mno'
        ,'7':'pqrs','8':'tuv','9':'wxyz'
        }
        res = []
        self.generate(digits,res,[],0,dict_map)
        return res