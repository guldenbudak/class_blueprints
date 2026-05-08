cinema_list = []


class Cinema:
    def __init__(self, movie_name, seat_number, ticket_type, is_borrowed=False, price=None):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.ticket_type = ticket_type
        self.is_borrowed = is_borrowed
        self.price = price
        self.set_ticket_price()

    def show_movie_list(self):
        borrowed_movie = "Available"
        if self.is_borrowed == True:
            borrowed_movie = "Borrowed "
        return f"{self.movie_name} movie was taken from seat number {self.seat_number} {borrowed_movie} ticket price : ${self.price}"

    def add_cinema(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"You have a borrowed {self.movie_name}. ")
        else:
            print(f"Sorry, {self.movie_name} is already taken.")

    def cancel_ticket(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            cinema_list.remove(new_cinema_list)
            print(f" You have a returned {self.movie_name}. ")
        else:
            print(f"Sorry, {self.movie_name} was not borrowed.")

    def set_ticket_price(self):
        if self.ticket_type == "vıp" or self.ticket_type == "vip":
            self.price = 200
        elif self.ticket_type == "normal":
            self.price = 100


while True:
    print("Welcome to Cinema Ticketing System")
    print("1. Add cinema tickets")
    print("2. Cancel movie ticket")
    print("3. Viewing movie tickets")
    print("4. Exit")

    option = int(input("Enter your choice: "))
    if option == 1:
        movie_name = input("Enter the movie name: ")
        seat_number = int(input("Enter the seat number: "))
        ticket_type = input("Enter the ticket type(VIP/Normal): ").lower()
        while ticket_type != "vıp" and ticket_type != "vip" and ticket_type != "normal":
            print("Please choose either VIP or standard type !!!")
            ticket_type = input("Enter the ticket type(VIP/Normal): ").lower()

        new_cinema_list = Cinema(movie_name=movie_name, seat_number=seat_number, ticket_type=ticket_type, price=None)
        cinema_list.append(new_cinema_list)

        selected_cinema = cinema_list
        for cinema in cinema_list:
            if cinema.seat_number == seat_number:
                selected_cinema = cinema
                selected_cinema.add_cinema()

                break
        else:
            print("You entered a sequence number that is not in the list.")

    if option == 2:
        seat_number = int(input("Enter the seat number: "))
        selected_cinema = cinema_list
        for cinema in cinema_list:
            if cinema.seat_number == seat_number:
                selected_cinema = cinema
                selected_cinema.cancel_ticket()

            else:
                print("You entered a sequence number that is not in the list.")

    if option == 3:
        seat_number = int(input("Enter the seat number: "))
        selected_cinema = cinema_list
        if cinema_list == []:
            print("List empty, no operations found.")
        for cinema in cinema_list:
            if cinema.seat_number == seat_number:
                selected_cinema = cinema
                print(selected_cinema.show_movie_list())
            else:
                print("You entered a sequence number that is not in the list.")

    if option == 4:
        print("Thank you for choosing Cinema Ticketing System")
        break
