from typing import (
    List,
)

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages:
            return 0
        start, end = max(pages), sum(pages)
        def check_complete(t, k):
            page = 0
            ans = 1
            for i in range(len(pages)):
                if page + pages[i] > t:
                    ans += 1
                    page = pages[i]
                else:
                    page += pages[i]
            if ans > k:
                return False
            return True
        
        while start < end:
            mid = start + (end - start) // 2
            if check_complete(mid, k):
                end = mid
            else:
                start = mid + 1
        return start
    
