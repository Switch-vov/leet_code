from typing import List


class SolutionV1:
    results = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.backtrack('', n, n)
        return self.results

    def backtrack(self, result: str, left: int, right: int):
        if not left and not right:
            self.results.append(result)
            return
        if left > right:
            return
        if left > 0:
            self.backtrack(result + '(', left - 1, right)
        if right > 0:
            self.backtrack(result + ')', left, right - 1)


class SolutionV2:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.backtrack(results, '', n, n)
        return results

    def backtrack(self, results: List[str], result: str, left: int, right: int):
        if not left and not right:
            results.append(result)
            return
        if left > right:
            return
        if left > 0:
            self.backtrack(results, result + '(', left - 1, right)
        if right > 0:
            self.backtrack(results, result + ')', left, right - 1)
