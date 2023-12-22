def books_in_stores(books, stores):
    book_to_stores = {}
    all_books = set()

    for store_index, store_books in enumerate(stores):
        for book in store_books:
            book_to_stores.setdefault(book, []).append(store_index)
            all_books.add(book)

    in_which_stores = {book: book_to_stores.get(book, []) for book in books}

    not_in_any_store = set(books) - all_books

    return in_which_stores, not_in_any_store, all_books

M = 3
N = 4

stores = [
    [2, 3],
    [2, 3, 4],
    [4]
]

all_books = [i for i in range(1, N + 1)]

in_which_stores, not_in_any_store, all_books_present = books_in_stores(all_books, stores)

print("Книги в каждом магазине:")
for book, stores_list in in_which_stores.items():
    print(f"Книга {book} в магазинах: {stores_list}")

print("\nКниги, не доставленные ни в один магазин:")
print(not_in_any_store)

print("\nКниги, имеющиеся хотя бы в одном магазине:")
print(all_books_present)