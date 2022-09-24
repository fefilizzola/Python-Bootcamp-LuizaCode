from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

#comando no terminal uvicorn hw_fastapi:app --reload

dados=[{"1":"A"},{"2":"B"},{"3":"C"}]
@app.get("/itens/")
async def read_item(numero: int=0):
    return dados[numero]