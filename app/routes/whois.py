from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/")
def get_whois(domain: str):
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True)
        return {"domain": domain, "whois": result.stdout}
    except Exception as e:
        return {"error": str(e)}
