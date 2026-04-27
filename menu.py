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
    category = input("Категорія: ").strip()
    dishes.append({"name": name, "price": price, "description": description, "category": category})
    print(f"Страву '{name}' додано!")

def show_dishes(dishes):
    print("\n========== СПИСОК СТРАВ ==========")
    if not dishes:
        print("  (список порожній)")
    for i, dish in enumerate(dishes, 1):
        cat = dish.get("category", "Без категорії")
        print(f"  {i}. {dish['name']} [{cat}]")
        print(f"     Ціна: {dish['price']:.2f} грн")
        print(f"     Опис: {dish['description']}")
        print("  " + "-" * 30)
    print("===================================")

def delete_by_name(dishes):
    print("\n--- Видалити страву за назвою ---")
    name = input("Назва страви: ").strip()
    for dish in dishes:
        if dish["name"].lower() == name.lower():
            dishes.remove(dish)
            print(f"Страву '{name}' видалено!")
            print(f"Страв у меню: {len(dishes)}")
            return
    print(f"Страву '{name}' не знайдено!")

def delete_by_category(dishes):
    print("\n--- Видалити всі страви за категорією ---")
    cat = input("Категорія: ").strip()
    before = len(dishes)
    dishes[:] = [d for d in dishes if d.get("category", "").lower() != cat.lower()]
    removed = before - len(dishes)
    if removed:
        print(f"Видалено {removed} страв(и) з категорії '{cat}'.")
    else:
        print(f"Страв у категорії '{cat}' не знайдено.")
    print(f"Страв у меню: {len(dishes)}")

def edit_dish(dishes):
    print("\n--- Редагувати страву ---")
    if not dishes:
        print("Список страв порожній.")
        return
    name = input("Введіть назву страви для редагування: ").strip()
    dish = next((d for d in dishes if d["name"].lower() == name.lower()), None)
    if not dish:
        print(f"Страву '{name}' не знайдено!")
        return
    print(f"Редагуємо: {dish['name']}")
    print("Залиште порожнім, щоб не змінювати.")

    new_name = input(f"  Назва [{dish['name']}]: ").strip()
    if new_name:
        dish["name"] = new_name

    while True:
        raw = input(f"  Ціна [{dish['price']}]: ").strip()
        if not raw:
            break
        try:
            new_price = float(raw)
            if new_price < 0:
                print("Ціна не може бути від'ємною!")
            else:
                dish["price"] = new_price
                break
        except ValueError:
            print("Введіть числове значення!")

    new_desc = input(f"  Опис [{dish['description']}]: ").strip()
    if new_desc:
        dish["description"] = new_desc

    new_cat = input(f"  Категорія [{dish.get('category', 'без категорії')}]: ").strip()
    if new_cat:
        dish["category"] = new_cat
    print("Страву оновлено!")

def show_by_category(dishes):
    print("\n--- Меню по категоріях ---")
    if not dishes:
        print("  (список порожній)")
        return
    categories = {}
    for dish in dishes:
        cat = dish.get("category", "Без категорії")
        categories.setdefault(cat, []).append(dish)
    for cat, items in categories.items():
        print(f"\n  [{cat}]")
        for dish in items:
            print(f"    - {dish['name']} | {dish['price']:.2f} грн | {dish['description']}")

def total_price(dishes):
    total = sum(d["price"] for d in dishes)
    print(f"\nЗагальна ціна всіх страв: {total:.2f} грн")

def total_by_category(dishes):
    print("\nЦіна за категоріями:")
    categories = {}
    for dish in dishes:
        cat = dish.get("category", "Без категорії")
        categories[cat] = categories.get(cat, 0) + dish["price"]
    for cat, total in categories.items():
        print(f"  {cat}: {total:.2f} грн")

def sort_by_price(dishes):
    print("\n--- Сортування за ціною ---")
    print("1. За зростанням")
    print("2. За спаданням")
    choice = input("Оберіть: ").strip()
    if choice == "1":
        dishes.sort(key=lambda d: d["price"])
        print("Відсортовано за зростанням.")
    elif choice == "2":
        dishes.sort(key=lambda d: d["price"], reverse=True)
        print("Відсортовано за спаданням.")
    else:
        print("Невірний вибір.")

# --- ГОЛОВНИЙ ЦИКЛ ПРОГРАМИ ---

def main():
    dishes = [] # База даних страв
    
    while True:
        print("\n=== МЕНЮ РЕСТОРАНУ ===")
        print("1. Додати страву (А)")
        print("2. Показати все меню (А)")
        print("3. Редагувати страву (Б)")
        print("4. Показати меню за категоріями (Б)")
        print("5. Видалити за назвою (В)")
        print("6. Видалити за категорією (В)")
        print("7. Загальна ціна та за категоріями (Г)")
        print("8. Сортувати за ціною (Г)")
        print("0. Вийти")
        
        choice = input("\nОберіть дію: ").strip()
        
        if choice == "1":
            add_dish(dishes)
        elif choice == "2":
            show_dishes(dishes)
        elif choice == "3":
            edit_dish(dishes)
        elif choice == "4":
            show_by_category(dishes)
        elif choice == "5":
            delete_by_name(dishes)
        elif choice == "6":
            delete_by_category(dishes)
        elif choice == "7":
            total_price(dishes)
            total_by_category(dishes)
        elif choice == "8":
            sort_by_price(dishes)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
