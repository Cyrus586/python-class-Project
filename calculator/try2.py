
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        add = lambda num1, num2: num1+num2
        return add

    def subtraction(self):
        sub = lambda num1,num2: num1-num2
        return sub

    def multiplicaion(self):
        mul = lambda num1,num2: num1*num2
        return mul

    def division(self):
        div = lambda num1,num2: num1/num2
        return div

class User_input(Calculator):
    print("\n Select your operation type: ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Sqauring")
    print("F. Square root")

    user_choice = input("Enter your option: ").lower()

    if user_choice == "a":
        

    elif user_choice == "b":
        

    elif user_choice == "c":
        

    elif user_choice == "d":
        



if __name__ == "__main__":

    num1 = int(input("Enter the first number: "))
    num2 = int(input("nter the second number: "))




