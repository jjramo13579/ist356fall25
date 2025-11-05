from fastapi import FastAPI

app = FastAPI() # Create a FastAPI instance

@app.get("/") # Define a GET endpoint at the root path
def root(): #the path operation function
    return {"message": "Hello, World!"} # Return a JSON response with a greeting message

@app.get("/hi/{name}") # Define a GET endpoint with a path parameter
def say_hi(name: str): #the path operation function with a path parameter
    return {"message": f"Hi, {name}!"} # Return a JSON response with a personalized greeting message

@app.get("/roll/{number}d{sides}") # Define a GET endpoint with two path parameters
def roll_dice(number: int, sides: int):
    import random 
    rolls = [random.randint(1, sides) for _ in range(number)] # Simulate rolling dice
    total = sum(rolls) # Calculate the total of the rolls
    return {"rolls": rolls, "total": total} # Return a JSON response with the rolls and total

