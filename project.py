import store
from person import person
from product import product

def main():
    service = input("""
    1. Person
    2. Product
    3. Store
            >>>""")


    if service == "1":
        return person()

    elif service == "2":
        return product()

    elif service == '3':
        return store.store()

    else:
        print("Error")
        return main()


if __name__ == "__main__":
    main()