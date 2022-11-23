chicken_menu, fish_menu, vegetarian_menu = int(input()), int(input()), int(input())

chicken_menu *= 10.35
fish_menu *= 12.4
vegetarian_menu *= 8.15
desert = (chicken_menu + fish_menu + vegetarian_menu) * 0.2
delivery_cost = chicken_menu + fish_menu + vegetarian_menu + desert + 2.5

print(f"{delivery_cost:.2f}")
