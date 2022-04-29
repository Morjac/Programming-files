biggest_so_far = -1
new_livro2 = ""

print ("The Books in the book of mormon are:")
with open("books_and_chapters.txt") as books:
    for book in books:
        #strip and split books.file
        book = book.strip()
        book = book.split(":")

        #seperate each list from the file
        scripture = book[0]
        chapters = int(book[1])
        livro = book[2]
        
        #
        if chapters > biggest_so_far:
            biggest_so_far = chapters
            biggest_livro = livro
            biggest_scripture = scripture
        
        
        if livro == "Book of Mormon":
            
            print (scripture)
            
            if chapters > biggest_so_far:
                biggest_so_far = chapters
                new_livro2 = biggest_livro
                biggest_scripture = scripture
            

print(f"The Book that have more scriptures is: {biggest_scripture} and it has {biggest_so_far} chapters!")
print(f"The Book in the Book of Mormon that has the most chapters is {new_livro2}")