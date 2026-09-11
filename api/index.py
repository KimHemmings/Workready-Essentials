from backend.main import app

# Vercel needs a handler called "app"
def handler(request, context):
    return app
