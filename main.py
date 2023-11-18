from fastapi import FastAPI, Depends, HTTPException, status, Request, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import Users
from database import SessionLocal
import secrets
from pydantic import BaseModel

app = FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    password: str
    session_id: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Placeholder function - replace with your implementation
security = HTTPBasic()

# Custom middleware for session-based authentication
def get_authenticated_user_from_session_id(request: Request, session_id: str = Cookie(None), db: Session = Depends(get_db)):
    if session_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session ID",
        )
    user_id = get_user_id_from_session_id(session_id, db)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session ID",
        )
    user = get_user(user_id, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user

def get_user_id_from_session_id(session_id: str, db: Session):
    # Replace this with your actual database query to get user_id from the session_id
    # Example assuming you have a column 'session_id' in your Users table:
    user = db.query(Users).filter(Users.session_id == session_id).first()
    return user.id if user else None

def get_user(user_id: int, db: Session):
    return db.query(Users).filter(Users.id == user_id).first()

@app.post("/signup")
async def sign_up(create_user_request: CreateUserRequest, db: Session = Depends(get_db)):
    user = db.query(Users).filter_by(username=create_user_request.username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )

    create_user_model = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )

    db.add(create_user_model)
    db.commit()

    return {"message": "User registered successfully"}

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = db.query(Users).filter_by(username=credentials.username).first()
    if user is None or not bcrypt_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

def create_session(user_id: int, db: Session):
    session_id = secrets.token_hex(16)
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        user.session_id = session_id
        db.commit()
    return session_id

# Login endpoint - Creates a new session
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = authenticate_user(credentials, db)
    session_id = create_session(user.id, db)
    return {"message": "Logged in successfully", "session_id": session_id}

# Get current user endpoint - Returns the user corresponding to the session ID
@app.get("/getusers/me")
def read_current_user(user: dict = Depends(get_authenticated_user_from_session_id)):
    return user

# Protected endpoint - Requires authentication
@app.get("/protected")
def protected_endpoint(user: dict = Depends(get_authenticated_user_from_session_id)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated")
    return {"message": "This user can connect to a protected endpoint after successfully authenticated", "user": user}
