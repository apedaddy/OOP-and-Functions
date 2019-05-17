class ListOperation():
    def __init__(self):
        self.check_list = [ ]
    def add_elements(self,a):
        self.check_list.append(a)
    def remove_elements(self,b):
        self.check_list.remove(b)
    def display_elements(self):
        return (self.check_list)

mylist = ListOperation()
operation_select = 1

while operation_select !=0:
    print ("0. Exit")
    print ("1. Add elements")
    print ("2. Delete elements")
    print ("3. Display")
    operation_select = int(input("\nEnter your selection from above"))
    if operation_select ==1:
        num = int(input("Enter number to append:"))
        mylist.add_elements(num)
    elif operation_select ==2:
        print (mylist.display_elements())
        if (len(mylist.display_elements())==0):
            print ("ZERO ENTRIES! No removal possible")
        else:
            num = int(input("Enter number to remove:"))
        mylist.remove_elements(num)
    elif operation_select ==3:
        print (f"List of your numbers is: {mylist.display_elements()}")
        print()
    elif operation_select ==0:
        print ("Exiting ..........")
    else:
        print ("Invalid number entered")
print()



