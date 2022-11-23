# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
# 212
# 20
# 2


current_book_pages = int(input())
pages_red_per_hour = int(input())
days_needed_for_reading = int(input())

total_hours_needed = (current_book_pages // pages_red_per_hour) / days_needed_for_reading

print(int(total_hours_needed))
