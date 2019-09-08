class Solution:
    def defangIPaddr(self, address: str) -> str:
        work = address.split(".")
        
        for string in work:
            string = ("[.]")
        print(work)
                
        return "".join(work)