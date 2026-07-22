from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(num1: int, num2: int, operation: str):

    if operation == "add":
        result = num1 + num2

    elif operation == "sub":
        result = num1 - num2

    elif operation == "mul":
        result = num1 * num2

    elif operation == "div":
        result = num1 / num2

    elif operation == "power":
        result = num1 ** num2

    elif operation == "mod":
        result = num1 % num2

    else:
        return {"error": "Invalid operation"}

    return {"result": result}