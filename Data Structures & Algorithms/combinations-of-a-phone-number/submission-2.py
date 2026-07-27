class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitmap={
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m", "n", "o"],
            "7":["p","q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w","x","y", "z"]
        }

        if not digits: return []

        result=[]

        def helper(i, temp):
            if i==len(digits):
                result.append("".join(temp[:]))
                return 


            for val in digitmap[digits[i]]:
                temp.append(val)
                helper(i+1, temp)
                temp.pop()

        helper(0,[])



        return result

            
                


            

        