import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_one_books(self, collector):
        collector.add_new_book('Дюна')
        assert 'Дюна' in collector.books_genre

    def test_add_new_book_add_name_book_42_symbols(self, collector):
        collector.add_new_book('Самурай без меча Самурай без меча Самурай.')
        assert 'Самурай без меча Самурай без меча Самурай.' not in collector.books_genre

    def test_add_new_book_add_two_identical_books(self, collector):
        collector.add_new_book('Черный лебедь')
        collector.add_new_book('Черный лебедь')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name, genre', [
        ('Дюна', 'Фантастика'),
        ('Только хорошие индейцы', 'Ужасы'),
        ('Гордость и предубеждение', 'Детективы'),
        ('Укрощение строптивой', 'Комедии'),
        ('Умка ищет друга', 'Мультфильмы')
    ])
    def test_set_book_genre_add_book_different_genres(self, book_name, genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_set_book_genre_add_book_nonexistent_genre_self_development(self, collector):
        collector.add_new_book('Эмоциональный интеллект')
        collector.set_book_genre('Эмоциональный интеллект', 'Саморазвитие')
        assert collector.books_genre['Эмоциональный интеллект'] == ''

    def test_get_book_genre_get_book_genre_by_name(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_get_list_books_by_genre_fantasy(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Метро 2033')
        collector.add_new_book('Только хорошие индейцы')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        collector.set_book_genre('Только хорошие индейцы', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Метро 2033']

    def test_get_books_genre_get_list_all_added_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Метро 2033')
        collector.add_new_book('Только хорошие индейцы')
        assert collector.get_books_genre() == {'Дюна': '', 'Метро 2033': '', 'Только хорошие индейцы': ''}

    @pytest.mark.parametrize('book_name, genre', [
        ('Дюна', 'Фантастика'),
        ('Укрощение строптивой', 'Комедии'),
        ('Умка ищет друга', 'Мультфильмы')
    ])
    def test_get_books_for_children_get_books_without_rating(self, book_name, genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.favorites

    def test_add_book_in_favorites_add_two_identical_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_get_list_with_one_favorites_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']
