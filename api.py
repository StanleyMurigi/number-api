from fastapi import FastAPI, Query, HTTPException
import requests

app = FastAPI()

def is_armstrong(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == number

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect(number: int) -> bool:
    return number > 1 and sum(i for i in range(1, number) if number % i == 0) == number

def get_fun_fact(number: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
    except requests.RequestException:
        return "Could not retrieve fun fact."
    return "No fun fact available."

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="The number to classify")):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")
    
    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number),
    }
    return response_data
