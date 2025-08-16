from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
 return {"message": "Olá turma, este é meu primeiro container com FastAPI!"}

@app.get("/Rafael")
def read_root():
 return {"message": "Olá turma, ete é o metodo do Rafael"}
