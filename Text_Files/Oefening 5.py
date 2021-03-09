with open('./files/books.txt') as file:
    book = file.readline()
    counter = 1
    while book:
        author = file.readline()
        print('{}. {} -> {}'.format(counter, book.rstrip(), author.rstrip()))
        book = file.readline()
        counter += 1
