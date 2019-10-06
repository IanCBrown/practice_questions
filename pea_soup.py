






num_restaurants = int(input())

answer = "Anywhere is fine I guess"
for i in range(num_restaurants):
    num_menu_items = int(input())

    restuarant = input()
    menu = []
    for i in range(num_menu_items):
        menu.append(input())

    if "pancakes" in menu and "pea soup" in menu:
        answer = restuarant
        break

print(answer)

