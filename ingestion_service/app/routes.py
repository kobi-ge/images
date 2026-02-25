from fastapi import APIRouter

router = APIRouter()

@router.get("/start")
def start_program():
    pass

@router.get("healthcheck")
def health():
    return {"status": "healthy"} 