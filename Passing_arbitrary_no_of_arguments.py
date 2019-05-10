# Assume toppings in the pizza orders can be none or many
# Hence arguments are not fixed, it can be any number of arguments

def make_pizza (*toppings):
    ''' Print the list of toppings that were choosen'''
    print ("\nFollowing toppings will be added")
    for topping in toppings:
        print ("- "+topping)

# Single topping
make_pizza('Pepperoni')

# multiple number of toppings
make_pizza('mushroom', 'sweet corn', 'tanduri chicken')
