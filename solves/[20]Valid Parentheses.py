class SolutionV1:
    def isValid(self, s: str) -> bool:
        result = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                result.append(c)
                continue
            if not result:
                return False
            r_c = result.pop()
            if c == ')' and r_c != '(':
                return False
            elif c == ']' and r_c != '[':
                return False
            elif c == '}' and r_c != '{':
                return False
        return not result
