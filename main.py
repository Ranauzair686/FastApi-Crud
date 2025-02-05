from fastapi import FastAPI, Body
app = FastAPI()
fakeDatabase={
    1:{'task' : 'This is task 1'},
    2:{'task' : 'This is task 2'},
    3:{'task' : 'This is task 3'},
    4:{'task' : 'This is task 4'},
}

@app.get("/")   
def getTasks():
    return fakeDatabase

#1st post method 
@app.post("/")
def addTask(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {'task' : task}
    return fakeDatabase

#2nd post method
# @app.post("/")
# def addTask(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task' : body['task']}
#     return fakeDatabase
       
@app.get("/{id}")
def getTask(id:int):
    return fakeDatabase[id]

@app.put("/{id}")
def updateTask(id:int, task: str):
    fakeDatabase[id]['task'] = task
    return fakeDatabase

@app.delete("/{id}")
def removeTask(id:int):
    del fakeDatabase[id]
    return fakeDatabase