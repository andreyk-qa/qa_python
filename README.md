1) test_add_new_book_add_one_books - проверка на добавление книги. Добавлена фикстура collector.
2) test_add_new_book_add_name_book_42_symbols - проверка на добавление книги с названием в 42 символа. Добавлена фикстура collector.
3) test_add_new_book_add_two_identical_books - проверка на повторное добавление одной книги. Добавлена фикстура collector.
4) test_set_book_genre_add_book_different_genres - проверка на добавление жанра к добавленной ранее книге. Применяется параметризация, где поочередно проверяется добавление всех жанров. Добавлена фикстура collector.
5) test_set_book_genre_add_book_nonexistent_genre_self_development - проверка на добавление несуществующего жанра к добавленной ранее книге. Добавлена фикстура collector.
6) test_get_book_genre_get_book_genre_by_name - проверка на вывод жанра книги по её названию Добавлена фикстура collector.
7) test_get_books_with_specific_genre_get_list_books_by_genre_fantasy - проверка на вывод книг по заданному жанру. Добавлена фикстура collector.
8) test_get_books_genre_get_list_all_added_books - проверка на вывод словаря с книгами. Добавлена фикстура collector.
9) test_get_books_for_children_get_books_without_rating - проверка на вывод книг для детей. Применяется параметризация, где поочередно проверяются книги с жанрами без возрастного рейтинга. Добавлена фикстура collector.
10) test_add_book_in_favorites_add_one_book - проверка на добавление книги в избранное. Добавлена фикстура collector.
11) test_add_book_in_favorites_add_two_identical_books - проверка на добавление в избранное одной книги дважды. Добавлена фикстура collector.
12) test_delete_book_from_favorites_delete_one_book - проверка на удаление книги из избранного. Добавлена фикстура collector.
13) test_get_list_of_favorites_books_get_list_with_one_favorites_book - проверка на вывод списка с избранными книгами. Добавлена фикстура collector.