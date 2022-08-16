print("Welcome to the movies!")
choice = 'y'

# Initializes order total
total_order = 0

# While loop starts
while choice == 'y':
    first_movie = '1 - Beast'
    second_movie = '2 - Minions: The Rise of Gru'
    third_movie = '3 - Thor: Love and Thunder'
    movies = first_movie + ', ' + second_movie + ", " + third_movie
    movies = movies.split(', ')
    print(movies)

    # Prints the selected movie
    select_movie = int(input('Select movie: '))
    if select_movie == 1:
        print(first_movie)
    elif select_movie == 2:
        print(second_movie)
    elif select_movie == 3:
        print(third_movie)

    # Ticket prices, tax, and food prices
    adult_ticket_price = 10.20
    child_ticket_price = 7.52
    local_tax = 1.072
    popcorn_price = 7.90
    candy_price = 5.00
    drink_price = 6.25

    adult_ticket = int(input("Number of adult tickets: "))
    child_ticket = int(input('Number of child tickets: '))

    popcorn = int(input("How many popcorn buckets? "))
    popcorn_total = popcorn_price*popcorn

    candy = int(input("How many candy boxes? "))
    candy_total = candy_price*candy

    drink = int(input("How many drinks? "))
    drink_total = drink_price*drink

    food_total = popcorn_total + candy_total + drink_total
    
    # Prints total of each order
    total = round((adult_ticket_price*adult_ticket)*(local_tax) + (child_ticket_price*child_ticket)*(local_tax) + food_total, 2)
    print("$" + str(total))
    total_order = total + total_order
    # While loop either ends or continues
    choice = input("Do you want to purchase more tickets? (y or n) ")

print("Total for all movies: $" + str(total_order))
print("Enjoy your movie! Goodbye!")