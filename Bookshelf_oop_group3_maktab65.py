class Media:
    def __init__(self, title, author, language):
        self.title = title
        self.author = author
        self.language = language

class Book(Media):
    items = []

    def __init__(self, title, author, language, pages):
        super().__init__(title, author, language)
        self.__pages = pages
        self.read_pages = 0

    def __repr__(self):
        return f"Title: {self.title}, author: {self.author}, page: {self.__pages}"

    @classmethod
    def add_book(cls):
        title = input('Enter book title: ')
        author = input("Enter book's Author name: ")
        language = input("Enter language: ")
        page = int(input("Enter pages number: "))
        id = Book.generate_id(title, author)
        if id in Book.items:
            print("This is availabe in bookshelf")
        else:
            Book.items.append(id)
            return cls(title, author, language, page)

    @staticmethod
    def generate_id(str1, str2):
        return f"{str1.lower()}_{str2.lower()}"

    def read(self, read_pages):

        if read_pages > 0 and read_pages < self.__pages:
            self.read_pages = read_pages

    def show_progress(self):
        return f"in book {self.title} you read {self.read_pages}/{self.__pages}"

class Audio(Media):
    items = []

    def __init__(self, title, author, language, narrator, time):
        super().__init__(title, author, language)
        self.__time = time
        self.narrator = narrator
        self.listen_time = 0

    @classmethod
    def add_book(cls):
        title = input('Enter book title: ')
        author = input("Enter book's Author name: ")
        language = input("Enter language: ")
        narrator = input("Enter narrator's name:")
        time = int(input("Enter duration : "))
        id = Audio.generate_id(title, author)
        if id in Audio.items:
            print("This is availabe in bookshelf")
        else:
            Audio.items.append(id)
            return cls(title, author, language, narrator, time)

    @staticmethod
    def generate_id(str1, str2):
        return f"{str1.lower()}_{str2.lower()}"

    def set_time(self, time):
        self.time = time

    def listen(self, listen_time):

        if listen_time > 0 and listen_time < self.__time:
            self.listen_time = listen_time

    def show_progress(self):
        return f"in book {self.title} you listen {self.listen_time}/{self.__time}"

    def __repr__(self):
        return f"Title: {self.title}, author: {self.author}, time: {self.__time}"

list_of_book = []
list_of_audio = []
book_names = []
audio_names = []

def menu(number):
    if number == '1':
        b = Book.add_book()
        list_of_book.append(b)
        book_names.append(b.title)

    elif number == '2':
        a = Audio.add_book()
        list_of_audio.append(a)
        audio_names.append(a.title)
    elif number == '3':
        print(list_of_book)
    elif number == '4':
        print(list_of_audio)
    elif number == '5':
        print("books: ", book_names)
        book_name = input("enter a book name that you want to read: ")
        page_num = int(input("enter the pages that you want to read: "))
        for i in list_of_book:
            if i.title == book_name:
                i.read(page_num)
    elif number == '6':
        print("books: ", audio_names)
        audio_name = input("enter a book name that you want to listen: ")
        listen_time = int(input("enter the time that you want to listen: "))
        for i in list_of_audio:
            if i.title == audio_name:
                i.listen(listen_time)

    elif number == '7':
        for i in list_of_book:
            print(i.show_progress())
    elif number == '8':
        for i in list_of_audio:
            print(i.show_progress())

while True:
    number = input("enter an operation:")
    if number == '9':
        break
    else:
        menu(number)