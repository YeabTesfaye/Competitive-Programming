class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # output = []
        # for i in range(len(words) - 1, -1 , -1):
        #     output.append(words[i])

        #     result = ' '.join(output)

        # return result 
        
        #the shortest form of the above code 
        return ' '.join(s.split()[::-1])

        

        