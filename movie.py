print("Welcome to the movies!")
choice = 'y'

# Creates blank dictionary for movie totals
movie_total = {}

# Initializes order total
total_order = 0

# While loop starts
while choice == 'y':
    movies = ['1 - Beast', '2 - Minions: The Rise of Gru', '3 - Thor: Love and Thunder']
    print(movies)

    # Prints the selected movie
    select_movie = int(input('Select a movie: '))
    while select_movie > len(movies) or select_movie <= 0:
        print('That is not a valid movie choice. Please choose again.')
        select_movie = int(input('Select a movie: '))
    
    if select_movie == 1:
        movie = movies[select_movie - 1]
        movie_choice = movie[4:]
    elif select_movie == 2:
        movie = movies[select_movie - 1]
        movie_choice = movie[4:]
    elif select_movie == 3:
        movie = movies[select_movie - 1]
        movie_choice = movie[4:]
    # Ticket prices, tax, and food prices
    adult_ticket_price = 10.20
    child_ticket_price = 7.52
    local_tax = 1.072
    popcorn_price = 7.90
    candy_price = 5.00
    drink_price = 6.25

    adult_ticket = int(input("Number of adult tickets: "))
    adult_total = adult_ticket*adult_ticket_price

    child_ticket = int(input('Number of child tickets: '))
    child_total = child_ticket*child_ticket_price

    popcorn = int(input("How many popcorn buckets? "))
    popcorn_total = popcorn_price*popcorn

    candy = int(input("How many candy boxes? "))
    candy_total = candy_price*candy

    drink = int(input("How many drinks? "))
    drink_total = drink_price*drink

    food_total = popcorn_total + candy_total + drink_total
    
    # Prints total of each order
    total = round((adult_ticket_price*adult_ticket)*(local_tax) + (child_ticket_price*child_ticket)*(local_tax) + food_total, 2)
    print('Movie choice: ' + str(movie_choice))
    if adult_ticket != 0:
        print("Price of adult tickets: $" + str(adult_total))
    if child_ticket != 0:
        print("Price of children tickets: $" + str(child_total))
    if popcorn != 0:
        print("Price of popcorn buckets: $" + str(popcorn_total))
    if candy != 0:
        print("Price of candy boxes: $" + str(candy_total))
    if drink != 0:
        print("Price of drinks: $" + str(drink_total))
    print("Total: $" + str(total))
    total_order = round(total + total_order, 2)
    movie_total[movie_choice] = "$" + str(total)
    # While loop either ends or continues
    choice = input("Do you want to purchase more tickets? (y or n) ")

print("Totals for each movie: " + str(movie_total))
print("Total for all movies: $" + str(total_order))
print("Enjoy your movie! Goodbye!")