import numpy as np

class Calculator:
    def __init__(self, action) -> None:
        self.action = action
    def calculate(self, num1, num2):
        return self.action(num1, num2)

# These are the are operations
add = np.vectorize(lambda x,y: x+y)    #np.vectorize returns a vectorized verson of the function. It takes array inputs and evaluates the function
sub = np.vectorize(lambda x,y: x-y)
mul = np.vectorize(lambda x,y: x*y) 
div = np.vectorize(lambda x,y: x/y)

def calculating():
    print("\n Select your operation: ")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    
    user_choice = input("\nEnter your option: ").lower()
    num1 = int((input("\nEnter the first number: ")))
    num2 = int((input("Enter the second number: ")))

    array1= np.array([num1])
    array2= np.array([num2])

    if user_choice == "a":
        operation = Calculator(add)
        
    elif user_choice == "b":
        operation = Calculator(sub)
        
    elif user_choice == "c":
        operation = Calculator(mul)
        
    elif user_choice == "d":
        operation = Calculator(div)

    answer = operation.calculate(num1, num2)
    print(f"The answer is: {answer}")

if __name__ == '__main__':
    calculating()       





    




