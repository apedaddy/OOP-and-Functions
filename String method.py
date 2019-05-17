class PrintString():
    def __init__(self):
        self.string = ""
    def get_string(self):
        self.string = input("Etner your string: ")
    def print_string(self):
        print ("\nThe string you entered is: ")
        print (self.string)

mystring = PrintString()
mystring.get_string()
mystring.print_string()