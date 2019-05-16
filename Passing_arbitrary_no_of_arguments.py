# Assume toppings in the pizza orders can be none or many
# Hence arguments are not fixed, it can be any number of arguments

def make_pizza (size, *toppings):
    ''' Print the list of toppings that were choosen'''
    print ("\nFollowing toppings will be added to".format(size))
    for topping in toppings:
        print ("- "+topping)

# Single topping
make_pizza(16, 'Pepperoni')

# multiple number of toppings
make_pizza(12, 'mushroom', 'sweet corn', 'tanduri chicken')
