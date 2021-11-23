import re
import pandas as pd
import csv


class Address:

    def __init__(self, city_name, street_name, number_plaque, number_postal_code):
        self.city = city_name
        self.street = street_name
        self.number_plaque = number_plaque
        self.number_postal_code = number_postal_code

    def change_to_dict(self):
        dict_info_Adress = vars(self)

        return dict_info_Adress

    def Edit(self):
        dict_info_Adress = Address.change_to_dict(self)

        list_of_key_edit = []
        list_of_value_edit = []
        number_of_edit = int(input('How many do you want to change?'))
        for i in range(number_of_edit):
            print("city\t\tstreet\t\tnumber_plaque\t\tnumber_postal_code")
            key = input("Enter the attribute you want to change:")
            if key in dict_info_Adress.keys():
                list_of_key_edit.append(key)
            else:
                print("The key not found!")
        for j in range(len(list_of_key_edit)):
            value = input(f"Enter the value of {list_of_key_edit[j]} you want to change:")
            list_of_value_edit.append(value)
            dict_info_Adress.update({list_of_key_edit[j]: list_of_value_edit[j]})

    def show_info(self):

        for k, v in Address.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Person:

    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.email = ''
        self.national_code = None
        self.phone_number = phone_number

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
                if len(national_code) == 10:
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
        number_of_edit = int(input('How many do you want to change?'))
        for j in range(number_of_edit):
            print("firstname\t\tlastname\t\temail\t\tnational_code\t\tphone_number")
            key = input("Enter the attribute you want to change:")
            if key not in dict_info_Person.keys():
                print("This key not found!")
            else:
                list_of_key_edit.append(key)

        for k in range(len(list_of_key_edit)):
            if list_of_key_edit[k] == "email":
                while True:
                    try:
                        value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                        if value.endswith(".com"):
                            if value.startswith('@') == False:
                                if re.findall("@", value):

                                    list_of_value_edit.append(value)
                                    dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})
                                    break

                                else:
                                    raise ValueError()
                            else:

                                raise ValueError()

                        else:

                            raise ValueError()

                    except  ValueError:
                        print("email is wrong!please try again")
            elif list_of_key_edit[k] == "national_code":
                while True:
                    try:
                        value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                        if len(value) == 10:
                            list_of_value_edit.append(value)
                            dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})
                            break
                        else:
                            raise ValueError()

                    except ValueError:
                        print("it is wrong try again!please try again")

            else:
                value = input(f"Enter the value of {list_of_key_edit[k]} you want to change:")
                list_of_value_edit.append(value)
                dict_info_Person.update({list_of_key_edit[k]: list_of_value_edit[k]})

    def show_info(self):

        for k, v in Person.change_to_dict(self).items():
            print(k, '=', v, end=" , ")
        else:
            print('\n')


class Store:

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


class RealEstateAdvisor:
    def __init__(self, sales_rental, area, martage_amount,rental_amount,sales_amount):
        self.martage_amount = martage_amount
        self.rental_amount = rental_amount
        self.sales_amount = sales_amount
        self.sales_rental = sales_rental
        self.area = area
    # @classmethod
    # def get_info(cls):
    #     mortgage_amount = input(" Enter mortgage_amount")
    #     rental_amount = input("Enter rental_amount")
    #     sales_amount = input(" Enter sales_amount")
    #     sales_rental = input("Enter sales_rental")
    #     area = input("Enter area")
    #     return cls(mortgage_amount, rental_amount, sales_amount, sales_rental, area)
    #
    # @staticmethod
    # def search_home():
    #     c = Home.change_to_dict(a)
    #     for i, value in c.items():
    #         w0.append(value)
    #     x0 = " ".join(w0)
    #     y0 = re.findall("mortgage_amount|rental_amount|sales_amount|sales_rental", x0)
    #
    #     return y0
    #     # # myit = iter(c)
    #     # for i in range(3):
    #     #     print(next(myit), "", end='')


def give_address():
    city_name = input('Enter your city: ')
    street_name = input('Enter your street: ')
    number_plaque = input("Enter your plaque: ")
    number_postal_code = input("Enter your postal code: ")

    print("succesfully addad!")
    address_obj = Address(city_name, street_name, number_plaque, number_postal_code)
    address_obj.change_to_dict()
    return address_obj


person_list = []
apart_list = []
home_list = []
store_list = []


def get_info_person():
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    phone_number = input("Enter the phone number: ")
    person_obj = Person(firstname, lastname, phone_number)
    person_obj.change_to_dict()
    list1 = [firstname, lastname]
    join_store = "_".join(list1)
    person_list.append(join_store)

    return person_obj


def get_info_store():
    tenant = input("Enter tenant: ")
    owner = input("Enter owner: ")
    mortgage_amount = input("Enter mortgage_amount: ")
    rental_amount = input("Enter Rental_amount: ")
    sales_rental = input("Enter sales_rental: ")
    address = input("Enter address: ")
    active_inactive = input("Enter active or inactive: ")
    telephone = input("Enter telephone number: ")
    sales_amount = input("Enter sales_amount: ")
    area = input("Enter area: ")
    store_obj = Store(tenant, owner, address, active_inactive, telephone, area,
                      mortgage_amount, rental_amount, sales_amount, sales_rental)
    dict_store = store_obj.change_to_dict()
    list1 = [mortgage_amount, rental_amount, sales_amount, sales_rental, area]
    join_store = " ".join(list1)
    store_list.append(join_store)
    from csv import DictWriter
    field_names_store = ['tenant', 'owner', 'address', 'active_inactive', 'telephone', 'area',
                         'mortgage_amount', 'rental_amount', 'sales_amount', 'sales_rental']
    # assign header columns
    # open CSV file and assign header
    with open("csv_file1 (1).csv", 'a') as file:
        dw = csv.DictWriter(file, delimiter=',',
                            fieldnames=field_names_store)
        dw.writeheader()

    # display csv file
    fileContent = pd.read_csv("csv_file1 (1).csv")
    fileContent

    with open('csv_file1 (1).csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names_store)

        dictwriter_object.writerow(dict_store)
        f_object.close()

    return store_obj


def get_info_apart():
    # common with store
    tenant = input("Enter tenant: ")
    owner = input("Enter owner: ")
    mortgage_amount = input("Enter mortgage_amount: ")
    rental_amount = input("Enter Rental_amount: ")
    sales_rental = input("Enter sales_rental: ")
    address = input("Enter address: ")
    active_inactive = input("Enter active or inactive: ")
    telephone = input("Enter telephone number: ")
    sales_amount = input("Enter sales_amount: ")
    # other
    area = input("Enter area: ")
    number_rooms = input("Enter number_rooms: ")
    number_floor = input("Enter number_floor: ")
    floor = input("Enter floor: ")
    parking = input("Enter parking: ")
    apartment_obj = Apartment(tenant, owner, address, active_inactive, telephone, area,
                              mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms,
                              number_floor, floor,
                              parking)
    dict_apart = apartment_obj.change_to_dict()
    list1 = [mortgage_amount,rental_amount,sales_amount,sales_rental,area]
    join_apart =" ".join(list1)
    apart_list.append(join_apart)

    from csv import DictWriter
    field_names_apart = ['tenant', 'owner', 'address', 'active_inactive', 'telephone', 'area',
                         'mortgage_amount', 'rental_amount', 'sales_amount', 'sales_rental', 'sales_amount',
                         'sales_rental', 'number_rooms',
                         'number_floor', 'floor',
                         'parking']
    # assign header columns
    # open CSV file and assign header
    with open("csv_file1 (1).csv", 'a') as file:
        dw = csv.DictWriter(file, delimiter=',',
                            fieldnames=field_names_apart)
        dw.writeheader()

    # display csv file
    fileContent = pd.read_csv("csv_file1 (1).csv")
    fileContent

    with open('csv_file1 (1).csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names_apart)

        dictwriter_object.writerow(dict_apart)
        f_object.close()

    return apartment_obj


def get_info_home():
    # common with store
    tenant = input("Enter tenant: ")
    owner = input("Enter owner: ")
    mortgage_amount = input("Enter mortgage_amount: ")
    rental_amount = input("Enter Rental_amount: ")
    sales_rental = input("Enter sales_rental: ")
    address = input("Enter address: ")
    active_inactive = input("Enter active or inactive: ")
    telephone = input("Enter telephone number: ")
    sales_amount = input("Enter sales_amount: ")
    area = input("Enter area: ")
    # other
    number_rooms = input("Enter number_rooms: ")
    number_floor = input("Enter number_floor: ")
    area_yard = input("Enter area yard: ")
    home_obj = Home(tenant, owner, address, active_inactive, telephone, area,
                    mortgage_amount, rental_amount, sales_amount, sales_rental, number_rooms, number_floor,
                    area_yard)
    dict_home = home_obj.change_to_dict()
    list1 = [mortgage_amount, rental_amount, sales_amount, sales_rental, area]
    join_home = " ".join(list1)
    home_list.append(join_home)
    from csv import DictWriter
    field_names_home = ['tenant', 'owner', 'address', 'active_inactive', 'telephone', 'area',
                        'mortgage_amount', 'rental_amount', 'sales_amount', 'sales_rental', 'number_rooms',
                        'number_floor',
                        'area_yard']
    # assign header columns
    # open CSV file and assign header
    with open("csv_file1 (1).csv", 'a') as file:
        dw = csv.DictWriter(file, delimiter=',',
                            fieldnames=field_names_home)
        dw.writeheader()

    # display csv file
    fileContent = pd.read_csv("csv_file1 (1).csv")
    fileContent

    with open('csv_file1 (1).csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names_home)

        dictwriter_object.writerow(dict_home)
        f_object.close()

    return home_obj


def serch():
    for name in person_list:
        print("1.apaertment\t\t2.home\t\t3.store")
        number_building = int(input(f"{name} what kind of building do you want? "))
        martage_amount = input("Enter martage_amount: ")
        rental_amount = input("Enter rental_amount: ")
        sales_amount = input("Enter sales_amount: ")
        sales_rental = input("Enter sales_rental: ")
        area = input("Enter area: ")
        RealEstateAdvisor_obj = RealEstateAdvisor(sales_rental, area, martage_amount,rental_amount,sales_amount)
        if number_building == 1:
            for i in range(len(apart_list)):

                y0 = re.findall(f"{martage_amount} {rental_amount} {sales_amount} {sales_rental} {area}", apart_list[i])
                if y0:
                    print(f"{name} the apartment that you want is available")
                    del apart_list[i]
                else:
                    print("No match!")
        elif number_building == 2:

            for i in range(len(home_list)):

                y0 = re.findall(f"{martage_amount} {rental_amount} {sales_amount} {sales_rental} {area}",home_list[i])
                if y0:
                    print(f"{name} the home that you want is available")
                    del home_list[i]
                else:
                    print("No match!")
        elif number_building == 3:

            for i in range(len(store_list)):

                y0 = re.findall(f"{martage_amount} {rental_amount} {sales_amount} {sales_rental} {area}", store_list[i])
                if y0:
                    print(f"{name} the store that you want is available")
                    del store_list[i]
                else:
                    print("No match!")
        else:
            print("please try again")


def menu():
    while True:
        print(
            "class>> 1.Address\t\t2.Person\t\t3.Apartment\t\t4.Home\t\t5.Store\t\t6.Real Estate Advisor\t\t7.Transaction\t\t\tQuit:else")
        number_class = input("Enter a number of class: ")

        if number_class == "1":
            address_obj = give_address()

            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                address_number = input("Choose your method: ")
                if address_number == "1":
                    address_obj.Edit()
                elif address_number == "2":
                    address_obj.show_info()
                else:
                    break

        elif number_class == "2":
            person_obj = get_info_person()

            while True:
                print(
                    "method>> 1.email_address_validation\t\t2.national_code_validation\t\t3.Edit\t\t4.show_info\t\t\tQuit:else")
                person_number = input("Choose a number of method: ")
                if person_number == "1":
                    person_obj.email_address_validation()
                elif person_number == "2":
                    person_obj.national_code_validation()
                elif person_number == "3":
                    person_obj.Edit()
                elif person_number == "4":
                    person_obj.show_info()
                else:
                    break

        elif number_class == "3":
            apartment_obj = get_info_apart()
            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                apartment_number = input("Choose your method: ")
                if apartment_number == "1":
                    apartment_obj.Edit()
                elif apartment_number == "2":
                    apartment_obj.show_info()
                else:
                    break

        elif number_class == "4":
            home_obj = get_info_home()

            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                home_number = input("Choose your method: ")
                if home_number == "1":
                    home_obj.Edit()
                elif home_number == "2":
                    home_obj.show_info()
                else:
                    break
        elif number_class == "5":
            store_obj = get_info_store()
            while True:
                print("method>> 1.Edit\t\t2.show info\t\t\tQuit:else")
                store_number = input("Choose your method: ")
                if store_number == "1":
                    store_obj.Edit()
                elif store_number == "2":
                    store_obj.show_info()
                else:
                    break

        elif number_class == "6":
            serch()
        else:
            break
        # if number_class == "7":


menu()
