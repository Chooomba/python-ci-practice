import unittest
from books import add_book, get_all_books, search_by_author


class BookCatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = [
            {"title": "Преступление и наказание", "author": "Фёдор Достоевский"},
            {"title": "Идиот", "author": "Фёдор Достоевский"},
            {"title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
            {"title": "1984", "author": "Джордж Оруэлл"},
        ]

    def test_add_book_increases_catalog(self):
        add_book(self.catalog, "Обломов", "Иван Гончаров")
        self.assertEqual(len(self.catalog), 5)

    def test_added_book_has_title_and_author(self):
        book = add_book(self.catalog, "Обломов", "Иван Гончаров")
        self.assertEqual(book, {"title": "Обломов", "author": "Иван Гончаров"})

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_book(self.catalog, " ", "Иван Гончаров")

    def test_blank_author_is_rejected(self):
        with self.assertRaises(ValueError):
            add_book(self.catalog, "Обломов", " ")

    def test_search_returns_matching_author_books(self):
        self.assertEqual(len(search_by_author(self.catalog, "Фёдор Достоевский")), 2)

    def test_author_search_ignores_case(self):
        self.assertEqual(len(search_by_author(self.catalog, "фЁДОР ДОСТОЕВСКИЙ")), 2)

    def test_search_returns_empty_for_unknown_author(self):
        self.assertEqual(search_by_author(self.catalog, "Неизвестный автор"), [])

    def test_search_ignores_outer_spaces(self):
        self.assertEqual(len(search_by_author(self.catalog, "  Михаил Булгаков  ")), 1)

    def test_get_all_books_returns_all_entries(self):
        self.assertEqual(len(get_all_books(self.catalog)), 4)

    def test_get_all_books_returns_separate_list(self):
        result = get_all_books(self.catalog)
        result.append({"title": "Новая", "author": "Автор"})
        self.assertEqual(len(self.catalog), 4)


if __name__ == "__main__":
    unittest.main()
