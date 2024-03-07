from flask import Flask, request, render_template, url_for

app = Flask(__name__)

class Calculator:
    def __init__(self, operation) -> None:
        self.operation = operation
    def calculate(self, number_1, number_2):
        return self.operation(number_1, number_2)
    
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: Division by Zero"


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        number_1 = float(request.form["num1"])
        number_2 = float(request.form["num2"])
        operation = request.form["operation"]
        
        if operation == "add":
            calc = Calculator(addition)
        elif operation == "subtract":
            calc = Calculator(subtraction)
        elif operation == "multiply":
            calc = Calculator(multiplication)
        elif operation == "divide":
            calc = Calculator(division)
        
        result = calc.calculate(number_1, number_2)
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)