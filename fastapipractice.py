from fastapi import FastAPI,HTTPException

app = FastAPI()

todos = ["learn AI", "Practice for driving test", "Go for a walk"]

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{id}")
def get_one_todo(id: int):
    if id<0 or id>=len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[id]

# str is QUERY parameter or query string  - str is after the ?
@app.post("/todos")
def add_todo(todo: str): 
    todos.append(todo)
    return {"message": "Todo added successfully", "todos": todos}   
# here str query parameter         

# Instead of URL parameters or query parameter, send data in the request body using a plain dict. This is more flexible and allows you to send more complex data structures.
@app.post("/todosDict")
def create_todo(todo: dict):
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}

# id is a PATH parameter - id is part of the URL
@app.put("/todos/{id}")
def update_todo(id: int, todo: str):
    # validation
    if id < 0 or id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todos[id] = todo        # replace old todo with new one
    return {"message": "Todo updated", "todo": todos}