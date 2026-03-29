from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_squares = defaultdict(set)

        for idx_r, row in enumerate(board):
            for idx_c, val in enumerate(row):
                if val == '.':
                    continue
                if (val in seen_rows[idx_r]) or (val in seen_cols[idx_c]) or (val in seen_squares[(idx_r // 3, idx_c // 3)]):
                    return False
                seen_rows[idx_r].add(val)
                seen_cols[idx_c].add(val)
                seen_squares[(idx_r // 3, idx_c // 3)].add(val)
        return True