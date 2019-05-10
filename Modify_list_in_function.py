def print_models(unprinted_designs, completed_models):
    '''
    Check as if each design taken to print out, until none left
    in the list "unprinted_designs"
    '''

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print ("printing now..... " + current_design)
        completed_models.append(current_design)

def show_comleted_models(completed_models):
    # Showing all printed models
    print ("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robo case', 'keyring', 'stylus']
completed_models = []

# [:] Prevent original listing to be modified.
# print_models function called on copied version of list, hence original remains same

print_models(unprinted_designs[:], completed_models)
show_comleted_models(completed_models)
print()
print('ORIGINAL LIST')
print(unprinted_designs[::])