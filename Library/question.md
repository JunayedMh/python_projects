Build a simple library management system.
Rules:
- Pre-load 5 books. Each book: title, author, year, available (True/False).
- Menu:
1. View all books (show availability)
2. Borrow a book (by title)
3. Return a book (by title)
4. Search by author
5. Exit
- Borrowing: if available, mark it unavailable. If not, say checked out.
- Returning: if unavailable, mark it available. If already in, show error.
- Search by author is case-insensitive, shows all matching books.
- Show available vs total count when viewing all.
