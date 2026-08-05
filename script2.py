from fastapi import FastAPI
app = FastAPI()
@app.get("/User_Name")
def User_Name(Name:str,age:int):
   return {"Name":Name,"age":age}