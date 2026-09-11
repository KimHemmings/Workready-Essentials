from backend.utils.supabase import get_supabase
from fastapi import FastAPI
from backend.auth import router as auth_router
from backend.jobseekers import router as jobseekers_router
from backend.providers import router as providers_router
from backend.modules import router as modules_router
from backend.interviews import router as interviews_router
from backend.jobsearch import router as jobsearch_router
from backend.resume import router as resume_router
from backend.evidence import router as evidence_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router, prefix="/auth")
app.include_router(jobseekers_router, prefix="/jobseekers")
app.include_router(providers_router, prefix="/providers")
app.include_router(modules_router, prefix="/modules")
app.include_router(interviews_router, prefix="/interviews")
app.include_router(jobsearch_router, prefix="/jobsearch")
app.include_router(resume_router, prefix="/resume")
app.include_router(evidence_router, prefix="/evidence")
