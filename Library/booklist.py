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

# New function to find book author to use option 4.

def find_author(author):
    for book in books:
        if book["author"].lower() == author.lower():
            return book
    return None
        
while True:
    print("\n1.View 2.Borrow 3.Return 4.Author Search 5.Exit")
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

    elif choice == "3":
        ret = find_book(input("Enter the book title: "))
        if not ret:
            print("Book not available.")
        elif ret["available"] == True:
            print(f"{ret["title"]} was not borrowed")
        else:
            ret["available"] = True
            print("Thanks for returning the book.")

    elif choice == "4":
        b = find_author(input("Search by author: "))
        if b:
            print(f"{b["author"]} titles: {b["title"]:<5}, {b["year"]}")
            brw = find_book(input("Which book you want to borrow?: "))
            if not brw:
                print("Not available.")
            elif brw["available"] == True:
                print(f"{brw["title"]} is available to borrow.")
                choice1 = input("Do you want to borrow? Yes/No: ").capitalize()
                if choice1 == "Yes":
                    brw["available"] = False
                    print("Borrowed successful.")
                else:
                    print("Thanks for visisng the library.")
            else:
                print("Book is not available to borrow.")
        else:
            print("Not available.")

    elif choice == "5":
        break
    else:
        again = input("Back to the menu? Y/N: ")
        again = again.strip().lower()

        if again == "n":
                break


