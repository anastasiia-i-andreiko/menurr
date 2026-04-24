
dishes = []

def show_menu():
    print("\n=== МЕНЮ РЕСТОРАНУ ===")
    print("1. Додати страву")
    print("2. Редагувати страву")
    print("3. Видалити страву")
    print("4. Показати загальну ціну")
    print("0. Вийти")

def main():
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()
        if choice == "0":
            print("До побачення!")
            break
        else:
            print("Функціонал у розробці...")

if __name__ == "__main__":
    main()
