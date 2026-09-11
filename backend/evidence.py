from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.post("/")
def upload_evidence(data: dict):
    return supabase.table("evidence").insert(data).execute()
