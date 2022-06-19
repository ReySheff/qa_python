from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_twice_add_one(self): # проверка, что нельзя добавить одну и ту же книгу 2 раза
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_add_with_rating_1(self): # проверка, что книга по умолчанию получает рейтинг 1
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_set_book_rating_add_new_rating(self):  # проверка, что книга получила заданный рейтинг 5 (-1: 11: 0 : "")
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби',5)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_set_book_rating_add_rating_not_in_list_book(self):  # Нельзя выставить рейтинг книге, которой нет в списке.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение',5)
        assert collector.get_book_rating('Гордость и предубеждение') == None

    def test_set_book_rating_add_rating_less_one(self):  # Нельзя выставить рейтинг меньше 1
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби',0)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 0

    def test_set_book_rating_add_rating_more_ten(self):  # Нельзя выставить рейтинг больше 10
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') != 11

    def test_get_book_rating_check_none_rating_not_added_book(self):  # У не добавленной книги нет рейтинга.
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    def test_add_book_in_favorites_book_added(self): # Добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books()[-1] == 'Гордость и предубеждение и зомби'


    def test_add_book_in_favorites_book_not_in_books_rating(self):  # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self): # Проверка удаления книги из избранного.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        bookslist = collector.get_books_rating()
        assert len(bookslist) == 2 and 'Гордость и предубеждение и зомби' in bookslist and 'Что делать, если ваш кот хочет вас убить' in bookslist

    def get_books_with_specific_rating(self): # выводим список книг с определенным рейтингом
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        assert collector.get_books_with_specific_rating(5) == 'Гордость и предубеждение и зомби'

    def get_books_with_specific_rating_not_in_list(self): # Если нет книги с таким рейтингом для пуш
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 9)
        assert collector.get_books_with_specific_rating(4) == []
