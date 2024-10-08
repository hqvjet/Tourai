from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, service, favourite, comment, admin, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(service.router)
app.include_router(comment.router)
app.include_router(favourite.router)

app.mount("/res", StaticFiles(directory="res"), name="res")