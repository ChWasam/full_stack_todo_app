from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to TaskTrack todo app"}

@app.get("/todo")
async def read_todos():
    return {"content":"dummy_todo"}
