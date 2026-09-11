from fastapi import APIRouter
from backend.utils.supabase import get_supabase

router = APIRouter()
supabase = get_supabase()

@router.post("/login")
def login(payload: dict):
    email = payload.get("email")
    password = payload.get("password")
    return supabase.auth.sign_in_with_password({"email": email, "password": password})
