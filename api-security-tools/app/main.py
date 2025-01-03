from fastapi import FastAPI
from app.routes import whois, nmap, shodan

app = FastAPI(
    title="Security Tools API",
    description="API para consolidar ferramentas de OSINT, pentest e análise de vulnerabilidades.",
    version="1.0.0"
)

# Rotas
app.include_router(whois.router, prefix="/whois")
app.include_router(nmap.router, prefix="/nmap")
app.include_router(shodan.router, prefix="/shodan")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Security Tools!"}
