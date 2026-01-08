from library import format_book_details

def test_format_book_details():
    result = format_book_details(1001, "How good to be true", "Prajakta", 2025)

    expected = (
        "Book ID: 1001\n"
        "Book Name: How good to be true\n"
        "Author Name: Prajakta\n"
        "Year of Publication: 2025"
    )

    assert result == expected
