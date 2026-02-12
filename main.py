from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from fastapi import Form

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")

def index():
    return FileResponse("templates/index.html")

class Dados(BaseModel):
    hora: str 

def porcentagem(hora_user):

    separador = -1
    # hora_user = input("Que horas são: ")

    while separador == -1:
        separador = hora_user.find(":")
        if separador == -1:
            hora_user = hora_user + ":00"

    hora = int(hora_user[:separador])
    minutos = hora_user[separador+1:]
    minutos = "0." + str(int(minutos) // 6) + "0"
    hora_real = hora + float(minutos)

    #hora = 8
    porcentagem = 100 - ((hora_real - 7) * 15)
    porcentagem = int(porcentagem)
    # print("---", str(porcentagem) + "% ---")
    return(str(porcentagem) + "%")

@app.post("/descobrir")

async def descobrir(dados: Dados):
    resultado = porcentagem(dados.hora)
    return {"resultado": resultado}