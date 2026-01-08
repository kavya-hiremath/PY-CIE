def format_book_details(book_id, book_name, author_name, year_of_publication):
    result = (
        f"Book ID: {book_id}\n"
        f"Book Name: {book_name}\n"
        f"Author Name: {author_name}\n"
        f"Year of Publication: {year_of_publication}"
    )
    return result

if __name__ == "__main__": 
    print(format_book_details(1001, "How good to be good", "Prajakta", 2025))