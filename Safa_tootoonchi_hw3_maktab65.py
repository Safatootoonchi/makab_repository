import re


class Address:

    def __init__(self, city_name, street_name, number_plaque, number_postal_code):
        self.city = city_name
        self.street = street_name
        self.number_plaque = number_plaque
        self.number_postal_code = number_postal_code

    @classmethod
    def give_address(cls):
        city_name = input('Enter the city:')
        street_name = input('Enter the street:')
        number_plaque = input("Enter the plaque:")
        number_postal_code = input("Enter postal code:")

        print("succesfully addae!")
        return cls(city_name, street_name, number_plaque, number_postal_code)

    def change_to_dict(self):
        dict_info_Adress = vars(self)

        return dict_info_Adress

    def Edit(self):
        dict_info_Adress = Address.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Adress.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Adress.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Address.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


#
a = Address.give_address()
a.Edit()
a.change_to_dict()
a.show_info()


class Person:

    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.email = ''
        self.national_code = None
        self.phone_number = phone_number

    @classmethod
    def get_info_person(cls):
        firstname = input('Enter your first name:')
        lastname = input('Enter your last name:')
        phone_number = input("Enter the phone number:")
        # Person.dict_info_person = {" firstname": firstname, "last_name": lastname,
        #                            "phone_number": phone_number}

        return cls(firstname, lastname, phone_number)

    def email_address_validation(self):

        while True:
            try:
                email = input('enter your email: ')
                if email.endswith(".com"):
                    if email.startswith('@') == False:
                        if re.findall("@", email):
                            self.email = email
                            break

                        else:
                            raise ValueError()
                    else:

                        raise ValueError()

                else:

                    raise ValueError()



            except  ValueError:
                print("email is wrong!please try again")

    def national_code_validation(self):
        while True:
            try:
                national_code = input("Enter national code:")
                if national_code == '10':
                    self.national_code = national_code
                    break
                else:
                    raise ValueError()

            except ValueError:
                print("it is wrong try again!please try again")

    def change_to_dict(self):
        dict_info_Person = vars(self)

        return dict_info_Person

    def Edit(self):
        dict_info_Person = Person.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            # if ker == email:
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Person.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Person.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


b = Person.get_info_person()
b.email_address_validation()
b.national_code_validation()
b.Edit()
b.change_to_dict()
b.show_info()


class Store():

    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental):
        self.tenant = tenant
        self.owner = owner
        self.address = address
        self.active_inactive = active_inactive
        self.telephone = telephone
        self.area = area
        self.mortgage_amount = mortgage_amount
        self.rental_amount = rental_amount
        self.sales_rental = sales_rental
        self.sales_amount = sales_amount

    @classmethod
    def get_info(cls):
        tenant = input("Enter tenant:")
        owner = input("Enter owner:")
        mortgage_amount = input("Enter mortgage_amount: ")
        rental_amount = input("Enter Rental_amount:")
        sales_rental = input(" Enter sales_rental:")
        address = input("Enter address:")
        active_inactive = input("Enter active or inactive!")
        telephone = input("Enter telephone number:")
        sales_amount = input(" Enter sales_amount:")
        area = input("Enter area")
        return cls(tenant, owner, mortgage_amount, rental_amount, sales_rental, area,
                   sales_amount, address, active_inactive, telephone)

    def change_to_dict(self):
        dict_info_Store = vars(self)

        return dict_info_Store

    def Edit(self):
        dict_info_Store = Store.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Store.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Store.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Store.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Apartment(Store):
    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms, number_floor, floor,
                 parking):
        super().__init__(tenant, owner, address, active_inactive, telephone, area,
                         mortgage_amount, rental_amount, sales_amount, sales_rental)
        self.number_rooms = number_rooms
        self.number_floor = number_floor
        self.floor = floor
        self.parking = parking

    @classmethod
    def get_info_apart(cls):
        number_rooms = input("Enter number_rooms:")
        number_floor = input("Enter number_floor:")
        floor = input("Enter floor:")
        parking = input("Enter parking:")
        return cls(number_rooms, number_floor, floor, parking)

    def change_to_dict(self):
        dict_info_Apartment = vars(self)

        return dict_info_Apartment

    def Edit(self):
        dict_info_Apartment = Apartment.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Apartment.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Apartment.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Apartment.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Home(Store):
    def __init__(self, tenant, owner, address, active_inactive, telephone, area,
                 mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms, number_floor,
                 area_yard):
        super().__init__(tenant, owner, address, active_inactive, telephone, area,
                         mortgage_amount, rental_amount, sales_amount, sales_rental)
        self.number_rooms = number_rooms
        self.number_floor = number_floor
        self.area_yard = area_yard

    @classmethod
    def get_info_home(cls):
        number_rooms = input("Enter number_rooms:")
        number_floor = input("Enter number_floor:")
        area_yard = input("Enter area yard:")
        return cls(number_rooms, number_floor, area_yard)

    def change_to_dict(self):
        dict_info_Home = vars(self)

        return dict_info_Home

    def Edit(self):
        dict_info_Home = Home.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?:'))
        for i in range(number_of_edit):
            key = input("Enter the attribute you want to change:")
            list_of_key_edit.append(key)

        for j in list_of_key_edit:
            if j in dict_info_Home.keys():
                for k in range(number_of_edit):
                    value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                    list_of_value_edit.append(value)
                    dict_info_Home.update({list_of_key_edit[k]: list_of_value_edit[k]})
                break

            else:
                print("Not found!")

    def show_info(self):

        for k, v in Home.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


w0 = []


class RealEstateAdvisor:
    def __init__(self, sales_amount, sales_rental, area, martage_amount, rental_amount):
        self.sales_amount = sales_amount
        self.sales_rental = sales_rental
        self.area = area
        self.martage_amount = martage_amount
        self.rental_amount = rental_amount

    @classmethod
    def get_info(cls):
        mortgage_amount = input(" Enter mortgage_amount")
        rental_amount = input("Enter rental_amount")
        sales_amount = input(" Enter sales_amount")
        sales_rental = input("Enter sales_rental")
        area = input("Enter area")
        return cls(mortgage_amount, rental_amount, sales_amount, sales_rental, area)

    @staticmethod
    def search_home():
        c = Home.change_to_dict(a)
        for i, value in c.items():
            w0.append(value)
        x0 = " ".join(w0)
        y0 = re.findall("mortgage_amount|rental_amount|sales_amount|sales_rental", x0)

        return y0
        # # myit = iter(c)
        # for i in range(3):
        #     print(next(myit), "", end='')
i = Person
i.email_address_validation()