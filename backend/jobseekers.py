from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()

@router.get("/")
def list_jobseekers():
    supabase = get_supabase()
    return supabase.table("jobseekers").select("*").execute()

@router.post("/")
def create_jobseeker(data: dict):
    supabase = get_supabase()
    return supabase.table("jobseekers").insert(data).execute()
