'''
Make pizza from given size value and any number of toppings
'''
def make_pizza(size, *toppings):
    print ("\nMaking a "+ str(size) + "-inch pizza with following topping(s)")
    for topping in toppings:
        print ("- "+topping)
