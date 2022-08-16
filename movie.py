movies = ('Beast', 'Minions: The Rise of Gru', 'Thor: Love and Thunder')

select_movie = input('Select movie: ')

ticket_price_adult = 10.20
total_adult_ticket = int(input("Number of adult tickets: "))

ticket_price_child = 7.52
total_child_ticket = int(input('Number of child tickets: '))

local_tax = 1.072

popcorn = int(input("How many popcorn buckets? "))
popcorn_total = 7.90*popcorn

candy = int(input("How many candy boxes? "))
candy_total = 5.00*candy

drink = int(input("How many drinks? "))
drink_total = 6.25*drink

food_total = popcorn_total + candy_total + drink_total

total = str(round((ticket_price_adult*total_adult_ticket)*(local_tax) + (ticket_price_child*total_child_ticket)*(local_tax) + food_total, 2))
print("$" + total)