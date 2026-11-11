def validate_book(title, author):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название книги не должно быть пустым")
    if not isinstance(author, str) or not author.strip():
        raise ValueError("Имя автора не должно быть пустым")
    return True


def add_book(catalog, title, author):
    validate_book(title, author)
    book = {"title": title.strip(), "author": author.strip()}
    catalog.append(book)
    return book


def search_by_author(catalog, author):
    if not isinstance(author, str) or not author.strip():
        return []
    query = author.strip().casefold()
    return [book for book in catalog if query in book["author"].casefold()]


def get_all_books(catalog):
    return list(catalog)
