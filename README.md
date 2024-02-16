# qa_python

* Класс BooksCollector содержит
    * Словарь books_genre, куда можно добавить пару Название книги: Жанр книги.
    * Список favorites, который содержит избранные книги. 
    * Список genre, который содержит доступные жанры. 
    * Список genre_age_rating, который содержит жанры с возрастным рейтингом.
---
* Набор методов для работы со словарем books_genre и списком favorites:
  * add_new_book — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
    * test_add_new_book_add_two_books
  * set_book_genre — устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre. 
    * test_set_book_genre
    * test_set_book_genre_set_incorrect_genres
  * get_book_genre — выводит жанр книги по её имени. 
    * test_get_book_genre_genre_exists
    * test_get_book_genre_no_genre
  * get_books_with_specific_genre — выводит список книг с определённым жанром. 
    * test_get_books_with_specific_genre_get_list
    * test_get_books_with_specific_genre_empty_list
  * get_books_genre — выводит текущий словарь books_genre. 
    * test_get_books_genre_get_dict
  * get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга. 
    * test_get_books_for_children_only_horror_book_in_list
    * test_get_books_for_children_suitable_books_only
  * add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя. 
    * test_add_book_in_favorites_book_from_books_genre_list
    * test_add_book_in_favorites_book_not_from_books_genre_list
    * test_add_book_in_favorites_add_book_twice
  * delete_book_from_favorites — удаляет книгу из избранного, если она там есть. 
    * test_delete_book_from_favorites_if_book_exists
    * test_delete_book_from_favorites_if_favorites_empty
  * get_list_of_favorites_books — получает список избранных книг.
    * test_get_list_of_favorites_books_two_favorites_in_list