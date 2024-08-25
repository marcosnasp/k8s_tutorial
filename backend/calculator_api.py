from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

class OperationInput(BaseModel):
    x: float
    y: float


@app.post("/add")
def add(input: OperationInput):
    logging.info(f"Function 'add' called with x={input.x}, y={input.y}")
    result = input.x + input.y
    return {"result": result}


@app.post("/subtract")
def subtract(input: OperationInput):
    logging.info(f"Function 'subtract' called with x={input.x}, y={input.y}")
    result = input.x - input.y
    return {"result": result}


@app.post("/multiply")
def multiply(input: OperationInput):
    loggin.info(f"Function 'multiply' called with x={input.x}, y={input.y}")
    result = input.x * input.y
    return {"result": result}


@app.post("/divide")
def divide(input: OperationInput):
    logging.info(f"Function 'divide' called with x={input.x}, y={input.y}")
    if input.y == 0:
        logging.error("Division by zero attempt")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = input.x / input.y
    return {"result": result}

