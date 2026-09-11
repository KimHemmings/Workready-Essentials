from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.get("/")
def list_providers():
    return supabase.table("providers").select("*").execute()

@router.post("/")
def create_provider(data: dict):
    return supabase.table("providers").insert(data).execute()
