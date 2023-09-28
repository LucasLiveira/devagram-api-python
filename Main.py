from fastapi import FastAPI

from routes.UsuarioRoute import router as UsuarioRote

from routes.AutenticacaoRoute import router as AutenticacaoRoute

app = FastAPI()

app.include_router(UsuarioRote, tags=["Usuário"], prefix="/api/usuario")
app.include_router(AutenticacaoRoute, tags=["Autenticação"], prefix="/api/auth")


@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status": "OK!"
    }