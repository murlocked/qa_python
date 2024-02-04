import pytest
from main import BooksCollector

book_titles = ['Гордость и предубеждение и зомби',
                'Что делать, если ваш кот хочет вас убить',
                'Ужасно длинное название для дальнейшего использования в тестах']

genres = ['Фантастика', 'Ужасы',
          'Детективы', 'Мультфильмы',
          'Комедии']


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_new_book(book_titles[1])

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.set_book_genre(book_titles[0], genres[0])

        assert collector.books_genre == {book_titles[0]: genres[0]}

    @pytest.mark.parametrize('genre', ['123', 'pewpew', 'mewmew'])
    def test_set_book_genre_set_incorrect_genres(self, genre):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.set_book_genre(book_titles[0], genre)

        assert collector.books_genre == {book_titles[0]: ''}

    def test_get_book_genre_genre_exists(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.set_book_genre(book_titles[0], genres[2])

        assert collector.get_book_genre(book_titles[0]) == genres[2]

    def test_get_book_genre_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.set_book_genre(book_titles[0], '')

        assert not collector.get_book_genre(book_titles[0])

    def test_get_books_with_specific_genre_get_list(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.set_book_genre(book_titles[0], genres[2])

        assert collector.get_books_with_specific_genre(genres[2]) == [book_titles[0]]

    def test_get_books_with_specific_genre_empty_list(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])

        assert not collector.get_books_with_specific_genre(genres[2])

    def test_get_books_genre_get_dict(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])

        assert collector.get_books_genre() == {book_titles[0]: ''}

    def test_get_books_for_children_only_horror_book_in_list(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[2])
        collector.set_book_genre(book_titles[2], genres[1])

        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_suitable_books_only(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_new_book(book_titles[1])
        collector.set_book_genre(book_titles[0], genres[0])
        collector.set_book_genre(book_titles[1], genres[3])

        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_book_from_books_genre_list(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_book_in_favorites(book_titles[0])

        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_book_not_from_books_genre_list(self):
        collector = BooksCollector()

        collector.add_book_in_favorites(book_titles[0])

        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_add_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_book_in_favorites(book_titles[0])
        collector.add_book_in_favorites(book_titles[0])

        assert not len(collector.favorites) == 2

    def test_delete_book_from_favorites_if_book_exists(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_book_in_favorites(book_titles[0])
        collector.delete_book_from_favorites(book_titles[0])

        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_if_favorites_empty(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])

        assert not collector.delete_book_from_favorites(book_titles[0])

    def test_get_list_of_favorites_books_two_favorites_in_list(self):
        collector = BooksCollector()

        collector.add_new_book(book_titles[0])
        collector.add_new_book(book_titles[1])
        collector.add_book_in_favorites(book_titles[0])
        collector.add_book_in_favorites(book_titles[1])

        assert len(collector.get_list_of_favorites_books()) == 2

