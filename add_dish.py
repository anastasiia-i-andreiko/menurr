def add_dish(dishes):
    print("\n--- Додати страву ---")
    name = input("Назва страви: ").strip()
    while True:
        try:
            price = float(input("Ціна (грн): "))
            if price < 0:
                print("Ціна не може бути від'ємною!")
            else:
                break
        except ValueError:
            print("Введіть числове значення!")
    description = input("Опис: ").strip()
    dishes.append({"name": name, "price": price, "description": description})
    print(f"Страву '{name}' додано!")

def show_dishes(dishes):
    print("\n========== СПИСОК СТРАВ ==========")
    if not dishes:
        print("  (список порожній)")
    for i, dish in enumerate(dishes, 1):
        print(f"  {i}. {dish['name']}")
        print(f"     Ціна: {dish['price']:.2f} грн")
        print(f"     Опис: {dish['description']}")
        print("  " + "-" * 30)
    print("===================================")
