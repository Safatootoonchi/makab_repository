class Cart_metro1:
    def __init__(self, number_of_trip):
        self.number_of_trip = number_of_trip

    def used(self):
        if self.number_of_trip > 1:
            print("Max number of your trips is one. ")
        elif self.number_of_trip == 1:
            print("heve a nice trip. ")
        else:
            print("Number of trips not passible. ")


class Cart_metro2(Cart_metro1):
    def __init__(self, number_of_trip, amount_of_credit):
        self.amount_of_credit = amount_of_credit
        self.residua_credit = None
        super().__init__(number_of_trip)

    def credit(self):

        if self.number_of_trip > self.amount_of_credit:
            print("Number of trip is not allowed. ")
        elif self.number_of_trip <= self.amount_of_credit:
            print("Number of trip is allowed. ")

    def Add(self, add_trips):
        self.add_trips = add_trips
        self.residua_credit = self.amount_of_credit - self.number_of_trip + self.add_trips
        print(f'your residua_credit is : {self.residua_credit}.')


class Cart_metro3(Cart_metro2):
    def __init__(self, number_of_trip, amount_of_credit, expirition_date):
        self.expirition_date = expirition_date.split("/")
        super().__init__(number_of_trip, amount_of_credit)

    def set_time(self, your_date):
        self.your_date = your_date.split("/")

    def compare_time(self):
        if self.your_date[0] > self.expirition_date[0]:
                return f'Your cart has expired. '
        else:
            if self.your_date[1] > self.expirition_date[1]:
                return f'Your cart has expired. '
            else:
                if self.your_date[2] > self.expirition_date[2]:
                    return f'Your cart has expired. '
                else:
                    return f'Your cart has not expired. '


    def credit(self):
        super().credit()

    def Add(self, add_trips):
        super().Add(add_trips)


def Menu():
    while True:
        print('1_Single table card\n2_Credit card\n3_Credit and timed card\n ')
        key = int(input('Enetr a number of cart: '))
        if key == 1:
            number_of_trip = int(input('Enter number_of_trip: '))
            a = Cart_metro1(number_of_trip)
            a.used()
        elif key == 2:
            number_of_trip = int(input('Enter number_of_trip: '))
            amount_of_credit = int(input('Enter amount_of_credit: '))
            b = Cart_metro2(number_of_trip, amount_of_credit)
            b.credit()
            add_trips = int(input('Enter add_trips: '))
            b.Add(add_trips)
        elif key == 3:
            number_of_trip = int(input('Enter number_of_trip: '))
            amount_of_credit = int(input('Enter amount_of_credit: '))
            expirition_date = input('Enter expirition_date: ')
            c = Cart_metro3(number_of_trip, amount_of_credit, expirition_date)
            your_date = input('Enter your_date: ')
            c.set_time(your_date)
            print(c.compare_time())
            c.credit()
            add_trips = int(input('Enter add_trips: '))
            c.Add(add_trips)
        else:
            print('You left. ')
            break


Menu()
