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
