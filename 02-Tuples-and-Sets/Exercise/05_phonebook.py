def fill_phone_book():
    data = input()
    phone_book = {}
    while not data.isdigit():
        name, phone_number = data.split("-")
        phone_book[name] = phone_number
        data = input()
    return phone_book, int(data)


def search_contact(contact_name, phone_book):
    if phone_book.get(contact_name):
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")


phone_book, iterations_count = fill_phone_book()

for _ in range(int(iterations_count)):
    name = input()
    search_contact(name, phone_book)

