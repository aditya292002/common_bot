from fastapi import APIRouter

from ..utility import passwd_utils
from .. import models, schemas
from fastapi import Depends, status, Response, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    print(user.email)
    print(user.password)
    
    # hash the password - user.password
    hashed_password = passwd_utils.hash(user.password)
    user.password = hashed_password
    

    new_user = models.User(**user.dict())  # dictonary unpacking allow us to pass each of the element or(pair) of the dict as individual arguments 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user