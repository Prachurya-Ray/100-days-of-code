
'''
A QSR service where customer can choose which menu to take then choose which item from the menu to take,
if wants can choose more item. Then also can choose more menus and items.
Will get final item bought list and total cost.'''

class Menu():
    menus = {1: "Momo", 2: "Pizza", 3: "Burger", 4: "Sandwich", 5: "Fried Chicken"}
    momos = {1: {"Fried Momo": 350}, 2: {"Grilled Momo": 240}, 3: {"Steamed Momo": 185}}
    pizzas = {1: {"Paneer pizza": 450}, 2: {"Mushroom pizza": 325}, 3: {"Chicken pizza": 550}}
    burgers = {1: {"Fried burger": 200}, 2: {"Veg burger": 250}, 3: {"Chicken burger": 350}}
    sandwiches = {1: {"Plain sandwich": 250}, 2: {"Grilled sandwich": 350}, 3: {"Egg sandwich": 450}}
    fried_chicken = {1: {"Fried Chicken 'Small'": 250}, 2: {"Fried Chicken 'Medium'": 450}, 3: {"Fried Chicken 'Large'": 750}}

    all_item = {}
    total = 0

    def Totals(self):
        '''Totals the order'''
        for i in Menu.all_item:
            Menu.total = Menu.total + Menu.all_item[i]

    def Final_print(self):
        '''Prints the order and total amount'''
        Menu.Totals(self)           # Calls Total() function to ttal the value
        print("\t\nYour Orders :\n")
        for i, j in Menu.all_item.items():
            print('\t', i, ' : ', j)
        print("\t\nTotal :\t", Menu.total)


class Order(Menu):

    def Categories(self):
        '''Take The order according to the option choosed by customer'''

        if self.it == 1:
            for i, j in Menu.momos.items():
                print('\t', i, ' : ')
                for k, l in j.items():
                    print('\t\t', k, ' = ', l)
            while True:
                fi = int(input(">> "))
                Menu.all_item.update(Menu.momos[fi])    # update (add) the choosed item from the inner most dict
                a = input("Want More Momos?Y/N >> ")
                if a == 'N' or a == 'n':
                    break

        elif self.it == 2:
            for i, j in Menu.pizzas.items():
                print('\t', i, ' : ')
                for k, l in j.items():
                    print('\t\t', k, ' = ', l)
            while True:
                fi = int(input(">> "))
                Menu.all_item.update(Menu.pizzas[fi])    # update (add) the choosed item from the inner most dict
                a = input("Want More Pizzas?Y/N >> ")
                if a == 'N' or a == 'n':
                    break

        elif self.it == 3:
            for i, j in Menu.burgers.items():
                print('\t', i, ' : ')
                for k, l in j.items():
                    print('\t\t', k, ' = ', l)

            # Order.loop(Menu.burgers)

            while True:
                fi = int(input(">> "))
                Menu.all_item.update(Menu.burgers[fi])   # update (add) the choosed item from the inner most dict
                a = input("Want More Burgers?Y/N >> ")
                if a == 'N' or a == 'n':
                    break

        elif self.it == 4:
            for i, j in Menu.sandwiches.items():
                print('\t', i, ' : ')
                for k, l in j.items():
                    print('\t\t', k, ' = ', l)
            while True:
                fi = int(input(">> "))
                Menu.all_item.update(Menu.sandwiches[fi])    # update (add) the choosed item from the inner most dict
                a = input("Want More Sandwich?Y/N >> ")
                if a == 'N' or a == 'n':
                    break

        elif self.it == 5:
            for i, j in Menu.fried_chicken.items():
                print('\t', i, ' : ')
                for k, l in j.items():
                    print('\t\t', k, ' = ', l)
            while True:
                fi = int(input(">>> "))
                Menu.all_item.update(Menu.fried_chicken[fi])     # update (add) the choosed item from the inner most dict
                a = input("Want More Fried Chicken?Y/N >> ")
                if a == 'N' or a == 'n':
                    break

    '''value = []
    value = Menu.all_item.values()
    total = sum(value)'''

    '''
    def loop(self, i):
        while True:
            a = input("Want More Pizzas?Y/N >> ")
            if a == 'N' or a == 'n':
                break
            fi = int(input(">> "))
            Order.all_item.update(i[fi])'''


def Init():
    '''Take what menu the customer wants'''
    i = 0
    while True:
        ite.it = int(input(">>> "))  # taking order
        ite.Categories()
        a = input("Want More Menus?Y/N >>> ")
        if a == 'N' or a == 'n':
            break
        for i, j in Menu.menus.items():
            print('\t', i, ' : ', j)


# ------------------------- START -------------------------

print("\n-------------------- Welcome --------------------\n"
      "\nSir/Mam What would you like to have for today?\n"
      "\tMenu:\n")

for i, j in Menu.menus.items():
    print('\t', i, ' : ', j)

ite = Order()
Init()
ite. Final_print()  # Prints the final order








