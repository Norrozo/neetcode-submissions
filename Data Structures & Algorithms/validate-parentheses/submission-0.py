class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            #check if character is a bracket
            if char in bracket_map:
                #puts stuff onto the stack
                stack.append(char)

            else:
                #if its not a right close then itll return false immediately
                if not stack:
                    return False

                top_element = stack.pop()

                if bracket_map[top_element] != char:
                    return False
# if len(stack) == 0:
# return True
# else:
# return False
# another way to write this
        return not stack

