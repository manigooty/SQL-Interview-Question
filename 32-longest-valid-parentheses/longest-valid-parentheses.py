class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        longest=0
        for i,val in enumerate(s):
            if val=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    longest=max(longest,i-st[-1])
        return longest
        

        