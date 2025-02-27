# External Dependencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# # Endpoints
# from endpoints.chats import router as endpoints_chats
# from endpoints.users import router as endpoints_users


app = FastAPI()
# app.include_router(endpoints_chats, prefix="/chats", tags=["chats"])
# app.include_router(endpoints_users, prefix="/users", tags=["users"])

@app.get("/")
def root():
    """Root endpoint to verify the API is running."""
    return {
        "message": "Welcome to API",
    }
