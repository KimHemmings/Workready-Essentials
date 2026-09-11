from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.post("/generate")
def generate_resume(data: dict):
    return {"message": "Resume generated", "input": data}
