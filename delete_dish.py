
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
