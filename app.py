from books import add_book, get_all_books, search_by_author


def main():
    catalog = []
    add_book(catalog, "Преступление и наказание", "Фёдор Достоевский")
    add_book(catalog, "Идиот", "Фёдор Достоевский")
    print("Каталог книг")
    for book in search_by_author(catalog, "достоевский"):
        print(f'{book["title"]} — {book["author"]}')
    print(f"Всего книг: {len(get_all_books(catalog))}")


if __name__ == "__main__":
    main()
