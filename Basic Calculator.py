'''
This program will accept two numbers from user and calculator on the basis
of option choosen by user from the given set of operations
'''

class Calculator():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def addition(self):
        return self.n1 + self.n2

    def subtraction(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        return self.n1 / self.n2
num1 = int(input("\nEnter your first number: "))
num2 = int(input("Enter your second number: "))
numbers = Calculator(num1, num2)

choice = 1
while choice !=0:
    print ("\n0. Exit \n1. Add \n2. Subtraction \n3. Multiplication \n4. Division")
    choice = int(input("Enter a choice from above list: "))
    if choice ==1:
        print (f"Sum of given numbers {num1} and {num2} is: {numbers.addition()}")
    elif choice ==2:
        print(f"Subtraction of given numbers {num1} and {num2} is: {numbers.subtraction()}")
    elif choice ==3:
        print(f"Multiplication of given numbers {num1} and {num2} is: {numbers.multiplication()}")
    elif choice ==4:
        print(f"Division of given numbers {num1} and {num2} is: {numbers.division()}")
    elif choice ==0:
        print ("Exit .....")
    else:
        print ("INVALID CHOICE! 'Select correct option from above'")

print()

