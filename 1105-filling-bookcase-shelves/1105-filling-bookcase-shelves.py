class Solution:
    def helper(self, cur_book_index, books_len, books, shelf_width, cur_books_width, cur_shelf_max_height, memo):
        if (cur_book_index, cur_books_width) in memo:
            return memo[(cur_book_index, cur_books_width)]
        
        if cur_book_index == books_len:
            return cur_shelf_max_height
        
        # Put current book on the current shelf
        cur_book_width = books[cur_book_index][0]
        cur_book_height = books[cur_book_index][1]
        
        # Update current shelf total books width
        new_books_width = cur_books_width + cur_book_width
        
        # Final answer will be
        answer_next_shelf = float("inf")
        answer_same_shelf = float("inf")
        
        # Check if the current book can be placed on current shelf
        if new_books_width <= shelf_width:
            # Go to the next book
            answer_same_shelf = self.helper(cur_book_index + 1, books_len, books, shelf_width, new_books_width, max(cur_shelf_max_height, cur_book_height), memo)
            
        # Put current book on the next shelf
        answer_next_shelf = cur_shelf_max_height + self.helper(cur_book_index + 1, books_len, books, shelf_width, cur_book_width, cur_book_height, memo)
        
        answer = min(answer_same_shelf, answer_next_shelf)
        memo[(cur_book_index, cur_books_width)] = answer
        
        return answer
    
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        memo = defaultdict(int)
        return self.helper(0, len(books), books, shelf_width, 0, 0, memo)
        