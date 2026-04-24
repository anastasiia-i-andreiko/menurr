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
