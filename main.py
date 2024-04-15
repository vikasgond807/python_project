from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def main():
    return "Hello world "

@app.get("/api/v1/goals")
def api():

    return {"goal1":"Value"}