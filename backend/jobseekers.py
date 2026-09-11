from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.get("/")
def list_jobseekers():
    return supabase.table("jobseekers").select("*").execute()

@router.post("/")
def create_jobseeker(data: dict):
    return supabase.table("jobseekers").insert(data).execute()
