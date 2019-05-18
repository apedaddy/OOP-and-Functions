def gen_sublists(main_list):
    sublists = []

    for main_list_counter in range (len(main_list) + 1):

        for sec_list_counter in range (main_list_counter+1, len(main_list)+1):

            sub = main_list[main_list_counter:sec_list_counter]
            sublists.append(sub)
    return sublists

mylist = []
tot_elements = int(input("Enter how many elements you want in the listing: "))

for counter in range (tot_elements):
    list_elem = int(input(f"Enter INDEX -> {counter} element for list: "))
    mylist.append(list_elem)

list_of_sublist= (gen_sublists(mylist))


print (f"\nNumber of sublist generated: {len(list_of_sublist)}")

print (list_of_sublist)
