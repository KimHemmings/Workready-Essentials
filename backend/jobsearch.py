from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.get("/")
def list_jobs():
    return supabase.table("jobsearch").select("*").execute()
