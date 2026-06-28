books = [
{"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "available": True},
{"title": "Atomic Habits", "author": "James Clear", "year": 2018, "available": True},
{"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
{"title": "Animal Farm", "author": "George Orwell", "year": 1945, "available": False},
{"title": "Deep Work", "author": "Cal Newport", "year": 2016, "available": True},
]

def find_book(title):
    for book in books:
       # for debugging: print(f"Checking: {book['title']} against {title}")
        if book["title"].lower() == title.lower():
            return book
        # else: return None {The loop was returning False after the first mismatch.}
    return None
        
while True:
    print("\n\n1.View 2.Borrow 3.Return 4.Author Search 5.Exit")
    print()
    choice = input("Select option: ")

    if choice == "1":
        print("\nBook name             Author               year      Available")
        for book in books:
            print(f"{book["title"]:<20}: {book["author"]:<20} {book["year"]:<10} {book["available"]}")
    
    elif choice == "2":
        borrow = find_book(input("Search by title: "))
        if borrow:
            if borrow["available"] == True:
                print("Book is available to borrow.")
                choice = input("Do you want to borrow? Yes/No: ").capitalize()
                if choice == "Yes":
                    borrow["available"] = False
                    print(f"{borrow["title"]} borrowed successful.")
                else:
                    print("Thanks for visiting.")
            else:
                print("Book is not available to borrow")
        else:
            print("Book not found.")